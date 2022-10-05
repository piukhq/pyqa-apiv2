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
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi        | 200                  |master              |
      |Iceland        |200                  |master               |
      |HarveyNichols  |200                  |master               |


  @wallet_invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify invalid token scenario for get Wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request with <invalid> to view Wallet
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | status_code_returned | error_message             | error_slug    |invalid|
      | 401                  | Supplied token is invalid | INVALID_TOKEN |token  |

  @wallet_failed_join @bink_regression_api2 @sandbox_regression
  Scenario Outline: verify wallet for joins
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "master" payment account to wallet
    And I perform <scheme_state> POST request to join "<merchant>" membership card
    And I perform GET Wallet
    Then I see a <status_code_returned>
    And Verify Wallet fields for <merchant> with <scheme_state>

    Examples:
      | merchant| status_code_returned |  scheme_state         |
      | Iceland | 200                  |  enrol_failed        |
      | Iceland | 200                  |  join_success         |
      | Iceland | 200                  | asynchronous_join_in_progress |