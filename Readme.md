# 🛠️ Resilient Playwright Automation (Basic Version)

This project demonstrates a basic framework for resilient browser automation using Python and [Playwright](https://playwright.dev/python/). It includes:

- Failure logging
- Mock AI-based fix suggestions
- Self-healing selectors
- Retry mechanism on failure

---

## 📁 Project Structure

```

resilient\_playwright\_basic/
├── ai\_suggester.py               # Mock AI suggestion for fixing selectors
├── logs/
│   └── test\_log.txt              # Test failure logs
├── main.py                       # Main runner
├── selectors.json                # Centralized selectors
├── test\_runner.py                # Orchestrator logic with retries
├── tests/
│   └── test\_login.py             # Example login test
├── utils/
│   └── self\_healing.py           # Selector self-healing mechanism
├── requirements.txt              # Dependencies

````

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
````

### 2. Run the Test

```bash
python main.py
```

---

## 🧠 How It Works

* The test script attempts to log in to a sample website using selectors from `selectors.json`.
* If the test fails:

  * The error is logged to `logs/test_log.txt`.
  * A mock AI module (`ai_suggester.py`) analyzes the logs.
  * The `self_healing.py` module randomly updates the `submit` selector to simulate "healing".
  * The test is re-run with the updated selector.

---

## 📚 File Descriptions

| File              | Purpose                                       |
| ----------------- | --------------------------------------------- |
| `main.py`         | Entrypoint to run tests                       |
| `test_runner.py`  | Core orchestration and retry logic            |
| `selectors.json`  | Stores selectors used in the test             |
| `ai_suggester.py` | Mocks AI-powered fix suggestions              |
| `self_healing.py` | Randomly alters selectors to simulate healing |
| `test_login.py`   | Playwright test using selectors from JSON     |

---

## 🧪 Test Example

The test navigates to:

```
https://example.com/login
```

Fills in:

* Username
* Password
* Clicks Login Button

Asserts the word **"Dashboard"** is present in the response.

---

## 🛡️ Limitations

* This version does **not use real AI tools** (Copilot/OpenAI).
* Selector healing is simulated via random updates.
* No DOM inspection or model-based fix logic.

---

## 📌 To Do

* Integrate real LLMs (e.g. OpenAI, Claude, GitHub Copilot).
* Add support for visual comparisons.
* Create a selector repository with confidence scores.
* Automate pull requests for selector changes.

---


