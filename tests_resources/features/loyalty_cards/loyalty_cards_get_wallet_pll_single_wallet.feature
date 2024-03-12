# Created by bularaghavan on 16/09/2022

   @bink_regression_api2

Feature: View single wallet pll
  As a Bink user
  I want to see the Status of the PLL Link between a given loyalty card and payment card in my given wallet
  so that I fully understand the state of my wallet


  Scenario Outline: Verify wallet pll links for active payment account and authorised loyalty card
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_active journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug |description |
     | SquareMeal   | 200                 | master              |active|null|null       |

  Scenario Outline: Verify wallet pll links for inactive payment account and authorised loyalty card
    Given I am a Lloyds user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state     |slug                     |description                                                     |
     | SquareMeal   | 200                 | master              |inactive  |PAYMENT_ACCOUNT_INACTIVE |The Payment Account is not active so no PLL link can be created.|

  Scenario Outline: Verify wallet pll links for active payment account and unauthorised loyalty card
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                        | description                                                      |
     | SquareMeal   | unauthorised    | 202         | 200                  | master                | inactive | LOYALTY_CARD_NOT_AUTHORISED | The Loyalty Card is not authorised so no PLL link can be created. |

  Scenario Outline: Verify wallet pll links for inactive payment account and unauthorised loyalty card
    Given I am a Lloyds user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider | state    | slug                                      | description                                                                                   |
     | SquareMeal   | unauthorised    | 202         | 200                  | master                | inactive | PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |

  Scenario Outline: No PLL link when loyalty card deleted from single wallet
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And I perform DELETE request to delete the "<merchant>" membership card
    When I perform GET Wallet
    Then I can see empty loyalty card and empty payment account PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | SquareMeal   | 200                   | master                |active |null |null         |

    Scenario Outline: No PLL link when payment card deleted from single wallet
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add and authorise "<merchant>" membership card
      And I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When I perform GET Wallet
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet


     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | SquareMeal   | 200                   | master                |active |null |null         |
