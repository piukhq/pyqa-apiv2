# Created by nehapatil on 22/02/2022
@membership_cards_by_id @membership_cards
Feature: View Wallet by loyalty card id
  As a Bink user
  I want to view details of single loyalty cards
  so that I do not have to call multiple different endpoints


   @view_wallet_by_loyalty_card_id @bink_regression_api2
  Scenario Outline: View wallet loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card using b2b token
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator         |200                  |master               |

     @wallet_lcbyid_unauthorised @bink_regression_api2 @sandbox_regression
  Scenario Outline: Get wallet lc by id with unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |


  @wallet_loyaltycard_pll_status3 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | request_payload | status_code | status_code_returned| payment_card_provider | state    | slug                        | description                                                      |
     | Viator   | unauthorised    | 202         | 200                 | master                | inactive | LOYALTY_CARD_NOT_AUTHORISED | The Loyalty Card is not authorised so no PLL link can be created. |

  @wallet_loyaltycard_pll_status4 @bink_regression_api2 @ubiquity_collision
  Scenario Outline: Verify wallet loyalty card by id pll links for inactive payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                                      | description                                                                                   |
     | Viator   | unauthorised    | 202         | 200                  | master                | inactive | PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |
