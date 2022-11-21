# Created by bularaghavan on 16/09/2022
@membership_cards_pll @pll_get_wallet_multi @trusted
Feature: View multi wallet pll
  As a Bink user
  I want to see the Status of the PLL Link between a given loyalty card and payment card in my given wallet
  so that I fully understand the state of my wallet, independent of what is linked/unlinked in other wallets

  @multi_wallet_pll_status1 @sandbox_regression
  Scenario Outline: Verify pll links for active payment account and authorised loyalty card for multi wallets
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For bink_user2 I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug                     |description |
     | Wasabi   | 200                 | master              |active|null                    |null        |

  @multi_wallet_pll_status2 @sandbox_regression
  Scenario Outline: Verify pll links for inactive payment account and authorised loyalty card for multi wallets
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For bink_user2 I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned|payment_card_provider|state |state2     |slug|slug2                     |description|description2                                                     |
     | Wasabi   | 200                 |master               |active|inactive   |null|PAYMENT_ACCOUNT_INACTIVE  |null       |The Payment Account is not active so no PLL link can be created. |

  @multi_wallet_pll_status3 @sandbox_regression
  Scenario Outline: Verify pll links for active payment account and unauthorised loyalty card for multi wallets
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state | state2   |slug | slug2                       | description| description2                                                      |
     | Wasabi   |  200                  | master                |active| inactive |null | LOYALTY_CARD_NOT_AUTHORISED | null       | The Loyalty Card is not authorised so no PLL link can be created. |

  @multi_wallet_pll_status4 @sandbox_regression
  Scenario Outline: Verify pll links for inactive payment account and unauthorised loyalty card for multi wallets
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    Given I am a Lloyds user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
    And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned | payment_card_provider |state |  state2    |slug   |slug2                                      |description| description2                                                                                  |
     | Wasabi   | 200                  | master                |active| inactive   |null   |PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE  |null       | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |

  @multi_wallet_pll_status5a @UC_same_channel @sandbox_regression
  Scenario Outline: Verify Ubiquity Collision for two users in the same channel
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    And I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' for loyalty card PLL links in the Wallet
    And I can see '<state1>','<slug1>' and '<description1>' for payment accounts PLL links in the Wallet
    When For bink_user2 I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>', '<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1            |  slug1              |description1 | state2   | slug2              | description2                                                                               |
     | Wasabi   | 200                  | visa                  |active            |  null               |null         |inactive  |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |


   @multi_wallet_pll_status5b @UC_different_channels @sandbox_regression
  Scenario Outline: Verify Ubiquity Collision for two users in different channels
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' for loyalty card PLL links in the Wallet
     And I can see '<state1>','<slug1>' and '<description1>' for payment accounts PLL links in the Wallet
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And I can see '<state2>', '<slug2>' and '<description2>' for loyalty card PLL links in the Wallet
    And I can see '<state2>','<slug2>' and '<description2>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1            |  slug1              |description1 | state2             | slug2              | description2                                                                               |
     | Wasabi   | 200                  | visa                  |active            |  null               |null         |inactive            |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |

    @multi_wallet_delete_lc_pll @sandbox_regression
   Scenario Outline: PLL link when loyalty card deleted from multiple wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And For bink_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      When For lloyds_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      And I perform DELETE request to delete the "<merchant>" membership card
      When For lloyds_user I perform GET Wallet
      Then I can see empty loyalty card and empty payment account PLL links in the Wallet
      When For bink_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Wasabi   | 200                   | master                |active |null |null         |

  @multi_wallet_delete_pc_pll @sandbox_regression
   Scenario Outline: PLL link when payment account deleted from multiple wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And For bink_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      When For lloyds_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When For lloyds_user I perform GET Wallet
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet
      When For bink_user I perform GET Wallet
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' for loyalty card PLL links in the Wallet
      And I can see '<state>','<slug>' and '<description>' for payment accounts PLL links in the Wallet

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Wasabi   | 200                   | master                |active |null |null         |