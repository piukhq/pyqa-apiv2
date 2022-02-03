# Created by bularaghavan on 01/12/2021
@membership_cards_vouchers @membership_cards
Feature: View Vouchers
As a Bink user I want to view my loyalty card vouchers in my wallet
so that I am aware and have visibility of the vouchers that have been concluded with my loyalty card

  @view_loyalty_vouchers @bink_regression_api2
  Scenario Outline: Get Loyalty card vouchers
    Given I am a Bink user
    When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET request to view loyalty card vouchers for "<merchant>" with "<state>", "<progress_display_text>", "<current_value>", "<target_value>" "<suffix>" and "<barcode_type>"
    Then I see a <status_code_returned>
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | merchant      | status_code_returned |state       |progress_display_text | current_value |target_value|suffix|barcode_type|
      | Wasabi        | 200                  |inprogress  |4/7 stamps           |  4            | 7          |stamps | 0          |

   @vouchers_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get loyalty card vouchers
     Given I am a Bink user
     When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
     And I perform GET request to view loyalty card vouchers for "<merchant>" with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message              | error_slug     |
     |Wasabi  | 401                  | Supplied token is invalid  | INVALID_TOKEN  |

   @vouchers_resource_not_found @bink_regression_api2
   Scenario Outline: Verify resource not found scenario for get loyalty card vouchers
     Given I am a Bink user
     When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
     And I perform GET request to view loyalty card vouchers for "<merchant>" with invalid id "<invalid_id>"
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     |merchant| status_code_returned | error_message                       | error_slug          |invalid_id |
     |Wasabi  | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |1234567    |

