# Created by bularaghavan on 26/09/2022
@bink_regression_api2 @membership_cards
Feature: View multi wallet loyalty card by id  pll
  As a Bink user
  I want to see the Status of the PLL Link between a given loyalty card and payment card in my given wallet
  so that I fully understand the state of my wallet, independent of what is linked/unlinked in other wallets

  Scenario Outline: Verify wallet loyalty card by id pll links for active payment account and authorised loyalty card for multi wallet loyalty card by id
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I add and authorise "<merchant>" membership card
    And For halifax_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    When For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And verify that for halifax_user data stored in after pll_active journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|
     | Viator   | 200                 | master              |


  Scenario Outline: Verify pll links for inactive payment account and authorised loyalty card for multi wallet loyalty card by id
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card
    Then verify that for lloyds_user data stored in after pll_active journey for "<merchant>"
    Given I am a halifax user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card
    And For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    When For halifax_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned|payment_card_provider|
     | Viator   | 200                 |master               |
  Scenario Outline: Verify pll links for active payment account and unauthorised loyalty card for multi wallet loyalty card by id
     Given I am a bos user
     When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
     When I add membership card with transactions and vouchers for "<merchant>"
     Then verify that for bos_user data stored in after pll_active journey for "<merchant>"
     When For bos_user I perform GET Wallet_by_card_id
     Then I see a <status_code_returned>
     Given I am a Lloyds user
     When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
     When add and auth "<merchant>" membership card with "unauthorised" with "202"
     Then verify that for lloyds_user data stored in after pll_active journey for "<merchant>"
     When For lloyds_user I perform GET Wallet_by_card_id
     Then I see a <status_code_returned>
     And I can see '<state>','<slug>' and '<description>' in PLL links for Wallet loyalty card by id
     When For bos_user I perform GET Wallet_by_card_id
     Then I see a <status_code_returned>

     Examples:
     | merchant | status_code_returned | payment_card_provider |state    | slug                       |description                                                      |
     | Viator   | 200                   | master                |inactive|LOYALTY_CARD_NOT_AUTHORISED |The Loyalty Card is not authorised so no PLL link can be created.|

  Scenario Outline: Verify pll links for inactive payment account and unauthorised loyalty card for multi wallet loyalty card by id
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Then verify that for lloyds_user data stored in after pll_active journey for "<merchant>"
    When For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    Given I am a halifax user
    When I perform POST request to add a duplicate "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    Then verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"
    When For halifax_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    When For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>


     Examples:
     | merchant |status_code_returned | payment_card_provider |
     | Viator   | 200                 | master                |
  Scenario Outline: UC for multi wallet lc by id users in same channels
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card
    Then verify that for bink_user data stored in after pll_active journey for "<merchant>"
    When For bink_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    When For bink_user2 I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And verify that for bink_user2 data stored in after pll_inactive journey for "<merchant>"

     Examples:
     | merchant | status_code_returned | payment_card_provider |                                                                             |
     | Viator   | 200                  | visa                  |

  Scenario Outline: Verify pending payment status in two channels for multi wallet loyalty card by id
     Given I am a Lloyds user
     When I add membership card with transactions and vouchers for "<merchant>"
     And I perform POST request to add a pending "<payment_card_provider>" payment account to wallet
     Then verify that for lloyds_user data stored in after pll_inactive journey for "<merchant>"
     Given I am a halifax user
     When add and auth "<merchant>" membership card with "unauthorised" with "202"
     And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
     Then verify that for halifax_user data stored in after pll_inactive journey for "<merchant>"
     When For lloyds_user I perform GET Wallet_by_card_id
     Then I see a 200
     When For halifax_user I perform GET Wallet_by_card_id
     Then I see a 200

     Examples:
     | merchant | payment_card_provider |
     | Viator   | visa                  |


   Scenario Outline: No PLL link in get wallet loyalty card by id when loyalty card deleted from single wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      And For bink_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      And For lloyds_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>
      And I perform DELETE request to delete the "<merchant>" membership card
      When For lloyds_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned2>
      And I see a "<error_message>" error message
      And I see a "<error_slug>" error slug
      When For bink_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>

     Examples:
     | merchant | status_code_returned | payment_card_provider  |status_code_returned2|error_message                      |error_slug        |
     | Viator   | 200                   | master                 |404                  |Could not find this account or card|RESOURCE_NOT_FOUND|


   Scenario Outline: No PLL link in get wallet loyalty card by id when payment card deleted from single wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      And For bink_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When I add membership card with transactions and vouchers for "<merchant>"
      And For lloyds_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>
      And I perform DELETE request to delete "<payment_card_provider>" the payment card
      When For lloyds_user I perform GET Wallet_by_card_id
      Then I can see empty payment account and empty loyalty card PLL links in the Wallet loyalty card by id
      When For bink_user I perform GET Wallet_by_card_id
      Then I see a <status_code_returned>

     Examples:
     | merchant |  status_code_returned | payment_card_provider |
     | Viator   | 200                   | master                |
