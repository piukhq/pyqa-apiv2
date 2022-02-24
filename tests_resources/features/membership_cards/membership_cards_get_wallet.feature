# Created by bularaghavan on 11/11/2021
@membership_cards_wallet @membership_cards
Feature: View Wallet
  As a Bink user
  I want to view my loyalty cards in a wallet-only state
  so that I can see the cards that support store only functionality

#  @view_wallet_success @bink_regression_api2
#  Scenario Outline: View Wallet success
#    Given I am a Bink Wallet user1
#    When I perform GET request to view 'Wallet'
#    Then I see a <status_code_returned>
#    And I can see all Wallet fields successfully
#
#    Examples:
#      | status_code_returned |
#      | 200                  |

   @view_my_wallet @bink_regression_api2
  Scenario Outline: View my wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform GET 'Wallet'
    Then I see a <status_code_returned>
    And All 'Wallet' fields are correctly populated for <merchant>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      | Wasabi        | 200                 | master              |
      |Iceland        |200                  |master               |
      |HarveyNichols  |200                  |master               |


  @wallet_invalid_token @bink_regression_api2
  Scenario Outline: Verify invalid token scenario for get Wallet
    Given I am a Bink Wallet user1
    When I perform GET request to view 'Wallet' with <invalid>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | status_code_returned | error_message             | error_slug    |invalid|
      | 401                  | Supplied token is invalid | INVALID_TOKEN |token  |
