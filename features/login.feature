Feature: Users of different roles can log in

  Scenario Outline: As a user of a role i can log in
    Given The user is on the login screen
    When The user enters <username> in the username input
    And The user enters <password> in the password input
    And The user hits the submit button
    Then The user is redirected the main page

    Examples:
