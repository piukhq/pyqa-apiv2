# Created by njames on 22/03/2023
  @the_works_join @bink_regression_api2
Feature: Basic Merchant Integration Journeys
  As a Bank user
  I want check all Loyalty card features
  so that I am able to benefit from the Bink functionality


  Scenario Outline: Join to a Loyalty Scheme
    Given I am a bos user
    When I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then verify that for bos_user data stored in after <journey_type> journey for "<merchant>"

    Examples:
      | merchant  | status_code_returned |journey_type|
      | The_Works | 202                  |join        |
