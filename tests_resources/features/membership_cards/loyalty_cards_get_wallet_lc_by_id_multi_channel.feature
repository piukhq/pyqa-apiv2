# Created by nehapatil on 10/08/2022
@membership_cards_wallet @membership_cards @multi_wallet
Feature: View Wallet by LC id in different channel
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets


   @wallet_by_lc_id_multi_channel @add_and_auth_multi_channel
  Scenario Outline: View Wallet by LC id in different channel when both LCs are authorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet_by_card_id'
    Then I see a <status_code_returned>
    And All 'Wallet_by_card_id' fields are correctly populated for <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet_by_card_id'
    Then I see a <status_code_returned>
    And All 'Wallet_by_card_id' fields are correctly populated for <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
#      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


     @wallet_by_lc_id_unauth_multi_channel @add_and_auth_multi_channel
  Scenario Outline: View Wallet by LC id in different channel when both LCs are unauthorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET 'Wallet_by_card_id'
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET 'Wallet_by_card_id'
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|request_payload | status_code|
      |Wasabi        | 200                  |master              |unauthorised     | 202        |
#      |Iceland        |200                  |master               | unauthorised  | 202        |
#      |HarveyNichols  |200                  |master               | unauthorised  | 202        |
