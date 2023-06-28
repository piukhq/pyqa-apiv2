# Created by srikalyanikotha at 20/06/2023
 @twks
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want add a loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @add_auth_journey
  Scenario Outline: Works Add Journey
    Given I am a bos user
    When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | The_Works     | 202                  | add_and_authorise |


    @add_auth_failed_journey
  Scenario Outline: Add_Auth journey with failed Credentials_The Works
    Given I am a bos user
    When I perform POST request to add and auth "<merchant>" membership card with "<invalid_add_fields>" with "202"
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

  Examples:
      | merchant      | status_code_returned| invalid_add_fields    | journey_type|
      | The_Works     | 202                 | invalid_cardnumber | add_and_authorise |
      | The_Works     | 202                 | unknown_cardnumber | add_and_authorise |
