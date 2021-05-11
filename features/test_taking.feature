Feature: The User takes the test

    Scenario: The User navigates to the test
        Given The User is logged in
        When The User clicks a test
        Then The User views the test

    Scenario: The User takes the test
        Given The User is viewing the test
        When The User answers the questions
        And The User clicks on the submit button
        Then The User views their score


