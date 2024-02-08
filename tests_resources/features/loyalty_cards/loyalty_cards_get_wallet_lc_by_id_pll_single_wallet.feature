# Created by bularaghavan on 26/09/2022
 @membership_cards
Feature: View Wallet by loyalty card id
  As a Bink user
  I want to view PLL details of single loyalty cards
  so that I do not have to call multiple different endpoints

  @wallet_loyaltycard_pll_status1 @bink_regression_api2
  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    And verify that for bink_user data stored in after pll_active journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug  |description |
     | Wasabi   | 200                 | master              |active|null |null        |

  @wallet_loyaltycard_pll_status2 @bink_regression_api2
  Scenario Outline: Verify wallet loyalty card by id pll links for inactive payment account and authorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    And verify that for bink_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state     |slug                     |description                                                     |
     | Wasabi   | 200                 | master              |inactive  |PAYMENT_ACCOUNT_INACTIVE |The Payment Account is not active so no PLL link can be created.|

  @wallet_loyaltycard_pll_status3 @bink_regression_api2
  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    And verify that for bink_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | request_payload | status_code | status_code_returned| payment_card_provider | state    | slug                        | description                                                       |
     | Wasabi   | unauthorised    | 202         | 200                 | master                | inactive | LOYALTY_CARD_NOT_AUTHORISED | The Loyalty Card is not authorised so no PLL link can be created. |

  @wallet_loyaltycard_pll_status4 @bink_regression_api2
  Scenario Outline: Verify wallet loyalty card by id pll links for inactive payment account and unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    And verify that for bink_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                                      | description                                                                                   |
     | Wasabi   | unauthorised    | 202         | 200                  | master                | inactive | PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |

    @wallet_lcid_delete_pc_pll @bink_regression_api2 @sandbox_regression
    Scenario Outline: No PLL link when payment card deleted from single wallet loyalty card by id
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I add and authorise "<merchant>" membership card with transactions and vouchers
      And I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When I perform GET Wallet_by_card_id
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet loyalty card by id


     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Wasabi   | 200                   | master                |active |null |null         |
