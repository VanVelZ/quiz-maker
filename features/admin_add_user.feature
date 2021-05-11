Feature: An admin can place students and teachers into courses

  Scenario The admin can place a student into course:
    Given The admin is logged in
    And the Admin is on the students page
    When the admin selects a course for the user
    Then The user is assigned to the course

  Scenario The admin can assign a Teacher a course:
    Given The admin is logged in
    And the Admin is on the teachers page
    When the admin selects a course for the user
    Then The user is assigned to the course