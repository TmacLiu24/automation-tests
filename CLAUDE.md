# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based Playwright automation testing project for a schedule management web application (WFM). Tests validate login, schedule creation, and deletion operations.

**Target Application**: `https://wfm-web.warmheart.top/WFM-admin/`

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run tests
python tests/test_schedule.py        # Synchronous (local development)
python tests/test_schedule_async.py  # Asynchronous (Jenkins CI)
python tests/test_login.py           # Login test
```

## Architecture

**Pattern**: Page Object Model (POM)

```
pages/
├── base_page.py      # Base class with human-like delay utilities
├── login_page.py     # Login page object
└── schedule_page.py  # Schedule CRUD operations

tests/
├── test_schedule.py        # Sync tests
├── test_schedule_async.py  # Async tests (used by Jenkins)
└── test_login.py           # Login test
```

- `BasePage` provides `human_like_delay()` and `type_like_human()` for realistic interaction simulation
- Tests use async Playwright; Jenkins auto-detects headless mode via `JENKINS_HOME` env var

## CI/CD

- **Jenkins**: Pipeline in `Jenkinsfile` - installs dependencies, runs `test_schedule_async.py`
- **Qodana**: Linting configured in `qodana.yaml` (linter: `jetbrains/qodana-pycharm:2024.3`)

## Notes

- Error screenshots saved to `error_screenshot.png` on test failure
- Test credentials are hardcoded in test files
