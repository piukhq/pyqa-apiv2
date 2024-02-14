# Created by bularaghavan on 01/12/2021
@bink_regression_api2 @membership_cards
Feature: View transactions
As a Bink user
I want to view my loyalty card transactions in my wallet so that I am aware and have visibility of the transactions that have been concluded with my loyalty card

  Scenario Outline: Get Loyalty card transactions
    Given I am a bos user
    When I add and authorise "<merchant>" membership card with transactions and vouchers
    And As a bos_user I performed  GET transaction for authorised <merchant> membership card
    Then I see a 200
    Examples:
      | merchant      |
      | Viator        |
