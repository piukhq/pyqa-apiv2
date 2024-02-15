@membership_cards  @bink_regression_api2
Feature: Overview of wallet information
  As an API v2.0 consuming channel,
  I want to see an overview of wallet information
  so that I can display this on the front end without having to call the larger /wallet endpoint

  Scenario Outline: Get wallet overview success
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    When I add membership card with transactions and vouchers for "<merchant>"
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform GET Wallet_overview
    Then I see a <status_code_returned>
    And All 'Wallet_overview' fields are correctly populated for <merchant>

  Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator         |200                  |master               |


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


  Scenario Outline: Get wallet overview with empty list value
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And a GET request to view wallet overview with empty list
    Then I see a <status_code_returned>
    And I see 'join' list appearing
    And I see 'loyalty_card' list appearing
    And I see 'payment_account' list appearing

    Examples:
    | status_code_returned |
    | 200                  |
