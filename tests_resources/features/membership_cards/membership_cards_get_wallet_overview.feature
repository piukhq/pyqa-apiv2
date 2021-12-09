@membership_cards_wallet_overview @membership_cards
Feature: Overview of wallet information
  As an API v2.0 consuming channel,
  I want to see an overview of wallet information
  so that I can display this on the front end without having to call the larger /wallet endpoint

  @view_wallet_overview_success @bink_regression_api2
  Scenario Outline: Get wallet overview success
    Given I am a Bink Wallet user1
    When I perform GET request to view 'Wallet_overview'
    Then I see a <status_code_returned>
    And I can see all Wallet fields successfully

    Examples:
    | status_code_returned |
    | 200                  |

  @wallet_overview_empty_list @bink_regression_api2
  Scenario Outline: Get wallet overview with list value
    Given I am a Bink user
    When I perform GET request to view wallet overview with empty list
    Then I see a <status_code_returned>
    And I see 'join' list appearing
    And I see 'loyalty_card' list appearing
    And I see 'payment_account' list appearing

    Examples:
    | status_code_returned |
    | 200                  |

   @wallet_overview_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get Wallet overview
     Given I am a Bink Wallet user1
     When I perform GET request to view 'Wallet_overview' with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     | status_code_returned | error_message              | error_slug     |
     | 401                  | Supplied token is invalid  | INVALID_TOKEN |
