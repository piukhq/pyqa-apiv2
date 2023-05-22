# Created by njames on 22/03/2023
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want check all Loyalty card features
  so that I am able to benefit from the Bink functionality

  @retail @join1
  Scenario Outline: Join to a Loyalty Scheme
    Given I am a Lloyds user
    When I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    When I perform GET Wallet
#    Then Verify Wallet fields for <merchant> with join_success
    Then verify that for Lloyds data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant  | status_code_returned |journey_type|
      | The_Works | 202                  |join        |
