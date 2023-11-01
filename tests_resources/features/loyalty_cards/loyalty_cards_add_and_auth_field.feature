# Created by rupalpatel at 23/09/2021
@loyalty_card_add_and_authorise @membership_cards
Feature: Add and authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @add_and_auth_field @bink_regression_api2 @sandbox_regression @chk
  Scenario Outline: Add and authorise field journey
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 202                  | add_and_authorise |

  @sending_invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for add and authoirse journey (Unauthorized)
    Given I am a Lloyds user
    When I perform POST <merchant> membership_card request for add_and_auth with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant     | status_code_returned | error_message             | error_slug    |
      | SquareMeal   | 401                  | Supplied token is invalid | INVALID_TOKEN |
