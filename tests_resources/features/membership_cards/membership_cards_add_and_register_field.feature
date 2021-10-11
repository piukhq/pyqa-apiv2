# Created by rupalpatel at 06/10/2021
@membership_card_add_and_register @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to register a ghost loyalty card with the loyalty plan
  so that I can use the Bink functionality with the loyalty card

  @add_and_register_field
  Scenario Outline: Add and register field journey
    Given I am a Bink user
    When I perform POST request to add and register "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I perform DELETE request to delete the "<merchant>" membership card
    Examples:
      | merchant | status_code_returned | journey_type     |
      | Iceland  | 202                  | add_and_register |


  @reregister_already_registered_scheme
  Scenario Outline: Reregister the scheme which is already add and registered
    Given I am a Bink user
    When I perform POST request to add and register "<merchant>" membership card
    And I wait to get scheme active
    And I perform POST again the above request to add and register "<merchant>" membership card
    Then I see a <status_code_returned>
#    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant | status_code_returned | error_message              | error_slug         |
      | Iceland  | 409                  | Card is already registered | ALREADY_REGISTERED |

#  @add_and_auth_existing_field @bink_regression_api2
#  Scenario Outline: Add existing card again into wallet for add and authorise
##    Given I am a Bink user
#    When I perform POST request to add and authorise "<merchant>" membership card
#    And I perform POST request again with add and authorise to verify the "<merchant>" membership card is already added with "<status_code_returned>"
#    Then I see a <status_code_returned>
#    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
#    And I perform DELETE request to delete the "<merchant>" membership card
#    Examples:
#      | merchant | status_code_returned | journey_type      |
#      | Iceland  | 200                  | add_and_authorise |
#      | Wasabi   | 200                  | add_and_authorise |
#
  @invalid_field_bad_request_add_register
  Scenario Outline: Add field journey with Bad request for add and register
    Given I am a Bink user
    When I perform POST request to add and register "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    Examples:
      | merchant | error_message             | error_slug             | request_payload | status_code |
      | Iceland  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @invalid_field_add_register
  Scenario Outline: Add and register field journey with Unprocessable entity
    Given I am a Bink user
    When I perform POST request to add and register "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message | error_slug        | request_payload | status_code |
      | Iceland  | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @sending_invalid_token_add_register
  Scenario Outline: Sending invalid token with bearer prefix in header for add and register journey (Unauthorized)
    Given I am a Bink user
#    When I perform POST <merchant> membership_card request for add and auth with invalid token and bearer prefix
    When I perform POST <merchant> membership_card request for add and register with invalid token and bearer prefix

    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message             | error_slug    |
      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @add_already_then_add_register
  Scenario Outline: Loyalty scheme already exist with add and register credential
    Given I am a Bink user
    When I perform POST request to add registered "<merchant>" membership card
    And I perform POST request to add and register "<merchant>" membership card which already exist with add credentail
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant | status_code_returned | error_message                                                                                | error_slug    |
      | Iceland  | 409                  | Card already added. Use PUT /loyalty_cards/{loyalty_card_id}/register to register this card. | ALREADY_ADDED |
