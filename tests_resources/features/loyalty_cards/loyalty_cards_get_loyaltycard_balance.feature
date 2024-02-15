# Created by bularaghavan on 25/11/2021
@bink_regression_api2 @membership_cards
Feature: View balance
As a Bink user
I want to view my loyalty card balances in my wallet
so that I am aware and have visibility of my rewards

  Scenario Outline: Get Loyalty card balance
   When I add membership card with transactions and vouchers for "<merchant>"
   And As a bos_user I performed GET balance for authorised <merchant> membership card
   Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | The_Works     | 200                  |
