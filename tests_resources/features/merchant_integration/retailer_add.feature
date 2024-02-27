# Created by srikalyanikotha at 20/06/2023
 @bink_regression_api2
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want add a loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  Scenario Outline: Works Add Journey
    Given I am a bos user
    When I add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant  | status_code_returned | journey_type      |
      | The_Works | 202                  | add_and_authorise |
