# Created by bularaghavan on 07/12/2021
@bink_regression_api2 @membership_plans
Feature: View Loyalty Plans Overview
 As an API v2.0 consuming channel,
 I want to see an overview of the loyalty plans available
 so that I can display this on the front end without having to call the larger GET /loyalty_plans endpoint

  @loyalty_plans_overview_success @sandbox_regression
  Scenario Outline: View loyalty plans overview
    Given I am a Lloyds user
    When I perform GET request to view loyalty plans overview
    Then I verify the <status_code> for loyalty plan

    Examples:
    | status_code |
    | 200         |

  Scenario Outline: Verify is_in_wallet field loyalty plans overview
    Given I am a Lloyds user
    When I perform GET request to view loyalty plans overview and verify is_in_wallet field
    Then I verify the <status_code> for loyalty plan

    Examples:
    | status_code |
    | 200         |
