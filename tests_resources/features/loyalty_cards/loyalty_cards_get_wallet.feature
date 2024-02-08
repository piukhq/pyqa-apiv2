# Created by bularaghavan on 11/11/2021
@membership_cards_wallet @membership_cards @wallet
Feature: View Wallet
  As a Bink user
  I want to view my loyalty cards in a wallet-only state
  so that I can see the cards that support store only functionality


   @view_my_wallet @bink_regression_api2 @sandbox_regression
  Scenario Outline: View my wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      |status_code_returned |payment_card_provider|
      |Viator        |200                  |master               |

  @view_my_wallet_unauthorised @bink_regression_api2 @sandbox_regression
  Scenario Outline: View my wallet with unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And Wallet fields are correctly populated for unauthorised LC of <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |
