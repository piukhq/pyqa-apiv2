# Created by rupalpatel at 15/05/2023
@user_join_loyalty @events
Feature: Verify event for join loyalty card
  As a DM Administrator
  I want to see an event logged when a user joined scheme
  so that this Business Event can be written to ClickHouse for validation

  @user_join_event @bink_regression_api2 @event @test123
  Scenario Outline: Verify event generate for user join scheme
    Given I am a Lloyds user
    When I perform POST request to join "<merchant>" membership card
    Then I verify lc_join_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "join" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_join_success loyalty scheme event is created for lloyds_user
    Then verify consent in lc_join_success for lloyds_user for <merchant>

    Examples:
      | merchant      |
      | The_Works     |

  @multi_wallet_joins_event @bink_regression_api2 @event
  Scenario: Verify event generate for join requests in multiwallet
    Given I am a Lloyds user
    When I perform POST request to join "The_Works" membership card
    Then I verify lc_join_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "join" journey for "The_Works"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_join_success loyalty scheme event is created for lloyds_user
    Then verify consent in lc_join_success for lloyds_user for The_Works

    Given I am a halifax user
    When I perform POST request to join "The_Works" membership card
    Then I verify lc_join_request loyalty scheme event is created for halifax_user
    And verify that for halifax_user data stored in after "join" journey for "The_Works"
    And I verify lc_status_change loyalty scheme event is created for halifax_user
    And I verify lc_join_success loyalty scheme event is created for halifax_user
    Then verify consent in lc_join_success for halifax_user for The_Works
