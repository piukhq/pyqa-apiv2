# Created by bularagahavan 26/09/2022
 @membership_cards
Feature: Authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @bink_regression_api2 @sit

  Scenario Outline: PUT with valid cred in wallet 1 and invalid cred in wallet 2
    Given I am a bos user
    When I add membership card with transactions and vouchers for "<merchant>"
    Then I see a 201
    When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
    Then I see a 202
    And verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Given I am a halifax user
    When I add membership card with transactions and vouchers for "<merchant>"
    Then I see a 200
    When I perform PUT request to authorise "<merchant>" membership card with "unauthorised" with "202"
    Then I see a 202
    And verify that for halifax_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant  |journey_type    |
      | Viator    |authorise_field |
