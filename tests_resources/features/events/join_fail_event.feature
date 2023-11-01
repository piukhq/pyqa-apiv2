# Created by rupalpatel at 01/06/2023
@events
Feature: Verify event for join fail for loyalty card
  As a DM Administrator
  I want to see an event logged when a user joined failed scheme
  so that this Business Event can be written to ClickHouse for validation

  @join_fail_event @bink_regression_api2
  Scenario Outline: Remove a failed join request from the wallet and verify the event
    Given I am a Lloyds user
    When I perform <scheme_state> POST request to join "<merchant>" membership card
    Then I verify lc_join_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_join_failed loyalty scheme event is created for lloyds_user

    Examples:
      | merchant | journey_type | scheme_state |
      | The_Works  | join_failed  | enrol_failed |


  @multi_wallet_joins_fail_event @bink_regression_api2 @join_fail_event
  Scenario Outline: Verify event generate for join fail requests for multiwallet
    Given I am a Lloyds user
    When I perform <scheme_state> POST request to join "<merchant>" membership card
    Then I verify lc_join_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_join_failed loyalty scheme event is created for lloyds_user

    Given I am a halifax user
    When I perform <scheme_state> POST request to join "<merchant>" membership card
    Then I verify lc_join_request loyalty scheme event is created for halifax_user
    And verify that for halifax_user data stored in after "<journey_type>" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for halifax_user
    And I verify lc_join_failed loyalty scheme event is created for halifax_user

    Examples:
      | scheme_state | merchant |journey_type|
      | enrol_failed | The_Works  |join_failed |
