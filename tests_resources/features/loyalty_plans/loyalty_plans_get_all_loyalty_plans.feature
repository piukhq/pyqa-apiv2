@loyalty_plans_all @loyalty_plans
Feature: View Loyalty Plans
 As a consuming channel
 I want view all available loyalty plans for my channel
 so that I can display this to users on the front end

  @all_loyalty_plans_success @journey_type @bink_regression_api2 @sandbox_regression
  Scenario Outline: View all available Loyalty Plans
    Given I am a Lloyds user
    When I perform GET request to view all available loyalty plans
    Then I verify the <status_code> for loyalty plan

    Examples:
    | status_code |
    | 200         |

#    Below Plan work for lloyds channel
#    Command to run : pytest -m "all_lloyds_plans_success" --channel lloyds --env staging
  @all_lloyds_plans_success
#  Scenario Outline: View all available Lloyds Loyalty Plans
 #   Given I am a Lloyds user
#    When I perform GET request to view all available loyalty bank plans
#    Then I verify the <status_code> for loyalty plan
#    And I verify all plans appeared correctly

#    Examples:
#    | status_code |
#    | 200         |

  @all_loyalty_plans_invalid_token @invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify request does not have a valid token
    Given I am a Lloyds user
    When I perform GET request to view all available loyalty plans with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | status_code | error_message             | error_slug    |
      | 401         | Supplied token is invalid | INVALID_TOKEN |
