Feature: HomePage


  Scenario: Submit form To register for Protractor tutorial.
   # Given User navigate to the register page
    Given user enter the "name"
    When enter the "email"
    And enter the "Password"
    And select the checkbox
    And Select the "gender_type"
    And Select the Employment_status
    And enter the "date_of_birth"
    And click on Submit button
    Then verify the "success_message" displayed on screen
