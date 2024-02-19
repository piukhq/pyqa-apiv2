# Created by nehapatil on 10/08/2022
 @bink_regression_api2
Feature: View Wallets overview
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets



  Scenario Outline: View wallet overview in different channels when both LCs are authorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        |200                  |master               |


  Scenario Outline: View wallet overview in different channels when both LCs are unauthorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|request_payload | status_code|
       |Viator        |200                  |master               | unauthorised  | 202        |




   Scenario Outline: View two wallet overview of same channel when LCs are authorised in both
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    # When I add membership card with transactions and vouchers for "<merchant>"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |


   Scenario Outline: View two wallet overview of same channel when LC1 unauth and LC2 auth
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    When For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |


  Scenario Outline: View two wallet overview of different channel when LC1 unauth and LC2 auth
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user2 I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |
