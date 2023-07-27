# Created by srikalyanikotha at 20/06/2023
@the_works_add
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
      | merchant  | status_code_returned | journey_type      |
      | The_Works | 202                  | add_and_authorise |
      | itsu      | 202                  | add_and_authorise |


  @add_auth_failed_journey
  Scenario Outline: Add_Auth journey with failed Credentials
    Given I am a bos user
    When I perform POST request to add and auth "<merchant>" membership card with "<invalid_add_fields>" with "202"
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant  | status_code_returned | invalid_add_fields | journey_type      |
      | The_Works | 202                  | invalid_cardnumber | add_and_authorise |
      | The_Works | 202                  | unknown_cardnumber | add_and_authorise |
      | itsu      | 202                  | invalid_cardnumber | add_and_authorise |
      | itsu      | 202                  | unknown_cardnumber | add_and_authorise |



  Scenario Outline: Get Loyalty card vouchers
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | itsu        | 200                  |

