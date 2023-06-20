# Created by njames on 11/05/2023
 @register @the_works @bink_regression_api2
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want check all Loyalty card features
  so that I am able to benefit from the Bink functionality


  Scenario Outline: Register to a Loyalty Scheme (Ghost Card)
    Given I am a bos user
    When I perform POST request add and register for <merchant>
    Then I see a <status_code_returned>
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant  | status_code_returned | journey_type     |
      | The_Works | 202                  | add_and_register |


  Scenario Outline: PUT Register to a Loyalty Scheme (Ghost Card)
    Given I am a bos user
    When I perform POST request to add <merchant> membership card before registration_success register
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant  | status_code_returned |journey_type            |
      | The_Works | 202                  |add_and_register        |


  Scenario Outline: Register to a Loyalty Scheme (Ghost Card) - Error Handling
    Given I am a bos user
    When I perform POST request to add and register <merchant> <journey_type>
    Then I see a <status_code_returned>
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant  | status_code_returned | journey_type                                              |
      | The_Works | 200                  | account_already_exists                                    |
      | The_Works | 200                  | card_already_registered                                   |
      | The_Works | 200                  | ghost_card_registration_failed_non_retryable_http_error   |
      | The_Works | 200                  | ghost_card_registration_failed_non_retryable_other_errors |
