Feature: Log into the application as a Authorized user

Scenario: User should able to login with valid username and password
  Given Launch the browser
  When User enter the username
  And User enter the password
  And click login button
  Then user verify the welcome link
