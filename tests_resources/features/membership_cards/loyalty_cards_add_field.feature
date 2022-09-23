# Created by rupalpatel at 20/09/2021
@membership_card_add @membership_cards
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
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type | status_code_returned |
      | Iceland  | Add_field    | 201                  |
      | Wasabi   | Add_field    | 201                  |
      | Trenette | Add_field    | 201                  |

  @add_existing_field @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add existing card again into wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    And I perform POST request again to verify the "<merchant>" membership card is already added with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type | status_code |
      | Iceland  | Add_field    | 200         |
      | Wasabi   | Add_field    | 200         |
      | Trenette | Add_field    | 200         |

  @invalid_field_bad_request @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add field journey with Bad request
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message | error_slug        | request_payload | status_code |
      | Iceland  | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
      | Wasabi   | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
      | Trenette | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

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
      | Iceland  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
      | Wasabi   | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
      | Trenette | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

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
      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi   | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Trenette | 401                  | Supplied token is invalid | INVALID_TOKEN |