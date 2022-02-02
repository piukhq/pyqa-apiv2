# Created by bularaghavan on 07/12/2021
@loyalty_plan_overview @membership_plans
Feature: View Loyalty Plans Overview
 As an API v2.0 consuming channel,
 I want to see an overview of the loyalty plans available
 so that I can display this on the front end without having to call the larger GET /loyalty_plans endpoint

  @loyalty_plans_overview_success @bink_regression_api2
  Scenario Outline: View loyalty plans overview
    Given I am a Bink user
    When I perform GET request to view loyalty plans overview
    Then I verify the <status_code> for loyalty plan

    Examples:
    | status_code |
    | 200         |

  @loyalty_overview_is_in_wallet @bink_regression_api2
  Scenario Outline: Verify is_in_wallet field loyalty plans overview
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    When I perform GET request to view loyalty plans overview and verify is_in_wallet field
    Then I verify the <status_code> for loyalty plan

    Examples:
    | status_code |
    | 200         |

  @loyalty_plans_overview_invalid_token @invalid_token @bink_regression_api2
  Scenario Outline: Verify request does not have a valid token
    Given I am a Bink user
    When I perform GET request to view loyalty plans overview with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | status_code | error_message             | error_slug    |
      | 401         | Supplied token is invalid | INVALID_TOKEN |
