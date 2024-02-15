# Created by srikalyanikotha at 20/06/2023
@the_works_add
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want add a loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @add_auth_journey @bink_regression_api2
  Scenario Outline: Works Add Journey
    Given I am a bos user
    When I add membership card with transactions and vouchers for "<merchant>"
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant  | status_code_returned | journey_type      |
      | The_Works | 202                  | add_and_authorise |
#      | itsu      | 202                  | add_and_authorise



  Scenario Outline: Get Loyalty card vouchers
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    When I add membership card with transactions and vouchers for "<merchant>"
    And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | itsu        | 200                  |
