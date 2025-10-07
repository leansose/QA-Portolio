## Jira Workflow
This folder contains screenshots, examples of the same test cases documented and tracked inside a real agile platform (Jira)

  - Features listed by EPICS
  - Test Scenarios are listed as USER STORIES
  - Test Cases are listed as SUB-TASKs

*USER STORIES*
BDD, Gherkin format
    
Exemple:
Scenario outline: User logs out from the menu
As a user, I want to log out from the application so that I can securely end my session

Acceptance criteria:
Given the user is on the menu page
When the user clicks the "Logout" button
Then the user should be redirected to the login page
And the user session should be ended

*SUB-TASKs*
Status (Jira intern), Preconditions, Test Steps, Expected Result, Test Results (created field for test case status), Priority (Jira intern)
Test Results -> Passed, Failed, Blocked, Skipped
Priority set to High, Medium, Low
  


