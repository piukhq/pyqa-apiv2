# Created by nehapatil on 10/08/2022
@membership_cards_wallet @multi_wallet
Feature: View Wallet by LC id in different channel
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets


   @wallet_by_lc_id_multi_channel @add_and_auth_multi_channel @sandbox_regression
  Scenario Outline: View Wallet by LC id in different channel when both LCs are authorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


     @wallet_by_lc_id_unauth_multi_channel @add_and_auth_multi_channel @sandbox_regression
  Scenario Outline: View Wallet by LC id in different channel when both LCs are unauthorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|request_payload | status_code|
      |Wasabi        | 200                  |master              |unauthorised     | 202        |
      |Iceland        |200                  |master               | unauthorised  | 202        |
#      |HarveyNichols  |200                  |master               | unauthorised  | 202        |


    @wallet_by_lc_id_same_channel_multi_wallet @add_and_auth_multi_wallet @sandbox_regression
  Scenario Outline: View two wallet by LC id of same channel when LCs are authorised in both
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


  @wallet_by_lc_id_same_channel_valid_invalid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet by LC id of same channel when LC1 is auth and LC2 is unauth
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


  @wallet_by_lc_id_same_channel_invalid_valid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet by LC id of same channel when LC1 unauth and LC2 auth
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


  @wallet_by_lc_id_multi_channel_invalid_valid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet by LC id of different channel when LC1 is unauth and LC2 is auth
    Given I am a Lloyds user
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All 'Wallet_by_card_id' fields are correctly populated for <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |