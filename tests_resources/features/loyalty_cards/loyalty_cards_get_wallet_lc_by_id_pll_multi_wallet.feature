# Created by bularaghavan on 26/09/2022
@membership_cards_pll  @pll_get_wallet_lc_id_multi @membership_cards
Feature: View multi wallet loyalty card by id  pll
  As a Bink user
  I want to see the Status of the PLL Link between a given loyalty card and payment card in my given wallet
  so that I fully understand the state of my wallet, independent of what is linked/unlinked in other wallets

  @multi_wallet_loyaltycard_pll_status1 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and authorised loyalty card for multi wallet loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I call GET Wallet_by_card_id for first bink user
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    When I call GET Wallet_by_card_id for second bink user
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | status_code_returned|payment_card_provider|state|slug                     |description |
     | Wasabi   | 200                 | master              |active|null                    |null       |

  @multi_wallet_loyaltycard_pll_status2 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify pll links for inactive payment account and authorised loyalty card for multi wallet loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I call GET Wallet_by_card_id for first bink user
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    When I call GET Wallet_by_card_id for second bink user
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | status_code_returned|payment_card_provider|state |state2     |slug|slug2                     |description|description2                                                     |
     | Wasabi   | 200                 |master               |active|inactive   |null|PAYMENT_ACCOUNT_INACTIVE  |null       |The Payment Account is not active so no PLL link can be created. |

   @multi_wallet_loyaltycard_pll_status3 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify pll links for active payment account and unauthorised loyalty card for multi wallet loyalty card by id
     Given I am in Bink channel to get b2b token
     When I perform POST token request for token type "b2b" to get access token
     And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
     And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
     And I call GET Wallet_by_card_id for first bink user
     Then I see a <status_code_returned>
     And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
     Given I am a Lloyds user
     When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
     And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
     When I call GET Wallet_by_card_id for lloyds user
     Then I see a <status_code_returned>
     And I can see '<state2>','<slug2>' and '<description2>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider |state | slug |  description|state2  | slug2                      |description2                                                     |
     | Wasabi   | unauthorised    | 202         | 200                   | master               |active| null |  null       |inactive|LOYALTY_CARD_NOT_AUTHORISED |The Loyalty Card is not authorised so no PLL link can be created.|

  @multi_wallet_loyaltycard_pll_status4 @sandbox_regression @bink_regression_api2
  Scenario Outline: Verify pll links for inactive payment account and unauthorised loyalty card for multi wallet loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I call GET Wallet_by_card_id for first bink user
    Then I see a <status_code_returned>
    And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
    Given I am a Lloyds user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I call GET Wallet_by_card_id for lloyds user
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | request_payload | status_code | status_code_returned | payment_card_provider |state |  state2    |slug   |slug2                                      |description| description2                                                                                  |
     | Wasabi   | unauthorised    | 202         | 200                  | master                |active| inactive   |null   |PAYMENT_ACCOUNT_AND_LOYALTY_CARD_INACTIVE  |null       | The Payment Account and Loyalty Card are not active/authorised so no PLL link can be created. |

  @multi_wallet_loyaltycard_pll_status5a @UC_same_channel @ubiquity_collision @bink_regression_api2 @sandbox_regression
  Scenario Outline: UC for multi wallet lc by id users in same channels
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    And I call GET Wallet_by_card_id for first bink user
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' in PLL links for Wallet loyalty card by id
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I call GET Wallet_by_card_id for second bink user
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1 | slug1 |description1 | state2  | slug2              | description2                                                                               |
     | Wasabi   | 200                  | visa                  |active | null  |null         |inactive |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |

  @multi_wallet_loyaltycard_pll_status5b @UC_different_channels @ubiquity_collision @bink_regression_api2 @sandbox_regression
  Scenario Outline: UC for multi wallet lc by id users in different channels
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    And I call GET Wallet_by_card_id for first bink user
    Then I see a <status_code_returned>
    And I can see '<state1>','<slug1>' and '<description1>' in PLL links for Wallet loyalty card by id
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I call GET Wallet_by_card_id for lloyds user
    Then I see a <status_code_returned>
    And I can see '<state2>','<slug2>' and '<description2>' in PLL links for Wallet loyalty card by id

     Examples:
     | merchant | status_code_returned | payment_card_provider |state1 | slug1 |description1 | state2  | slug2              | description2                                                                               |
     | Wasabi   | 200                  | visa                  |active | null  |null         |inactive |UBIQUITY_COLLISION  | There is already a Loyalty Card from the same Loyalty Plan linked to this Payment Account. |

    @multi_wallet_lc_delete_lc_pll @sandbox_regression @bink_regression_api2
   Scenario Outline: No PLL link in get wallet loyalty card by id when loyalty card deleted from single wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And I call GET Wallet_by_card_id for first bink user
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And I call GET Wallet_by_card_id for lloyds user
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
      And I perform DELETE request to delete the "<merchant>" membership card
      When I call GET Wallet_by_card_id for lloyds user
      Then I see a <status_code_returned2>
      And I see a "<error_message>" error message
      And I see a "<error_slug>" error slug

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |status_code_returned2|error_message                      |error_slug        |
     | Wasabi   | 200                   | master                |active |null |null         |404                  |Could not find this account or card|RESOURCE_NOT_FOUND|

  @multi_wallet_lc_delete_pc_pll @sandbox_regression @bink_regression_api2
   Scenario Outline: No PLL link in get wallet loyalty card by id when payment card deleted from single wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And I call GET Wallet_by_card_id for first bink user
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      And I call GET Wallet_by_card_id for lloyds user
      Then I see a <status_code_returned>
      And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When I call GET Wallet_by_card_id for lloyds user
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet loyalty card by id

     Examples:
     | merchant |  status_code_returned | payment_card_provider |state  |slug |description  |
     | Wasabi   | 200                   | master                |active |null |null         |
