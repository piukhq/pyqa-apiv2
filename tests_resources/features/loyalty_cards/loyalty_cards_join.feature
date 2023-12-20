# Created by rupalpatel at 06/10/2021
@membership_card_join @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to join a loyalty scheme
  so that I can use the Bink functionality with the relevant loyalty plan

  @join_scheme @bink_regression_api2
  Scenario Outline: join journey
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type |
      | SquareMeal    | 202                  | join         |


  @pll_join @bink_regression_api2
  Scenario Outline: verify PLL for join journey
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant | status_code_returned | journey_type |
      | master                | Viator  | 202                  | pll_active   |


  @multi_wallet_joins @bink_regression_api2
  Scenario Outline: join requests in multiwallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then Verify Wallet fields for <merchant> with join_success
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    When I perform GET Wallet
    Then Verify Wallet fields for <merchant> with join_success

    Examples:
      | merchant      | status_code_returned |
      | The_Works     | 202                  |
