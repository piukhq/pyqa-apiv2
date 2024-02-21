# Created by rupalpatel at 06/06/2023
@add_auth_success_event @events @bink_regression_api2
Feature: Verify event for add and authorise loyalty card
  As a DM Administrator
  I want to see an event logged when a user send request to add and authorise scheme
  so that this Business Event can be written to ClickHouse for validation

  Scenario: Verify events for add and authorise field journey
    Given I am a Lloyds user
    When I add and authorise "Viator" membership card
    Then verify that for lloyds_user data stored in after "add_and_authorise" journey for "Viator"
    And I verify lc_add_auth_request loyalty scheme event is created for lloyds_user
    And I verify lc_add_auth_success loyalty scheme event is created for lloyds_user
