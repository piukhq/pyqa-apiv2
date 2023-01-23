# Created by bularaghavan at 31/10/2022
@trusted_channel_add_and_authorise @trusted @actual_tc @bink_regression_api2
Feature: Add and authorise a loyalty card into Trusted channel
  As a Trusted Channel I want to add a loyalty card into my user’s wallet, without needing to provide sensitive credential information
  so that I do not need to expose sensitive credential data within my system, and
  I can then link my user’s payment cards to their loyalty card, so my users can use PLL.


  @add_and_auth_tc @sandbox_regression
  Scenario Outline: Trusted channel adds loyalty card into wallet
    Given I am a squaremeal user
#    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    Then Wallet fields are correctly populated for <merchant> when lc_in_only_tc
    When For squaremeal_user I perform GET Wallet_overview
    Then I see a 200
    Then Wallet_overview fields are correctly populated for <merchant> when lc_in_only_tc
    When For squaremeal_user I perform GET Wallet_by_card_id
    Then I see a 200
    Then Wallet_by_card_id fields are correctly populated for <merchant> when lc_in_only_tc
    When For squaremeal_user I perform GET transaction for loyalty card with unauthorised for <merchant>
#    And For squaremeal_user I perform GET balance for loyalty card with unauthorised for <merchant>
    And For squaremeal_user I perform GET voucher for loyalty card with unauthorised for <merchant>

    Examples:
      | merchant      |journey_type      |
      | SquareMeal    | add_and_authorise|

 # @invalid_json_trusted @sandbox_regression
 # Scenario Outline: Add loyalty card in trusted channel with malformed request
 #   Given I am a squaremeal user
 #   When I perform POST request to add trusted channel "<merchant>" loyalty card with "<request_payload>" with "<status_code>"
#    Then I see a "<error_message>" error message
 #   And I see a "<error_slug>" error slug

  #  Examples:
  #    | merchant     | error_message | error_slug        | request_payload | status_code |
  #    | SquareMeal   | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @invalid_request_trusted @sandbox_regression
  Scenario Outline: Add loyalty card in trusted channel with unprocessable entity
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "<merchant>" loyalty card with "<request_payload>" with "<status_code>"
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant     | error_message             | error_slug             | request_payload | status_code |
      | SquareMeal   | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @sending_invalid_token_trusted @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for add trusted journey (Unauthorized)
    Given I am a squaremeal user
    When I perform POST <merchant> membership_card request for add_trusted with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | status_code_returned | error_message             | error_slug    |
      | SquareMeal  | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @add_and_auth_ntc_in_tc @sandbox_regression
  Scenario Outline: Trusted channel adds loyalty card into wallet which already exists in Non trusted channel
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    Then I see a 202
    And verify that for halifax_user data stored in after "<journey_type>" journey for "<merchant>"
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    And All Wallet fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_overview
    Then I see a 200
    And All Wallet_overview fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_by_card_id
    Then I see a 200
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For squaremeal_user I perform GET balance for loyalty card with authorised for <merchant>
    And For squaremeal_user I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant      | journey_type      |payment_card_provider|
      | SquareMeal    | add_and_authorise |master               |

@add_and_auth_tc_in_ntc @sandbox_regression
  Scenario Outline: Non Trusted channel adds loyalty card into wallet which already exists in Trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"
    When For lloyds_user I perform GET Wallet
    Then I see a 200
    And All Wallet fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_overview
    Then I see a 200
    And All Wallet_overview fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_by_card_id
    Then I see a 200
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When For lloyds_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET balance for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant      | status_code_returned | journey_type      |payment_card_provider|
      | SquareMeal    | 202                  | add_and_authorise |master               |

#  @add_and_auth_existing_field_tc @sandbox_regression
#  Scenario Outline: Add existing card again into wallet in trusted channel
#    Given I am a squaremeal user
#    When I perform POST request to add trusted channel "<merchant>" loyalty card
#    And I perform POST request again to add "<merchant>" in trusted channel with "<status_code_returned>"
#    Then I see a <status_code_returned>
#    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
#
#    Examples:
#      | merchant      | status_code_returned | journey_type      |
#      | SquareMeal    | 200                  | add_and_authorise |

  @add_and_auth_pll_tc @sandbox_regression
  Scenario Outline: verify PLL for add card in trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant   | status_code_returned | journey_type |
      | master                | SquareMeal | 201                  | pll          |

