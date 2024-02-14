@bink_regression_api2
Feature: View Loyalty Plans
 As a consuming channel
 I want view all available loyalty plans for my channel
 so that I can display this to users on the front end

  Scenario Outline: View all available Loyalty Plans
    Given I am a Lloyds user
    When I perform GET request to view all available loyalty plans
    Then I verify the <status_code> for loyalty plan

    Examples:
    | status_code |
    | 200         |


  Scenario Outline: Verify request does not have a valid token
    Given I am a Lloyds user
    When I perform GET request to view all available loyalty plans with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | status_code | error_message             | error_slug    |
      | 401         | Supplied token is invalid | INVALID_TOKEN |
