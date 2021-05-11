Feature: An admin can add different users

  Scenario:
    Given The admin is logged in
    And the Admin is on the Add User page
    When the admin fills out the user information
    And the admin hits submit
    Then The admin views success page