# AccuKnox User Management Tests

Project Overview
Automated E2E test suite for OrangeHRM’s User Management module using Playwright (Python + Pytest).

---

Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/syedmysfira11-bit/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests


pip install -r requirements.txt

playwright install

Running Tests-

pytest

pytest --headed

pytest tests/test_add_user.py --headed



AccuKnox-user-management-tests/
│
├── pages/              # Page Object Model files
├── tests/              # Test cases (one per scenario)
├── conftest.py         # Playwright setup fixture
├── requirements.txt
└── README.md
