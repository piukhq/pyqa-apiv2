# Created by rupalpatel at 06/10/2021
@membership_card_add_and_register @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to register a ghost loyalty card with the loyalty plan
  so that I can use the Bink functionality with the loyalty card

  @add_and_register_field @bink_regression_api2
  Scenario Outline: Add and register field journey
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request add and register for <merchant>
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | status_code_returned | journey_type     |
      | Iceland  | 202                  | add_and_register |

#  @scheme_is_pending_add_and_auth @bink_regression_api2
#  Scenario Outline: Add and register field journey where scheme is in pending
#    Given I am a Bink user
#    When I perform POST request <type> add and register for <merchant>
#    And I update the membership card to "<status>" pending in DB
#    And I perform POST request to add and register "<merchant>" membership card where membership card is in pending
#    Then I see a <status_code_returned>
#    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
#    When I update the membership card to "<status_changed>" pending in DB
#    And I perform DELETE request to delete the "<merchant>" membership card
#    Examples:
#      | merchant | status_code_returned | journey_type     | status |
#      | Iceland  | 200                  | add_and_register | 0      |

  @add_and_register_existing_field @bink_regression_api2
  Scenario Outline: Add existing card again into wallet for add and register
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When I perform POST request add_and_register again for <merchant>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | status_code_returned | journey_type     | error_message                                                                                          | error_slug         |
      | Iceland  | 409                  | add_and_register | Card is already registered. Use POST /loyalty_cards/add_and_authorise to add this card to your wallet. | ALREADY_REGISTERED |

  @invalid_field_bad_request_add_register @bink_regression_api2
  Scenario Outline: Add field journey with Bad request for add and register
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and register "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message             | error_slug             | request_payload | status_code |
      | Iceland  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @invalid_field_add_register @bink_regression_api2
  Scenario Outline: Add and register field journey with Unprocessable entity
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and register "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message | error_slug        | request_payload | status_code |
      | Iceland  | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @sending_invalid_token_add_and_register @bink_regression_api2
  Scenario Outline: Sending invalid token with bearer prefix in header for add and register journey (Unauthorized)
    Given I am a Bink user
    When I perform POST <merchant> membership_card request for add and register with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message             | error_slug    |
      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |


  @add_and_register_success_multi_wallet @bink_regression_api2 @trusted @testnp1402
  Scenario Outline: add and register success in wallet1 then add and register success in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request add_and_register again for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success


    Examples:
      | merchant |
      | Iceland  |

  @register_failed_card_multi_wallet @bink_regression_api2 @trusted @testnp1402
  Scenario Outline: add and register failed in wallet1 then add and register success in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to result failed add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request add_and_register again for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>

    Examples:
      | merchant |  scheme_state      |
      | Iceland  | registration_failed|


  @register_success_failed_multi_wallet @bink_regression_api2 @trusted @testnp1402
  Scenario Outline: add and register success in wallet1 then add and register failed in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to result failed add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success

    Examples:
      | merchant |  scheme_state      |
      | Iceland  | registration_failed|


  @register_failed_failed_multi_wallet @bink_regression_api2 @trusted @testnp1402
  Scenario Outline: add and register failed in wallet1 then add and register failed in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to result failed add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to result failed add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>

    Examples:
      | merchant |  scheme_state      |
      | Iceland  | registration_failed|