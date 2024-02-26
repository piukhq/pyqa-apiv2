# Created by rupalpatel at 08/06/2023
@add_auth_fail_event @events @bink_regression_api2
Feature: Verify event for add and authorise fail loyalty card
  As a DM Administrator
  I want to see an event logged when a user send request with invalid data to add and authorise scheme
  so that this Business Event can be written to ClickHouse for validation

  Scenario: Verify events for add and auth field journey with unauthorised loyalty card
    Given I am a Lloyds user
    Then I verify that user_created event is created for lloyds_user
    When add and auth "Viator" membership card with "unauthorised" with "202"
    Then verify that for lloyds_user data stored in after "unauthorised" journey for "Viator"
    And I verify lc_add_auth_request loyalty scheme event is created for lloyds_user
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_add_auth_failed loyalty scheme event is created for lloyds_user

  Scenario: Verify event generate for fail add and auth requests in multiwallet
    Given I am a Lloyds user
    Then I verify that user_created event is created for lloyds_user
    When add and auth "Viator" membership card with "unauthorised" with "202"
    Then verify that for lloyds_user data stored in after "unauthorised" journey for "Viator"
    And I verify lc_add_auth_request loyalty scheme event is created for lloyds_user
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_add_auth_failed loyalty scheme event is created for lloyds_user

    Given I am a halifax user
    When add and auth "<merchant>" membership card with "unauthorised" with "202"
    Then verify that for halifax_user data stored in after "unauthorised" journey for "Viator"
    And I verify lc_add_auth_request loyalty scheme event is created for halifax_user
    And I verify lc_status_change loyalty scheme event is created for halifax_user
    And I verify lc_add_auth_failed loyalty scheme event is created for halifax_user
