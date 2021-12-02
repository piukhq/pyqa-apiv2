# Created by bularaghavan on 01/12/2021
@membership_cards_transactions @membership_cards
Feature: View transactions
As a Bink user
I want to view my loyalty card transactions in my wallet so that I am aware and have visibility of the transactions that have been concluded with my loyalty card

  @view_loyalty_transactions @bink_regression_api2
  Scenario Outline: Get Loyalty card transactions
    Given I am a Bink user
    When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET request to view loyalty card transactions for "<merchant>" with "<transaction0>" "<transaction1>" and "<transaction3>"
    Then I see a <status_code_returned>
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant      | status_code_returned | transaction0 | transaction1| transaction3|
      | Iceland       | 200                  |  -£50        |  £10        | -£100.01    |
      | Wasabi        | 200                  |  1 stamps    |  1 stamps   | 1 stamps    |


   @transactions_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get loyalty card transactions
     Given I am a Bink user
     When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
     And I perform GET request to view loyalty card transactions for "<merchant>" with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message              | error_slug     |
     |Wasabi  | 401                  | Supplied token is invalid  | INVALID_TOKEN  |

   @transactions_resource_not_found @bink_regression_api2
   Scenario Outline: Verify resource not found scenario for get loyalty card transactions
     Given I am a Bink user
     When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
     And I perform GET request to view loyalty card transactions for "<merchant>" with invalid id "<invalid_id>"
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message                       | error_slug          |invalid_id |
     |Wasabi  | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |1234567    |
