# Created by bularaghavan on 11/11/2021
@membership_cards_wallet @membership_cards
Feature: View Wallet
  As a Bink user
  I want to view my loyalty cards in a wallet-only state
  so that I can see the cards that support store only functionality

  @view_wallet_success @bink_regression_api2
  Scenario Outline: View Wallet success
    Given I am a Bink Wallet user1
    When I perform GET request to view Wallet
    Then I see a <status_code_returned>
    And I can see all Wallet fields successfully

    Examples:
    | status_code_returned |
    | 200                  |

   @wallet_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get Wallet
     Given I am a Bink Wallet user1
     When I perform GET request to view Wallet with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     | status_code_returned | error_message              | error_slug     |
     | 401                  | Supplied token is invalid  | INVALID_TOKEN |
