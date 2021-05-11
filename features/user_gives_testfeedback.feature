Feature: User can give test feedback

  Scenario:
    Given The user is logged in
    When The User fills out the feedback form
    And The User clicks submit feedback button
    Then The User views feedback successfully sent page