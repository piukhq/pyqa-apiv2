# Created by nehapatil on 10/08/2022
@membership_cards_wallet @multi_wallet @trusted @bink_regression_api2
Feature: View Wallets overview
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets


   @wallet_overview_multi_channel @add_and_auth_multi_channel
  Scenario Outline: View wallet overview in different channels when both LCs are authorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


     @wallet_overview_unauth_multi_channel @add_and_auth_multi_channel
  Scenario Outline: View wallet overview in different channels when both LCs are unauthorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|request_payload | status_code|
      |Wasabi        | 200                  |master              |unauthorised     | 202        |
      |Iceland        |200                  |master               | unauthorised  | 202        |
#      |HarveyNichols  |200                  |master               | unauthorised  | 202        |


  @wallet_overview_same_channel_multi_wallet @add_and_auth_multi_wallet
  Scenario Outline: View two wallet overview of same channel when LCs are authorised in both
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


  @wallet_overview_same_channel_valid_invalid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet overview of same channel when LC1 auth and LC2 unauth
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with cp2_auth_card
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and auth "<merchant>" cp2_unauth_card with "unauthorised" with "202"
    And For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    Then Wallet_overview fields are correctly populated for <merchant> when lc_in_non_tc
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


  @wallet_overview_same_channel_invalid_valid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet overview of same channel when LC1 unauth and LC2 auth
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |


  @wallet_overview_multi_channel_invalid_valid @add_and_auth_multi_wallet
  Scenario Outline: View two wallet overview of different channel when LC1 unauth and LC2 auth
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
#      |HarveyNichols  |200                  |master               |
