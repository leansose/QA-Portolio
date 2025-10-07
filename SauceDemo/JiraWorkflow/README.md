# 🧭 Jira Workflow

This folder contains screenshots and examples of how the **SauceDemo QA Project** is documented, tracked, and executed inside a real **Agile environment (Jira)**.  
It mirrors the same **test scenarios and test cases** previously documented in Excel, now integrated into an agile board workflow.

---

## 🧩 Project Structure in Jira

| **Level** | **Jira Issue Type** | **Purpose** | **Example** |
|------------|---------------------|--------------|--------------|
| **EPIC** | Epic | Groups related user stories into larger product features | `EPIC: LOGIN` |
| **Test Scenario** | User Story | Describes a functional flow or user behavior (written in BDD format) | `User logs in with valid credentials` |
| **Test Case** | Sub-task | Represents a specific test derived from a scenario; includes steps, expected results, and test status | `TC001 – Login with valid username and password` |
| **Bug / Defect** | Bug | Logged when a test case fails; linked to the corresponding user story | `BUG-001 – About button redirects outside the app` |

---

## ⚙️ Sub-task (Test Case) Fields

Each **Sub-task (Test Case)** includes a custom field called **“Test Result”** to record the execution outcome.  
This field helps distinguish between progress (*Done*) and result (*Passed/Failed/Blocked/Skipped*).

Each test case is documented with the following attributes inside Jira:

| **Field** | **Description** |
|------------|----------------|
| **Preconditions** | System setup or data required before executing the test |
| **Test Steps** | Detailed user actions to perform |
| **Expected Result** | System behavior if test passes |
| **Test Result** | Custom field (Passed, Failed, Blocked, Skipped) |
| **Priority** | Jira built-in field (High, Medium, Low) |


| **Test Result** | |
|------------------|-------------|
| ✅ **Passed** | Expected behavior confirmed |
| ❌ **Failed** | Behavior did not meet expectations (a Bug is created) |
| ⚠️ **Blocked** | Test could not be executed due to dependency or defect |
| ⏭️ **Skipped** | Test intentionally skipped or out of scope for this sprint |

---

## 🧠 User Stories in BDD (Gherkin) Format

All user stories are written in **Behavior-Driven Development (BDD)** style for clarity and consistency.

**Example:**<br />

_Feature: Logout_<br />
Scenario: User logs out from the menu;<br />
As a user, I want to log out from the application so that I can securely end my session._

_Acceptance Criteria:_<br />
>_**Given** the user is on the menu page.<br />
>**When** the user clicks the "Logout" button.<br />
>**Then** the user should be redirected to the login page.<br />
>**And** the user session should be ended._<br />

---

### 📊 Sprint Planning
- Estimation via storie points **Planning Poker (Fibonacci 1, 2, 3, 5, 8, 13)**
- Prioritize and move to sprint backlog

---

## 🧱 Jira Board Columns (Workflow Status)

| **Status** | |
|-------------|-------------|
| 🟦 **TO DO** | Item is planned for this sprint but not yet started |
| 🟧 **IN PROGRESS** | Test scenario or case is currently being executed |
| 🟩 **DONE** | Work or test case has been completed and result logged |

---
