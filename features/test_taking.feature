Feature: The User takes the test

    Scenario: The User navigates to the test
        Given The User is on the login page
        When  The user put in the username
        And The user put in the password
        When The User clicks on login button
        Then The User is viewing the test

#    Scenario: The User takes the test
#        Given The User is viewing the test
#        When The User answers the questions
#        And The User clicks on the submit button
#        Then The User views their score


