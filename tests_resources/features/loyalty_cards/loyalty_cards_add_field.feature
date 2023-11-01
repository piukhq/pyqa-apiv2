# Created by rupalpatel at 20/09/2021
@membership_card_add @membership_cards @njames
Feature: Add a loyalty card
  As a Bink user
  I want to store a loyalty card in my wallet
  so that I can display the barcode in-store, and (if applicable) authorise the loyalty card at a later stage

  @add_field @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add field journey only
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    Then I see a <status_code_returned>
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type | status_code_returned |
      | Viator | Add_field    | 201                  |

  @invalid_field @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add field journey with Unprocessable entity
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message             | error_slug             | request_payload | status_code |
      | SquareMeal  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @sending_invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for add journey (Unauthorized)
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST <merchant> membership_card request with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message             | error_slug    |
      | Viator | 401                  | Supplied token is invalid | INVALID_TOKEN |
