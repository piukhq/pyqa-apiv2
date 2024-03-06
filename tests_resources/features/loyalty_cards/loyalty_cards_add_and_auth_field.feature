# Created by rupalpatel at 23/09/2021
@loyalty_card_add_and_authorise @membership_cards
Feature: Add and authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @bink_regression_api2 @pyqa-ait
  Scenario Outline: Add and authorise field journey
    Given I am a Lloyds user
    When I add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 202                  | add_and_authorise |
