Feature: The User Views The Test's Grade

    Scenario: The User navigates to the tests
        Given The User is logged in
        When The User clicks on view tests
        Then The User views the list of test

    Scenario: The User selects a test to view grade
        Given The User is viewing the tests
        When The User selects a test
        Then The User views the grade on the test