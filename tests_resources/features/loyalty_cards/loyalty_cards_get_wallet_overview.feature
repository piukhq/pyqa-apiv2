@membership_cards_wallet_overview @membership_cards @wallet
Feature: Overview of wallet information
  As an API v2.0 consuming channel,
  I want to see an overview of wallet information
  so that I can display this on the front end without having to call the larger /wallet endpoint

  @view_wallet_overview_success @bink_regression_api2
  Scenario Outline: Get wallet overview success
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All 'Wallet_overview' fields are correctly populated for <merchant>

  Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator         |200                  |master               |

  @wallet_overview_unauthorised @bink_regression_api2 @sandbox_regression
  Scenario Outline: Get wallet overview with unauthorised loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    And I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And Wallet_overview fields are correctly populated for unauthorised LC of <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |

   @wallet_overview_empty_list @bink_regression_api2
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

   @wallet_overview_invalid_token @bink_regression_api2
  Scenario Outline: Verify invalid token scenario for get Wallet overview
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request with <invalid> to view Wallet_overview
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

     Examples:
     | status_code_returned | error_message              | error_slug     |invalid|
     | 401                  | Supplied token is invalid  | INVALID_TOKEN |token   |
