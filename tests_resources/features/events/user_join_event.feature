# Created by rpatel on 12/05/2023
@user_join_loyalty @events
Feature: Verify event for join loyalty card
  As a DM Administrator
  I want to see an event logged when a user joined scheme
  so that this Business Event can be written to ClickHouse for validation

  @user_join_event @bink_regression_api2 @event
  Scenario Outline: Verify event for user join scheme
    Given I am a Lloyds user
    When I perform POST request to join "<merchant>" membership card
    Then I verify that lc_join_request scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "join" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_join_success loyalty scheme event is created for lloyds_user

    Examples:
      | merchant   |
      | Iceland    |
      | Wasabi     |
      | SquareMeal |






