Feature: The Teacher Views The Test Scores

    Scenario: The Teacher navigates to the tests
        Given The Teacher is logged in
        When The Teacher clicks on view tests
        Then The Teacher views the list of tests

    Scenario: The Teacher selects a test to view scores
        Given The Teacher is viewing the tests
        When The Teacher selects a specific test
        Then The Teacher views the students scores on the test
