# Created by bularaghavan on 16/09/2022
@bink_regression_api2
Feature: View multi wallet pll
  As a Bink user
  I want to see the Status of the PLL Link between a given loyalty card and payment card in my given wallet
  so that I fully understand the state of my wallet, independent of what is linked/unlinked in other wallets


  Scenario Outline: Verify pll links for active payment account and authorised loyalty card for multi wallets
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    And For halifax_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_active journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug                     |description |
     | Viator   | 200                 | master              |active|null                    |null        |


  Scenario Outline: Verify pll links for pending payment account and authorised loyalty card for multi wallets
    Given I am a bos user
    When I perform POST request to add a pending "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    And For bos_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for bos_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state  |slug                     |description                                                                        |
     | Viator   | 200                 | master              |pending|PAYMENT_ACCOUNT_PENDING  |When the Payment Account becomes active, the PLL link will automatically go active.|


  Scenario Outline: Verify pll links for inactive payment account and authorised loyalty card for multi wallets
    Given I am a Lloyds user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a halifax user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    And For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For halifax_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    And verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|state      | slug                     |description                                                      |
     | Viator   | 200                 |master               |inactive   |PAYMENT_ACCOUNT_INACTIVE  |The Payment Account is not active so no PLL link can be created. |

  Scenario Outline: Verify pll links for active payment accounts, authorised lc in first and unauthorised lc in second wallet

    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
And add and auth "<merchant>" membership card with "unauthorised" with "202"
    And For bos_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet
    And verify that for bos_user data stored in after pll_active journey for "<merchant>"

     Examples:
     | merchant |status_code_returned |payment_card_provider|state | state2   |slug | slug2                       | description| description2                                                      |
     | Viator   |200                  |master               |active| inactive |null | LOYALTY_CARD_NOT_AUTHORISED | null       | The Loyalty Card is not authorised so no PLL link can be created. |


  Scenario Outline: Verify pll links for inactive payment account and unauthorised loyalty card for multi wallets

    Given I am a bos user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
And add and auth "<merchant>" membership card with "unauthorised" with "202"
    And For bos_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned | payment_card_provider |state   |slug                       |slug2                                      |description                                                     | description2                                                                                  |
     | Viator   | 200                  | master                |inactive|PAYMENT_ACCOUNT_INACTIVE   |PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE  |The Payment Account is not active so no PLL link can be created.| The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |

   Scenario Outline: Verify Ubiquity Collision for two users in different channels
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    And For halifax_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' for loyalty card PLL links in the Wallet
     And I can see '<state1>','<slug1>' and '<description1>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>', '<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet
    And verify that for lloyds_user data stored in after pll_inactive journey for "<merchant>"


     Examples:
     | merchant | status_code_returned |payment_card_provider |state1 | slug1 |description1 | state2             | slug2              | description2                                                                               |
     | Viator   | 200                  |visa                  |active | null  |null         |inactive            |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |

  Scenario Outline: Verify pending payment status in two channels
    Given I am a Lloyds user
    When I add membership card with transactions and vouchers for "<merchant>"
    And I perform POST request to add a pending "<payment_card_provider>" payment account to wallet
    Given I am a halifax user
    When add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' for loyalty card PLL links in the Wallet
    And I can see '<state1>','<slug1>' and '<description1>' for payment accounts PLL links in the Wallet
    When For halifax_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>', '<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet
    And verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1 | slug1                   |description1                                                                        | state2   | slug2                       | description2                                                      |
     | Wasabi   | 200                  | visa                  |pending| PAYMENT_ACCOUNT_PENDING |When the Payment Account becomes active, the PLL link will automatically go active. |inactive  |LOYALTY_CARD_NOT_AUTHORISED  | The Loyalty Card is not authorised so no PLL link can be created. |


  Scenario Outline: Verify PLL links for failed join scenario
    Given I am a Lloyds user
    When I perform enrol_failed POST request to join "<merchant>" membership card
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    Given I am a halifax user
    When I perform enrol_failed POST request to join "<merchant>" membership card
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
  #  And I can see '<state>','<slug1>' and '<description1>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug1>' and '<description1>' for payment accounts PLL links in the Wallet
    When For halifax_user I perform GET Wallet
    Then I see a <status_code_returned>
  #  And I can see '<state>','<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet
    And verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned | payment_card_provider |state           |slug1                        |description1                                                      |slug2                |description2                                                                                |
     | Viator   | 200                 | visa                  |inactive        | LOYALTY_CARD_NOT_AUTHORISED |The Loyalty Card is not authorised so no PLL link can be created. |UBIQUITY_COLLISION   | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account.|

  Scenario Outline: Verify pending payment status in two channels
    Given I am a Lloyds user
    When I add membership card with transactions and vouchers for "<merchant>"
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    Then verify that for lloyds_user data stored in after pll_active journey for "<merchant>"
    Given I am a halifax user
    When I add membership card with transactions and vouchers for "<merchant>"
    And I perform POST request to add a pending "<payment_card_provider>" payment account to wallet
    And For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' for loyalty card PLL links in the Wallet
    And I can see '<state1>','<slug1>' and '<description1>' for payment accounts PLL links in the Wallet
    When For halifax_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>', '<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet
    And verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1 | slug1 |description1| state2 | slug2                  | description2                                                                       |
     | Viator   | 200                  | visa                  |active | null  |null        |pending |PAYMENT_ACCOUNT_PENDING | When the Payment Account becomes active, the PLL link will automatically go active.|


   Scenario Outline: PLL link when loyalty card deleted from multiple wallet
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      And For lloyds_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      Given I am a halifax user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      When For halifax_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      And I perform DELETE request to delete the "<merchant>" membership card
      When For lloyds_user I perform GET Wallet
      Then I can see empty loyalty card and empty payment account PLL links in the Wallet
      When For lloyds_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Viator   | 200                   | master                |active |null |null         |


   Scenario Outline: PLL link when payment account deleted from multiple wallet
      Given I am a halifax user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      And For halifax_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      When For lloyds_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When For lloyds_user I perform GET Wallet
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet
      When For halifax_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Viator   | 200                   | master                |active |null |null         |
