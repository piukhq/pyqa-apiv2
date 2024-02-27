# Created by bularaghavan on 01/12/2021
Feature: View Vouchers
As a Bink user I want to view my loyalty card vouchers in my wallet
so that I am aware and have visibility of the vouchers that have been concluded with my loyalty card


  @bink_regression_api2
  Scenario Outline: Get Loyalty card vouchers
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    When I add and authorise "<merchant>" membership card
    And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | Viator        | 200                  |
