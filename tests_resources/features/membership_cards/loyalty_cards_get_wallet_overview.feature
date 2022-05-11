@membership_cards_wallet_overview @membership_cards @wallet
Feature: Overview of wallet information
  As an API v2.0 consuming channel,
  I want to see an overview of wallet information
  so that I can display this on the front end without having to call the larger /wallet endpoint


  @view_wallet_overview_success
  Scenario Outline: Get wallet overview success
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform GET 'Wallet_overview'
    Then I see a <status_code_returned>
    And All 'Wallet_overview' fields are correctly populated for <merchant>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

  Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Wasabi         |200                  |master               |
      |Iceland        |200                  |master               |
      |HarveyNichols  |200                  |master               |



  @verify_wallet_overview_fully_pll
  Scenario Outline: Verify wallet overview fully pll
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform GET 'Wallet_overview'
    Then I see a <status_code_returned>
    And I see <pll_linked_payment_accounts>,<total_payment_accounts> and <is_fully_pll_linked>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete all the payment cards

  Examples:
      |merchant      | status_code_returned|payment_card_provider|pll_linked_payment_accounts|total_payment_accounts|is_fully_pll_linked|
      |Wasabi         |200                  |master               |3                         |3                     |True              |



@verify_wallet_overview_not_fully_pll
  Scenario Outline: Verify wallet overview not fully pll
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add a invalid_card_detail "<payment_card_provider>" payment account to wallet
    And I perform GET 'Wallet_overview'
    Then I see a <status_code_returned>
    And I see <pll_linked_payment_accounts>,<total_payment_accounts> and <is_fully_pll_linked>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete all the payment cards

  Examples:
      |merchant      | status_code_returned|payment_card_provider|pll_linked_payment_accounts|total_payment_accounts|is_fully_pll_linked|
      |Wasabi         |200                  |master               |2                         |3                     |False              |



  @verify_wallet_overview_unauth_LC
  Scenario Outline: Verify wallet overview no pll with unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform GET 'Wallet_overview'
    Then I see a <status_code_returned>
    And I see <pll_linked_payment_accounts>,<total_payment_accounts> and <is_fully_pll_linked>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete all the payment cards

  Examples:
      |merchant      | status_code_returned|payment_card_provider|pll_linked_payment_accounts|total_payment_accounts|is_fully_pll_linked|
      |Wasabi         |200                  |master               |0                         |3                     |False              |



   @wallet_overview_empty_list
  Scenario Outline: Get wallet overview with empty list value
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request to view wallet overview with empty list
    Then I see a <status_code_returned>
    And I see 'join' list appearing
    And I see 'loyalty_card' list appearing
    And I see 'payment_account' list appearing

    Examples:
    | status_code_returned |
    | 200                  |



   @wallet_overview_invalid_token
   Scenario Outline: Verify invalid token scenario for get Wallet overview
     Given I am in Bink channel to get b2b token
     When I perform POST token request for token type "b2b" to get access token
     And I perform GET request to view 'Wallet_overview' with <invalid>
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     | status_code_returned | error_message              | error_slug     |invalid|
     | 401                  | Supplied token is invalid  | INVALID_TOKEN |token   |
