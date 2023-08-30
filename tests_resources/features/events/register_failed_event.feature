# Created by rupalpatel at 15/05/2023
@user_register_failed_loyalty @events
Feature: Verify event for register failed loyalty card
  As a DM Administrator
  I want to see an event logged when a user register into a scheme
  so that this Business Event can be written to ClickHouse for validation

  @user_register_failed_event @bink_regression_api2 @event
  Scenario Outline: Verify event is generated when register fails
    Given I am a Lloyds user
    When I perform POST request to result "failed" add and register for <merchant>
    Then I verify lc_register_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "add_and_register" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_register_failed loyalty scheme event is created for lloyds_user

    Examples:
      | merchant   |
      | Iceland    |


  @put_register_failed_event @bink_regression_api2 @event
  Scenario Outline: Verify event is generated on put register failed
    Given I am a Lloyds user
    When I perform POST request to add <merchant> membership card before registration_failed register
    And I perform PUT request to register <merchant> with registration_failed membership card
    Then I verify lc_register_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "register_field" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_register_failed loyalty scheme event is created for lloyds_user

    Examples:
      | merchant   |
      | Iceland    |


  @multi_wallet_register_event @bink_regression_api2 @event
  Scenario Outline: Verify event is generated for multiple-wallet register
    Given I am a Lloyds user
    When I perform POST request to result "failed" add and register for <merchant>
    Then I verify lc_register_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "add_and_register" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_register_failed loyalty scheme event is created for lloyds_user
    Given I am a bos user
    When I perform POST request to result "failed" add and register for <merchant>
    Then I verify lc_register_request loyalty scheme event is created for bos_user
    And verify that for bos_user data stored in after "add_and_register" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for bos_user
    And I verify lc_register_failed loyalty scheme event is created for bos_user

    Examples:
      | merchant   |
      | Iceland    |



  @put_register_event @bink_regression_api2 @event
  Scenario Outline: Verify event is generated when on put register in multi-wallet
    Given I am a Lloyds user
    When I perform POST request to add <merchant> membership card before registration_failed register
    And I perform PUT request to register <merchant> with registration_failed membership card
    Then I verify lc_register_request loyalty scheme event is created for lloyds_user
    And verify that for lloyds_user data stored in after "register_field" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for lloyds_user
    And I verify lc_register_failed loyalty scheme event is created for lloyds_user
    Given I am a bos user
    When I perform POST request to add <merchant> membership card before registration_failed register
    And I perform PUT request to register <merchant> with registration_failed membership card
    Then I verify lc_register_request loyalty scheme event is created for bos_user
    And verify that for bos_user data stored in after "register_field" journey for "<merchant>"
    And I verify lc_status_change loyalty scheme event is created for bos_user
    And I verify lc_register_failed loyalty scheme event is created for bos_user

    Examples:
      | merchant   |
      | Iceland    |