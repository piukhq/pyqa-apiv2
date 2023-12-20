# Created by bularaghavan on 25/11/2021
@membership_cards_balance @membership_cards
Feature: View balance
As a Bink user
I want to view my loyalty card balances in my wallet
so that I am aware and have visibility of my rewards

  @view_loyalty_balance @bink_regression_api2 @sandbox_regression
  Scenario Outline: Get Loyalty card balance
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET balance for loyalty card with authorised for <merchant>
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | Iceland       | 200                  |
