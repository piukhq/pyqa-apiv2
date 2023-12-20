# Created by bularaghavan on 01/12/2021
@membership_cards_transactions @membership_cards
Feature: View transactions
As a Bink user
I want to view my loyalty card transactions in my wallet so that I am aware and have visibility of the transactions that have been concluded with my loyalty card

  @view_loyalty_transactions @bink_regression_api2 @sandbox_regression
  Scenario Outline: Get Loyalty card transactions
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user I perform GET transaction for loyalty card with authorised for <merchant>
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | Iceland       | 200                  |
