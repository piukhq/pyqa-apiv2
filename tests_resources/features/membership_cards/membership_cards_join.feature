# Created by rupalpatel at 06/10/2021
@membership_card_join @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to join a loyalty scheme
  so that I can use the Bink functionality with the relevant loyalty plan

  @join_scheme @bink_regression_api2
  Scenario Outline: join journey
    Given I am a Bink user
    When I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I perform DELETE request to delete the "<merchant>" membership card
    Examples:
      | merchant      | status_code_returned | journey_type |
      | Iceland       | 202                  | join         |
#      | Wasabi        | 202                  | join         |
#      | HarveyNichols | 202                  | join         |


  @empty_field_join @bink_regression_api2
  Scenario Outline: join journey with Bad request (empty field)
    Given I am a Bink user
    When I perform POST request to join "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant      | error_message             | error_slug             | request_payload | status_code |
      | Iceland       | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
      | Wasabi        | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
      | HarveyNichols | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @invalid_json_join @bink_regression_api2
  Scenario Outline: join journey with Unprocessable entity - bad request
    Given I am a Bink user
    When I perform POST request to join "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant      | error_message | error_slug        | request_payload | status_code |
      | Iceland       | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
      | Wasabi        | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
      | HarveyNichols | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @invalid_token_join @bink_regression_api2
  Scenario Outline: Sending invalid token with bearer prefix in header for join journey (Unauthorized)
    Given I am a Bink user
    When I perform POST request to join "<merchant>" with invalid token
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant      | status_code_returned | error_message             | error_slug    |
      | Iceland       | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi        | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | HarveyNichols | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @pll_join @bink_regression_api2
  Scenario Outline: verify PLL for join journey
    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

    Examples:
      | payment_card_provider | merchant | status_code_returned | journey_type |
      | master                | Iceland  | 202                  | pll          |
