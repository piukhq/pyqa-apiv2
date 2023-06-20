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


  @retail_join_failed
  Scenario Outline: retailer fails to join requests
    Given I am a bos user
    When I perform POST request to <journey_type> "<merchant>" membership card
    Then I see a <status_code_returned>
    When I perform GET Wallet
#    Then Verify Wallet fields for <merchant> with account_already_exists
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"


    Examples:
      | merchant      | status_code_returned |journey_type          |
      | The_Works         | 202              |account_already_exists|
      | The_Works         | 202              |join_failed           |
      | The_Works         | 202              |join_http_failed      |
