# Created by bularaghavan at 05/10/2021
@membership_card_register @membership_cards
Feature: Register a loyalty card
  As a Bink user
  I want to add registration credentials to an existing Store card,
  so that I can register the loyalty card with the merchant and enable the Bink functionality on the loyalty card

  @register_field @bink_regression_api2
  Scenario Outline: Register field journey only
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | status_code_returned | journey_type   |
      | Iceland  | 202                  | register_field |

  @register_existing_field @bink_regression_api2
  Scenario Outline: Register a card that is already registered into Wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a 202
    When I perform PUT request to register "<merchant>" above wallet only membership card again
    Then I see a  <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
 #  Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | status_code_returned | error_message                                                                                                                                                 | error_slug         |
      | Iceland  | 409                  | Card is already registered. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to authorise this card in your wallet, or to update authorisation credentials. | ALREADY_REGISTERED |

  @invalid_json_register @bink_regression_api2
  Scenario Outline: Register field journey with Bad request
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add <merchant> membership card before registration_success register
    And I perform PUT request to register "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message | error_slug        | request_payload | status_code |
      | Iceland  | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @invalid_request_register @bink_regression_api2
  Scenario Outline: Register field journey with Unprocessable entity
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add <merchant> membership card before registration_success register
    And I perform PUT request to register "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message             | error_slug             | request_payload | status_code |
      | Iceland  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |


  @register_invalid_token @bink_regression_api2
  Scenario Outline: Sending invalid token with bearer prefix in header for register journey (Unauthorized)
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add <merchant> membership card before registration_success register
    And I perform PUT request to register "<merchant>" membership card with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message             | error_slug    |
      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @reg_pll @bink_regression_api2
  Scenario Outline: verify PLL for update register
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    And I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant | status_code_returned | journey_type |
      | master                | Iceland  | 202                  | pll_active   |


  @put_register_multi_wallet @bink_regression_api2 @trusted
  Scenario Outline: Add existing card again into different wallet via put register
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add "<merchant>" membership card already registered
    Then I see a 200
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    When For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success


    Examples:
      | merchant | status_code_returned |
      | Iceland  | 202                  |


  @put_register_failed_multi_wallet @bink_regression_api2 @trusted
  Scenario Outline: Wallet1 add then register failed, wallet2 add then register same card with correct details
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before <scheme_state> register
    Then I see a 201
    When I perform PUT request to register <merchant> with <scheme_state> membership card
    Then I see a 202
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 200
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a 202
    When For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_failed


    Examples:
      | merchant | scheme_state      |
      | Iceland  |registration_failed|


  @put_register_failed_multi_wallet @bink_regression_api2 @trusted
  Scenario Outline: Wallet1 add then register valid, wallet2 add then register same card with invalid details
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a 202
    Given I am a halifax user
    When I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before <scheme_state> register
    Then I see a 200
    When I perform PUT request to register <merchant> with <scheme_state> membership card
    Then I see a 202
    When For halifax_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_failed
    Given I am a Lloyds user
    When For lloyds_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success


    Examples:
      | merchant | scheme_state      |
      | Iceland  |registration_failed|