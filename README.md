# 🛒 E-Commerce Automation Testing

End-to-end **E-Commerce test automation framework** built using **Python, Playwright, Pytest, BDD, API Testing, and GitHub Actions CI/CD**.

This project automates critical e-commerce workflows such as login, product selection, cart validation, checkout, and API testing. It also generates HTML test reports and automatically executes tests through GitHub Actions.

---

## 🚀 Project Overview

The goal of this project is to demonstrate a real-world **QA Automation / SDET testing framework** with:

* UI Automation
* Page Object Model (POM)
* BDD Testing
* Data-Driven Testing
* API Testing
* Pytest Fixtures
* Failure Screenshots
* HTML Test Reports
* Git & GitHub
* GitHub Actions CI/CD

The UI tests are implemented against **SauceDemo**, while API tests use **JSONPlaceholder**.

---

## 🛠️ Tech Stack

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Programming Language   |
| Playwright     | Web UI Automation      |
| Pytest         | Test Framework         |
| pytest-bdd     | BDD Testing            |
| Requests       | API Testing            |
| Pytest-HTML    | HTML Test Reports      |
| Git            | Version Control        |
| GitHub         | Source Code Repository |
| GitHub Actions | CI/CD Automation       |

---

## 📂 Project Structure

```text
E-Commerce-Automation/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── features/
│   └── login.feature
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── step_definitions/
│   └── test_login_steps.py
│
├── tests/
│   ├── api/
│   │   └── test_api.py
│   │
│   └── ui/
│       ├── test_login.py
│       ├── test_products.py
│       ├── test_cart.py
│       └── test_checkout.py
│
├── utils/
│   └── config.py
│
├── reports/
│   └── test_report.html
│
├── screenshots/
│   └── failed_test_screenshots
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧪 Test Coverage

### 🔐 UI Testing

The following e-commerce workflows are automated:

* Login with valid credentials
* Login with locked-out user
* Product page validation
* Add product to cart
* Cart validation
* Checkout
* Customer information entry
* Order completion

### 🔌 API Testing

API tests cover:

* GET users
* POST/create user
* Negative API testing
* HTTP status code validation
* JSON response validation

---

## 🥒 BDD Testing

BDD is implemented using **pytest-bdd**.

Example feature:

```gherkin
Feature: Login

  Scenario Outline: Login with different users

    Given I open the SauceDemo website
    When I login with username "<username>" and password "<password>"
    Then I should see the login result "<result>"

    Examples:
      | username        | password     | result  |
      | standard_user   | secret_sauce | success |
      | locked_out_user | secret_sauce | locked  |
```

This allows the same test scenario to be executed with multiple sets of test data.

---

## 🏗️ Page Object Model

The project follows the **Page Object Model (POM)** design pattern.

Each application page has a separate Python class containing its locators and actions.

Example:

```text
LoginPage
ProductsPage
CartPage
CheckoutPage
```

### Benefits

* Better code organization
* Reusable page methods
* Easier maintenance
* Reduced code duplication
* Cleaner test cases

---

## ⚙️ Pytest Fixtures

Reusable fixtures are defined in:

```text
conftest.py
```

For example, the project contains a fixture for logging into the application before executing tests.

This avoids repeating login steps across multiple UI tests.

---

## 📸 Failure Screenshots

The framework automatically captures a screenshot whenever a UI test fails.

Screenshots are stored in:

```text
screenshots/
```

Example:

```text
screenshots/
└── test_add_product_to_cart_failed.png
```

This helps with debugging failed automation tests.

---

## 📊 HTML Test Reports

The project uses **pytest-html** to generate HTML test reports.

Generate a report using:

```powershell
pytest tests/api tests/ui --html=reports/test_report.html --self-contained-html
```

The generated report will be available at:

```text
reports/test_report.html
```

Open it with:

```powershell
start reports\test_report.html
```

---

## 🔄 GitHub Actions CI/CD

The project uses **GitHub Actions** to automatically execute tests whenever code is pushed to the `main` branch or a pull request is created.

Workflow file:

```text
.github/workflows/ci.yml
```

### CI Pipeline

```text
Checkout Code
      ↓
Setup Python
      ↓
Install Dependencies
      ↓
Install Playwright Browsers
      ↓
Run API Tests
      ↓
Run UI Tests
      ↓
Generate HTML Report
      ↓
Upload Test Report Artifact
```

### CI Tests

The pipeline executes:

```powershell
pytest tests/api -v
```

and:

```powershell
pytest tests/ui -v
```

The HTML report is uploaded as a GitHub Actions artifact.

---

## ▶️ Installation

### 1. Clone the repository

```powershell
git clone https://github.com/nnrahuln/E-Commerce-Automation.git
```

### 2. Navigate to the project

```powershell
cd E-Commerce-Automation
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

### 6. Install Playwright browsers

```powershell
python -m playwright install
```

---

## ▶️ Running Tests

### Run all tests

```powershell
pytest -v
```

### Run UI tests

```powershell
pytest tests/ui -v
```

### Run API tests

```powershell
pytest tests/api -v
```

### Run BDD tests

```powershell
pytest step_definitions/test_login_steps.py -v
```

### Run UI tests with browser visible

```powershell
pytest tests/ui -v --headed
```

---

## 🧪 Test Results

Current automated test coverage includes:

```text
UI Tests
├── Login
├── Products
├── Cart
└── Checkout

API Tests
├── GET Users
├── POST User
└── Invalid User

BDD
└── Data-driven Login
```

All implemented tests are executed locally and through GitHub Actions CI/CD.

---

## 🔐 Test Application

### UI Application

SauceDemo:

```text
https://www.saucedemo.com/
```

### API

JSONPlaceholder:

```text
https://jsonplaceholder.typicode.com
```

---

## 📋 Requirements

The main dependencies are listed in:

```text
requirements.txt
```

Current framework uses:

```text
playwright
pytest
pytest-bdd
pytest-playwright
pytest-html
requests
```

---

## 🎯 Key QA Automation Concepts Demonstrated

This project demonstrates practical knowledge of:

* Manual-to-Automation Testing
* UI Automation
* API Automation
* End-to-End Testing
* Page Object Model
* Pytest
* Fixtures
* Assertions
* BDD
* Scenario Outline
* Data-Driven Testing
* HTTP Status Codes
* JSON Validation
* Failure Screenshots
* HTML Reporting
* Git
* GitHub
* CI/CD
* GitHub Actions

---

## 🔮 Future Enhancements

Planned improvements include:

* [ ] SQL database validation
* [ ] UI + API integration testing
* [ ] API authentication testing
* [ ] More negative test scenarios
* [ ] Advanced test data management
* [ ] Parallel test execution
* [ ] Cross-browser testing
* [ ] TypeScript + Playwright version
* [ ] Performance testing
* [ ] Docker integration
* [ ] Advanced CI/CD pipeline

---

## 👨‍💻 Author

**Rahul N N**

BE - Artificial Intelligence & Machine Learning

### Skills

```text
Python
Playwright
Pytest
BDD
API Testing
SQL
Git
GitHub
GitHub Actions
Test Automation
```

### GitHub

```text
https://github.com/nnrahuln
```

### Project Repository

```text
https://github.com/nnrahuln/E-Commerce-Automation
```

---

## 📌 Project Highlights

> End-to-end E-Commerce Automation Framework using Python and Playwright with Page Object Model, Pytest, BDD, API Testing, HTML Reporting, Failure Screenshots, and GitHub Actions CI/CD.

---

⭐ If you find this project useful, feel free to explore the repository and test automation framework.
