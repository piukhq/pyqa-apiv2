# Created by bularaghavan at 31/10/2022
@trusted_channel_add_and_authorise
Feature: Add and authorise a loyalty card into Trusted channel
  As a Trusted Channel I want to add a loyalty card into my user’s wallet, without needing to provide sensitive credential information
  so that I do not need to expose sensitive credential data within my system, and
  I can then link my user’s payment cards to their loyalty card, so my users can use PLL.


  @add_and_auth_tc @sandbox_regression
  Scenario Outline: Trusted channel adds loyalty card into wallet
    Given I am a squaremeal user
 #   When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    When For squaremeal_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET transaction for loyalty card with unauthorised for <merchant>
    And For squaremeal_user I perform GET balance for loyalty card with unauthorised for <merchant>
    And For squaremeal_user I perform GET voucher for loyalty card with unauthorised for <merchant>

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 202                  | add_and_authorise |

  @add_and_auth_ntc_in_tc @sandbox_regression
  Scenario Outline: Trusted channel adds loyalty card into wallet which already exists in Non trusted channel

    Given I am a halifax user
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Given I am a squaremeal user
 #   When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    When For squaremeal_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For squaremeal_user I perform GET balance for loyalty card with authorised for <merchant>
    And For squaremeal_user I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 202                  | add_and_authorise |

@add_and_auth_tc_in_ntc @sandbox_regression
  Scenario Outline: Non Trusted channel adds loyalty card into wallet which already exists in Trusted channel

    Given I am a squaremeal user
 #  When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When For lloyds_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET balance for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 202                  | add_and_authorise |

  @add_and_auth_existing_field_tc @sandbox_regression
  Scenario Outline: Add existing card again into wallet for add and authorise
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    And I perform POST request again with add and authorise to verify the "<merchant>" membership card is already added with "<status_code_returned>"
    Then I see a <status_code_returned>
    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 200                  | add_and_authorise |

  @invalid_field_bad_request_add_authorise_tc @sandbox_regression
  Scenario Outline: Add field journey with Bad request for add and authorise
    Given I am a Lloyds user
    When I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | error_message             | error_slug             | request_payload | status_code |
      | SquareMeal  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @invalid_field @sandbox_regression
  Scenario Outline: Add and authorised field journey with Unprocessable entity
    Given I am a Lloyds user
    When I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant     | error_message | error_slug        | request_payload | status_code |
      | SquareMeal   | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @sending_invalid_token_tc @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for add and authoirse journey (Unauthorized)
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant     | status_code_returned | error_message             | error_slug    |
      | SquareMeal   | 401                  | Supplied token is invalid | INVALID_TOKEN |


  @add_already_then_add_auth_tc @sandbox_regression
  Scenario Outline: Loyalty scheme already exist with add credential
    Given I am a Lloyds user
    When I perform POST request to add "<merchant>" membership card
    And I perform POST request to add and authorise "<merchant>" membership card which already exist with add credential
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | status_code_returned | error_message                                                                                  | error_slug    |
      | Iceland     | 409                  | Card already added. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to authorise this card. | ALREADY_ADDED |
      | Wasabi      | 409                  | Card already added. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to authorise this card. | ALREADY_ADDED |
      | Trenette    | 409                  | Card already added. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to authorise this card. | ALREADY_ADDED |


  @add_and_auth_with_different_authorised_field_tc @sandbox_regression
  Scenario Outline: Already Add and authorised scheme then add with different auth credential
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    And I perform POST request to add and authorise "<merchant>" with different auth credential
    Then I see a <status_code_returned>
#    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | status_code_returned | error_message                                                                                                    | error_slug         |
      | Iceland     | 409                  |Card already authorised. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to modify authorisation credentials.  | ALREADY_AUTHORISED |
      | SquareMeal  | 409                  |Card already authorised. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to modify authorisation credentials.  | ALREADY_AUTHORISED |
      | Trenette    | 409                  |Card already authorised. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to modify authorisation credentials.  | ALREADY_AUTHORISED |

  @add_and_auth_pll_tc @sandbox_regression
  Scenario Outline: verify PLL for add and authorise
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant   | status_code_returned | journey_type |
      | master                | Iceland    | 202                  | pll          |
      | master                | Wasabi     | 202                  | pll          |
      | master                | SquareMeal | 202                  | pll          |
      | master                | Trenette   | 202                  | pll          |
