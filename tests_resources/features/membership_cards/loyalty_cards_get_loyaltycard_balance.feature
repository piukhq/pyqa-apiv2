# Created by bularaghavan on 25/11/2021
@membership_cards_balance @membership_cards
Feature: View balance
As a Bink user
I want to view my loyalty card balances in my wallet
so that I am aware and have visibility of my rewards

  @view_loyalty_balance @bink_regression_api2
  Scenario Outline: Get Loyalty card balance
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET request to view loyalty card balance for "<merchant>"
    Then I see a <status_code_returned>
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant      | status_code_returned |
      | Iceland       | 200                  |
      | Wasabi        | 200                  |

   @balance_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get loyalty card balance
     Given I am in Bink channel to get b2b token
     When I perform POST token request for token type "b2b" to get access token
     And I perform POST request to add and authorise "<merchant>" membership card
     And I perform GET request to view loyalty card balance for "<merchant>" with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message              | error_slug     |
     |Wasabi  | 401                  | Supplied token is invalid  | INVALID_TOKEN  |

   @resource_not_found_balance @bink_regression_api2
   Scenario Outline: Verify resource not found scenario for get loyalty card balance
     Given I am in Bink channel to get b2b token
     When I perform POST token request for token type "b2b" to get access token
     And I perform POST request to add and authorise "<merchant>" membership card
     And I perform GET request to view loyalty card balance with invalid id "<invalid_id>" for "<merchant>"
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message                       | error_slug          |invalid_id |
     |Wasabi  | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |1234567    |
