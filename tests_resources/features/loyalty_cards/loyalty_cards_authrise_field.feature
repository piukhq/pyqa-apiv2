# Created by rupalpatel at 04/10/2021, updated by BR on 29/07/2022
 @membership_cards
Feature: Authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @sit @bink_regression_api2
  Scenario Outline: Authorise field journey only
    Given I am a bos user
    When I perform POST request to add "<merchant>" membership card
    And I perform PUT request to authorise "<merchant>" above wallet only membership card
    Then I see a <status_code_returned>
    And verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type    | status_code_returned |
      | Viator   | authorise_field  |202                  |

  @authorise_existing_field @bink_regression_api2
  Scenario Outline: Authorise existing card again into wallet
    Given I am a bos user
    When I perform POST request to add "<merchant>" membership card
    And I perform PUT request to authorise "<merchant>" above wallet only membership card
    And I perform PUT request to authorise "<merchant>" above wallet only membership card again
    Then I see a <status_code_returned>
    And verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type    | status_code_returned |
      | Viator   | authorise_field | 200                  |


  @auth_pll @bink_regression_api2
  Scenario Outline: verify PLL for authorise
    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add "<merchant>" membership card
    And I perform PUT request to authorise "<merchant>" above wallet only membership card
    Then I see a <status_code_returned>
    And verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant | status_code_returned | journey_type |
      | master                | Viator  | 202                  | pll_active   |
