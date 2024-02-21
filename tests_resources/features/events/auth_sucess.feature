# Created by rupalpatel at 07/06/2023
@bink_regression_api2 @event
Feature: Verify event for add and after authorise loyalty card
  As a DM Administrator
  I want to see an event logged when a user send request to add then put with authorise data to scheme
  so that this Business Event can be written to ClickHouse for validation

  Scenario: Verify events for add and PUT authorise journey
    Given I am a Lloyds user
    When I perform POST request to add "Viator" membership card
    And I perform PUT request to authorise "Viator" above wallet only membership card
    Then I verify lc_auth_request loyalty scheme event is created for lloyds_user
    And I verify lc_auth_success loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "authorise_field" journey for "Viator"
