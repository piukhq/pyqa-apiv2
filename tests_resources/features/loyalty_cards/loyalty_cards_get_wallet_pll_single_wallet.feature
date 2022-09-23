# Created by bularaghavan on 16/09/2022
@membership_cards_pll @pll_get_wallet_single
Feature: View single wallet pll
  As a Bink user
  I want to see the Status of the PLL Link between a given loyalty card and payment card in my given wallet
  so that I fully understand the state of my wallet

@wallet_pll_status1 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify wallet pll links for active payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug                     |description |
     | Wasabi   | 200                 | master              |active|null                    |null       |

  @wallet_pll_status2 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify wallet pll links for inactive payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned|payment_card_provider|state     |slug                     |description                                                     |
     | Wasabi   | 200                 | master              |inactive  |PAYMENT_ACCOUNT_INACTIVE |The Payment Account is not active so no PLL link can be created.|

  @wallet_pll_status3 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify wallet pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                        | description                                                      |
     | Wasabi   | unauthorised    | 202         | 200                  | master                | inactive | LOYALTY_CARD_NOT_AUTHORISED | The Loyalty Card is not authorised so no PLL link can be created. |

  @wallet_pll_status4 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify wallet pll links for inactive payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                                      | description                                                                                   |
     | Wasabi   | unauthorised    | 202         | 200                  | master                | inactive | PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |

  @wallet_delete_lc_pll @bink_regression_api2 @sandbox_regression
  Scenario Outline: No PLL link when loyalty card deleted from single wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    When I perform GET Wallet
    Then I can see empty loyalty card and empty payment account PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Wasabi   | 200                   | master                |active |null |null         |

    @wallet_delete_pc_pll @bink_regression_api2 @sandbox_regression
    Scenario Outline: No PLL link when payment card deleted from single wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When I perform GET Wallet
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet


     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Wasabi   | 200                   | master                |active |null |null         |