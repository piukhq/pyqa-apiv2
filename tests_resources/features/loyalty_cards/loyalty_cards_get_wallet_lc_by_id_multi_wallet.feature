# Created by nehapatil on 10/08/2022
@bink_regression_api2 @membership_cards
Feature: View Wallet by LC id in different channel
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets


  Scenario Outline: View Wallet by LC id in different channel when both LCs are authorised

    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    When For bos_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator         | 200                  |master              |



  Scenario Outline: View two wallet by LC id of same channel when LC1 unauth and LC2 auth
    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    And For bos_user I perform GET Wallet_by_card_id

    Given I am a halifax user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For halifax_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |

  @wallet_by_lc_id_multi_channel_invalid_valid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet by LC id of different channel when LC1 is unauth and LC2 is auth
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For lloyds_user I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And Wallet_by_card_id fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user2 I perform GET Wallet_by_card_id
    Then I see a <status_code_returned>
    And All Wallet_by_card_id fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |
