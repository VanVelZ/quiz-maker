Feature: User viewing accumulative grade

    Scenario: User is viewing accumulative grade
        Given The User is logged in
        When The User selects a course
        Then The user sees their cumulative grade
