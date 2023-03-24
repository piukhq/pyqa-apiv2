# Created by nehapatil on 22/02/2022
@membership_cards_by_id @membership_cards @wallet
Feature: View Wallet by loyalty card id
  As a Bink user
  I want to view details of single loyalty cards
  so that I do not have to call multiple different endpoints


   @view_wallet_by_loyalty_card_id @bink_regression_api2
  Scenario Outline: View wallet loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      | Wasabi        | 200                 |master               |
      |Iceland        |200                  |master               |
      |Viator         |200                  |master               |

     @wallet_lcbyid_unauthorised @bink_regression_api2 @sandbox_regression
  Scenario Outline: Get wallet lc by id with unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |

#  @view_my_walletlcbyid_put_invalid @sandbox_regression
#  Scenario Outline: View my wallet lc by id after authorising lc with invalid credentials
#    Given I am in Bink channel to get b2b token
#    When I perform POST token request for token type "b2b" to get access token
#    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
#    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
#    And I perform PUT request to authorise "<merchant>" membership card with "unauthorised" with "202"
#    And I perform GET Wallet_by_card_id
#    Then I see a <status_code_returned>
#    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>
#
#    Examples:
#      | merchant      | status_code_returned|payment_card_provider|
#      |Wasabi        | 200                  |master              |
#      |Iceland        |200                  |master               |

  @view_wallet_by_loyalty_card_id_invalid @bink_regression_api2
  Scenario Outline: Verify invalid token scenario for get Wallet loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET request with <invalid> to view Wallet_by_card_id
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | status_code_returned| error_message                      |error_slug        |merchant| invalid|
      | 401                  | Supplied token is invalid         |INVALID_TOKEN     |Wasabi  | token  |
      |404                   |Could not find this account or card|RESOURCE_NOT_FOUND|Wasabi  |scheme_account_id|

  @wallet_loyaltycard_pll_status1 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug                     |description |
     | Wasabi   | 200                 | master              |active|null                    |null       |

  @wallet_loyaltycard_pll_status2 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id pll links for inactive payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | status_code_returned|payment_card_provider|state     |slug                     |description                                                     |
     | Wasabi   | 200                 | master              |inactive  |PAYMENT_ACCOUNT_INACTIVE |The Payment Account is not active so no PLL link can be created.|

  @wallet_loyaltycard_pll_status3 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | request_payload | status_code | status_code_returned| payment_card_provider | state    | slug                        | description                                                      |
     | Wasabi   | unauthorised    | 202         | 200                 | master                | inactive | LOYALTY_CARD_NOT_AUTHORISED | The Loyalty Card is not authorised so no PLL link can be created. |

  @wallet_loyaltycard_pll_status4 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id pll links for inactive payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                                      | description                                                                                   |
     | Wasabi   | unauthorised    | 202         | 200                  | master                | inactive | PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |


  @wallet_loyaltycard_pll_status5 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id ubiquity collision pll links for two users
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    And I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    And I perform DELETE request to delete the first wallet "<merchant>" membership card
    And I perform DELETE request to delete the first wallet "<payment_card_provider>" the payment card

     Examples:
     | merchant | status_code_returned | payment_card_provider | state    | slug               | description                                                                                |
     | Wasabi   | 200                  | visa                  | inactive |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |
