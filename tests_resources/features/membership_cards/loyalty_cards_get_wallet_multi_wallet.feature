# Created by nehapatil on 10/08/2022
@membership_cards_wallet @membership_cards @multi_wallet
Feature: View Wallets
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets


   @view_my_wallet_multi_channel @add_and_auth_multi_channel
  Scenario Outline: View wallet in different channels when both LCs are authorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And All 'Wallet' fields are correctly populated for <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And All 'Wallet' fields are correctly populated for <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
#      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


     @view_my_wallet_unauth_multi_channel @add_and_auth_multi_channel
  Scenario Outline: View wallet in different channels when both LCs are unauthorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And Wallet fields are correctly populated for unauthorised LC of <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And Wallet fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|request_payload | status_code|
      |Wasabi        | 200                  |master              |unauthorised     | 202        |
#      |Iceland        |200                  |master               | unauthorised  | 202        |
#      |HarveyNichols  |200                  |master               | unauthorised  | 202        |