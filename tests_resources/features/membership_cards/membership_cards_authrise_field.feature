## Created by rupalpatel at 29/09/2021
#@membership_card_add
#Feature: Authorise a loyalty card
#  As a Bink user
#  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
#  so that I am able to benefit from the Bink functionality
#
#  @authorise_field @bink_regression_api2
#  Scenario Outline: Authorise field journey only
##    Given I am a Bink user
#    When I perform POST request to add "<merchant>" membership card
#    Then I see a <status_code_returned>
#    When I perform POST request to authorise "<merchant>" above wallet only membership card
#    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
#    And I perform DELETE request to delete the "<merchant>" membership card
#    Examples:
#      | merchant | journey_type    | status_code_returned |
#      | Iceland  | authorise_field | 202                  |
#      | Wasabi   | authorise_field | 202                  |
#
##  @add_existing_field @bink_regression_api2
##  Scenario Outline: Add existing card again into wallet
###    Given I am a Bink user
##    When I perform POST request to add "<merchant>" membership card
##    And I perform POST request again to verify the "<merchant>" membership card is already added with "<status_code>"
###    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
##    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
###    And I perform DELETE request to delete the "<merchant>" membership card
##    Examples:
##      | merchant | journey_type | status_code |
##      | Iceland  | Add_field    | 200         |
##      | Wasabi   | Add_field    | 200         |
#
#  @invalid_field_bad_request @bink_regression_api2
#  Scenario Outline: Authorise field journey with Bad request
##    Given I am a Bink user
#    When I perform POST request to authorise "<merchant>" membership card with "<request_payload>" with "<status_code>"
##    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
#    Then I see a "<error_message>" error message
#    And I see a "<error_slug>" error slug
##    And I perform DELETE request to delete the "<merchant>" membership card
#    Examples:
#      | merchant | error_message | error_slug        | request_payload | status_code |
#      | Iceland  | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
#      | Wasabi   | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
#
#  @invalid_field @bink_regression_api2
#  Scenario Outline: Authorise field journey with Unprocessable entity
##    Given I am a Bink user
#    When I perform POST request to authorise "<merchant>" membership card with "<request_payload>" with "<status_code>"
##    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
#    Then I see a "<error_message>" error message
#    And I see a "<error_slug>" error slug
#
##    And I perform DELETE request to delete the "<merchant>" membership card
#    Examples:
#      | merchant | error_message             | error_slug             | request_payload | status_code |
#      | Iceland  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
#      | Wasabi   | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
#
#  @sending_invalid_token @bink_regression_api2
#  Scenario Outline: Sending invalid token with bearer prefix in header for authorise journey (Unauthorized)
##    Given I am a Bink user
#    When I perform POST <merchant> membership_card request with invalid token and bearer prefix for authorise membership card
#    Then I see a <status_code_returned>
#    And I see a "<error_message>" error message
#    And I see a "<error_slug>" error slug
#
#    Examples:
#      | merchant | status_code_returned | error_message             | error_slug    |
#      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |
#      | Wasabi   | 401                  | Supplied token is invalid | INVALID_TOKEN |