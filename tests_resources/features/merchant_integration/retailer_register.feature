# Created by njames on 11/05/2023
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want check all Loyalty card features
  so that I am able to benefit from the Bink functionality

  @register @chk1
  Scenario Outline: Register to a Loyalty Scheme (Ghost Card)
    Given I am a bos user
    When I perform POST request add and register for <merchant>
    Then I see a <status_code_returned>
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant  | status_code_returned | journey_type     |
      | The_Works | 202                  | add_and_register |


#   @register
#  Scenario Outline: PUT Register to a Loyalty Scheme (Ghost Card)
#    Given I am a bos user
#    When I perform POST request to add <merchant> membership card before registration_success register
#    When I perform PUT request to register <merchant> with registration_success membership card
#    Then I see a <status_code_returned>
#    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"
#
#
#    Examples:
#      | merchant  | status_code_returned |journey_type            |
#      | The_Works | 202                  |add_and_register        |


  @register_field @bink_regression_api2
  Scenario Outline: Register to a Loyalty Scheme (Ghost Card) - Error Handling
    Given I am a bos user
    When I perform POST request to add and register for <merchant> with <invalid_data>
    Then I see a <status_code_returned>
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant  | status_code_returned | journey_type   | invalid_data            |
      | The_Works | 202                  | register_field | account_already_exists  |
      | The_Works | 202                  | register_field | card_already_registered |
      | The_Works | 202                  | register_field | invalid_card_num        |