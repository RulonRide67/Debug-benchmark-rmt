"""Model clients. Only the Python standard library is used.

- OllamaClient: a locally served open-weights model (recommended: fixed weights,
  no data leaves the machine, reproducible).
- OpenAICompatClient: any OpenAI-compatible chat endpoint (API key from env var).
- Mock clients: used ONLY to test the pipeline. They are not models and their
  outputs must never be reported as model results.
"""
import json
import os
import urllib.request


class OllamaClient:
    def __init__(self, model, host="http://localhost:11434", temperature=0.0, seed=42,
                 num_ctx=4096, timeout=300):
        self.name = f"ollama:{model}"
        self.model, self.host = model, host.rstrip("/")
        self.options = {"temperature": temperature, "seed": seed, "num_ctx": num_ctx}
        self.timeout = timeout

    def chat(self, messages, temperature=None):
        opts = dict(self.options)
        if temperature is not None:
            opts["temperature"] = temperature
        body = json.dumps({"model": self.model, "messages": messages,
                           "stream": False, "options": opts}).encode()
        req = urllib.request.Request(f"{self.host}/api/chat", data=body,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read())["message"]["content"]


class OpenAICompatClient:
    def __init__(self, model, base_url, api_key_env="OPENAI_API_KEY", temperature=0.0,
                 seed=42, timeout=300):
        self.name = f"api:{model}"
        self.model, self.base_url = model, base_url.rstrip("/")
        self.key = os.environ.get(api_key_env, "")
        self.temperature, self.seed, self.timeout = temperature, seed, timeout

    def chat(self, messages, temperature=None):
        t = self.temperature if temperature is None else temperature
        body = json.dumps({"model": self.model, "messages": messages,
                           "temperature": t, "seed": self.seed}).encode()
        req = urllib.request.Request(f"{self.base_url}/chat/completions", data=body,
                                     headers={"Content-Type": "application/json",
                                              "Authorization": f"Bearer {self.key}"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read())["choices"][0]["message"]["content"]


class _MockBase:
    """Pipeline-test stand-ins. They read the bug's own files; they do not 'debug'."""
    def __init__(self):
        self.current_bug_dir = None
        self.turn = 0

    def start_bug(self, bug_dir):
        self.current_bug_dir, self.turn = bug_dir, 0

    def _read(self, name):
        with open(os.path.join(self.current_bug_dir, name)) as f:
            return f.read()


class MockNoChange(_MockBase):
    """Returns the buggy code unchanged -> lower bound, every bug must fail."""
    name = "mock:no_change"

    def chat(self, messages, temperature=None):
        return "```python\n" + self._read("buggy.py") + "```"


class MockOracle(_MockBase):
    """Returns the reference fix -> upper bound, every bug must pass."""
    name = "mock:oracle"

    def chat(self, messages, temperature=None):
        return "```python\n" + self._read("fixed.py") + "```"


class MockLearnsFromFeedback(_MockBase):
    """Wrong on the first turn, reference fix after feedback. Exercises the
    iterative loop and the logging of multi-turn attempts."""
    name = "mock:fix_after_feedback"

    def chat(self, messages, temperature=None):
        self.turn += 1
        return "```python\n" + self._read("buggy.py" if self.turn == 1 else "fixed.py") + "```"


def make_client(cfg):
    kind = cfg["provider"]
    if kind == "ollama":
        return OllamaClient(cfg["model"], cfg.get("host", "http://localhost:11434"),
                            cfg.get("temperature", 0.0), cfg.get("seed", 42))
    if kind == "openai_compat":
        return OpenAICompatClient(cfg["model"], cfg["base_url"],
                                  cfg.get("api_key_env", "OPENAI_API_KEY"),
                                  cfg.get("temperature", 0.0), cfg.get("seed", 42))
    return {"mock_no_change": MockNoChange, "mock_oracle": MockOracle,
            "mock_feedback": MockLearnsFromFeedback}[kind]()
