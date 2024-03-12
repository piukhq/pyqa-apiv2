# Created by bularaghavan on 01/12/2021
Feature: View Vouchers
As a Bink user I want to view my loyalty card vouchers in my wallet
so that I am aware and have visibility of the vouchers that have been concluded with my loyalty card


  @bink_regression_api2
  Scenario Outline: Get Loyalty card vouchers
    Given I am a bos user
    When I add and authorise "<merchant>" membership card
    And For bos_user I perform GET voucher for loyalty card with authorised for <merchant>
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned |
      | Viator        | 200                  |
