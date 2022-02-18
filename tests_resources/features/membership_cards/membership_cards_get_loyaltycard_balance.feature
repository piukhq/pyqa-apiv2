# Created by bularaghavan on 25/11/2021
@membership_cards_balance @membership_cards
Feature: View balance
As a Bink user
I want to view my loyalty card balances in my wallet
so that I am aware and have visibility of my rewards

  @view_loyalty_balance @bink_regression_api2
  Scenario Outline: Get Loyalty card balance
    Given I am a Bink user
    When I perform POST request to add and authorise "<merchant>" membership card
    And I perform GET request to view loyalty card balance for "<merchant>" with "<balance>"
    Then I see a <status_code_returned>
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant      | status_code_returned | balance  |
      | Iceland       | 200                  | £123456  |
      | Wasabi        | 200                  | 5 stamps |

   @balance_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get loyalty card balance
     Given I am a Bink user
     When I perform POST request to add and authorise "<merchant>" membership card
     And I perform GET request to view loyalty card balance for "<merchant>" with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message              | error_slug     |
     |Wasabi  | 401                  | Supplied token is invalid  | INVALID_TOKEN  |

   @resource_not_found @bink_regression_api2
   Scenario Outline: Verify resource not found scenario for get loyalty card balance
     Given I am a Bink user
     When I perform POST request to add and authorise "<merchant>" membership card
     And I perform GET request to view loyalty card balance for "<merchant>" with invalid id "<invalid_id>"
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message                       | error_slug          |invalid_id |
     |Wasabi  | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |1234567    |
