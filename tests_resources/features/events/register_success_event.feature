# Created by rupalpatel at 15/05/2023
@user_register_loyalty @events
Feature: Verify event for register loyalty card
  As a DM Administrator
  I want to see an event logged when a user register into a scheme
  so that this Business Event can be written to ClickHouse for validation

  @user_register_event  @event
  Scenario Outline: Verify event is generated when a user registers into a scheme
    Given I am a Lloyds user
    When I perform POST request add and register for <merchant>
    Then I verify lc_register_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "add_and_register" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_register_success loyalty scheme event is created for lloyds_user
    Then verify consent in lc_register_success for lloyds_user for <merchant>

    Examples:
      | merchant   |
      | The_Works    |


  @put_register_event@event
  Scenario Outline: Verify event is generated when on put register
    Given I am a Lloyds user
    When I perform POST request to add <merchant> membership card before registration_success register
    And I perform PUT request to register <merchant> with registration_success membership card
    Then I verify lc_register_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "register_field" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_register_success loyalty scheme event is created for lloyds_user
    Then verify consent in lc_register_success for lloyds_user for <merchant>

    Examples:
      | merchant   |
      | The_Works    |
