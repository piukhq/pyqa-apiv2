# Created by bularaghavan on 11/11/2021
@membership_cards_wallet @membership_cards @wallet
Feature: View Wallet
  As a Bink user
  I want to view my loyalty cards in a wallet-only state
  so that I can see the cards that support store only functionality


   @view_my_wallet @bink_regression_api2
  Scenario Outline: View my wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And All 'Wallet' fields are correctly populated for <merchant>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
      |HarveyNichols  |200                  |master               |


  @wallet_invalid_token @bink_regression_api2
  Scenario Outline: Verify invalid token scenario for get Wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request to view 'Wallet' with <invalid>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | status_code_returned | error_message             | error_slug    |invalid|
      | 401                  | Supplied token is invalid | INVALID_TOKEN |token  |

  @wallet_pll_status1 @bink_regression_api2
  Scenario Outline: Verify wallet pll links for active payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug                     |description |
     | Wasabi   | 200                 | master              |active|null                    |null       |

  @wallet_pll_status2 @bink_regression_api2
  Scenario Outline: Verify wallet pll links for inactive payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

     Examples:
     | merchant | status_code_returned|payment_card_provider|state     |slug                     |description                                                     |
     | Wasabi   | 200                 | master              |inactive  |PAYMENT_ACCOUNT_INACTIVE |The Payment Account is not active so no PLL link can be created.|

  @wallet_pll_status3 @bink_regression_api2
  Scenario Outline: Verify wallet pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                        | description                                                      |
     | Wasabi   | unauthorised    | 202         | 200                  | master                | inactive | LOYALTY_CARD_NOT_AUTHORISED | The Loyalty Card is not authorised so no PLL link can be created. |

  @wallet_pll_status4 @bink_regression_api2
  Scenario Outline: Verify wallet pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                                      | description                                                                                   |
     | Wasabi   | unauthorised    | 202         | 200                  | master                | inactive | PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |


  @wallet_pll_status5 @bink_regression_api2
  Scenario Outline: Verify wallet pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    And I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And I can see '<state1>','<state2>','<slug1>','<slug2>','<description1>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state1>','<state2>','<slug1>','<slug2>','<description1>' and '<description2>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card
    And I perform DELETE request to delete the first wallet "<merchant>" membership card
    And I perform DELETE request to delete the first wallet "<payment_card_provider>" the payment card

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1            |  slug1              |description1 | state2             | slug2              | description2                                                                               |
     | Wasabi   | 200                  | visa                  |active            |  null               |null         |inactive            |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |


  @wallet_state_slug_descr_mapping
  Scenario Outline: verify state, slug and description in the wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform <scheme_state> POST request to join "<merchant>" membership card
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And Verify state, slug and description in the wallet for <scheme_state>
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant      | status_code_returned |  scheme_state |
      | HarveyNichols | 200                  |  enrol_failed         |
      | HarveyNichols | 200                  |  join_success         |
      | HarveyNichols | 200                  | asynchronous_join_in_progress |