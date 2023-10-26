# Created by rupalpatel at 07/06/2023
@auth_success_event @events
Feature: Verify event for add and after authorise loyalty card
  As a DM Administrator
  I want to see an event logged when a user send request to add then put with authorise data to scheme
  so that this Business Event can be written to ClickHouse for validation

  @auth_success_event @bink_regression_api2 @event
  Scenario: Verify events for add and after authorise field journey only
    Given I am a Lloyds user
    When I perform POST request to add "Iceland" membership card
    And I perform PUT request to authorise "Iceland" above wallet only membership card
    Then I verify lc_auth_request loyalty scheme event is created for lloyds_user
    And I verify lc_auth_success loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "authorise_field" journey for "Iceland"

  @multi_wallet_auth_event @bink_regression_api2 @event
  Scenario: Verify event generate for add and after authorise requests in multiwallet
    Given I am a Lloyds user
    When I perform POST request to add "Iceland" membership card
    And I perform PUT request to authorise "Iceland" above wallet only membership card
    Then verify that for lloyds_user data stored in after "add_and_authorise" journey for "Iceland"
    And I verify lc_auth_request loyalty scheme event is created for lloyds_user
    And I verify lc_auth_success loyalty scheme event is created for lloyds_user

    Given I am a halifax user
    When I perform POST request to add "Iceland" membership card
    And I perform PUT request to authorise "Iceland" above wallet only membership card
    Then verify that for halifax_user data stored in after "add_and_authorise" journey for "Iceland"
    And I verify lc_auth_request loyalty scheme event is created for halifax_user
    And I verify lc_auth_success loyalty scheme event is created for halifax_user
