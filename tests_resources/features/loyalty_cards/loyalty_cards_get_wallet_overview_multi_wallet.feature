# Created by nehapatil on 10/08/2022
 @bink_regression_api2
Feature: View Wallets overview
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets



  Scenario Outline: View wallet overview in different channels when both LCs are authorised
    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"

    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    When For bos_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        |200                  |master               |


  Scenario Outline: View wallet overview in different channels when both LCs are unauthorised
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For halifax_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>


    Examples:
      | merchant      | status_code_returned|payment_card_provider|request_payload | status_code|
       |Viator        |200                  |master               | unauthorised  | 202        |




   Scenario Outline: View two wallet overview of same channel when LCs are authorised in both
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card

    Given I am a Lloyds user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For halifax_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |


   Scenario Outline: View two wallet overview of same channel when LC1 unauth and LC2 auth
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    Given I am a bos user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    When For bos_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    When For halifax_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |


  Scenario Outline: View two wallet overview of different channel when LC1 unauth and LC2 auth
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And add and auth "<merchant>" membership card with "unauthorised" with "202"
    Given I am a bos user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card
    And For lloyds_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bos_user I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All Wallet_overview fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |
