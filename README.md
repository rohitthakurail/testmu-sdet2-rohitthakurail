# testmu-sdet2-rohitthakurail
SDET-2 | Quality Engineering Challenge

## Framework Goals
This framework is designed to:
- Support UI, API and Integration testing in a single repository
- Reduce flaky tests through reusable waits and retries
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