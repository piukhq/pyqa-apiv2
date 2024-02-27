# Created by bularaghavan on 11/11/2021
 @bink_regression_api2
Feature: View Wallet
  As a Bink user
  I want to view my loyalty cards in a wallet-only state
  so that I can see the cards that support store only functionality


  Scenario Outline: View my wallet
    Given I am a bos user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      |status_code_returned |payment_card_provider|
      |Viator        |200                  |master               |
