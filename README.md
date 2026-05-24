# testmu-sdet2-rohitthakurail
SDET-2 | Quality Engineering Challenge

## Framework Goals
This framework is designed to:
- Support UI, API and Integration testing in a single repository
- Provide readable reports with screenshots/logs
- Enable fast onboarding for new QA engineers
- Support CI execution using GitHub Actions

## Tech Stack
- Python 3.11+
- Pytest
- Selenium
- Requests
- Allure Reporting
- GitHub Actions

## Why Python + Selenium + Requests?
- Mature ecosystem
- Easy CI integration
- Strong community support
- Flexible architecture

## Design Patterns
- Page Object Model (POM)
- Factory-based WebDriver management
- Externalized test data
- Config-driven execution
- Reusable utilities

# Architecture

```text
testmu-sdet2-rohitthakurail/
│
├── .github/workflows/
├── config/
├── data/
├── pages/
├── reports/
├── tests/
│   ├── api/
│   ├── ui/
│   └── integration/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

# Project Setup

## 1. Clone Repository

```bash
git clone https://github.com/rohitthakurail/testmu-sdet2-rohitthakurail.git
cd testmu-sdet2-rohitthakurail
```

## 2. Create Virtual Environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```
---

# Running Tests

## Run All Tests
```bash
pytest
```

## Run UI Tests
```bash
pytest tests/ui -m ui
```

## Run API Tests
```bash
pytest tests/api -m api
```

## Run Integration Tests
```bash
pytest tests/integration -m integration
```

---

# Reporting Features

- Screenshots on UI failure
- Logs attached to report.html
- API response logging
- HTML reporting

---

# GitHub Actions CI

Pipeline automatically:
- Installs dependencies
- Runs tests
- Generates artifacts
- Uploads reports

Location:
```text
.github/workflows/ci.yml
```

---
