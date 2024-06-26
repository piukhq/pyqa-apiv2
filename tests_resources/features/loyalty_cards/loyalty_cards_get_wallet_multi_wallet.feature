# Created by nehapatil on 10/08/2022
 @bink_regression_api2 @membership_cards
Feature: View Wallets
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets
  Scenario Outline: View wallet in different channels when both LCs are authorised
    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card

    Given I am a Lloyds user
    When I add and authorise "<merchant>" membership card
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For bos_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |



  Scenario Outline: View two wallet of same channel when LCs are authorised in both
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card

    Given I am a bos user
    When I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card

    And For bos_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |
