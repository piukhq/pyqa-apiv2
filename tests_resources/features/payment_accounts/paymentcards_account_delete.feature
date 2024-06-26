# Created by rupalpatel at 26/08/2021
@paymentcard_account_delete @paymentcard_account
Feature: As a Bink User
  I want to be able to delete my payment card account to my bink wallet
  So that I can start verify its deleted from my wallet

  @sit
  Scenario Outline: Delete new payment card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
#    GET is not implemented
#    And I perform the GET request to verify the new payment card "<payment_card_provider>" has been added successfully to the wallet
    Then I verify the paymentcard "<payment_card_provider>" been added into my wallet
    And I perform DELETE request to delete "<payment_card_provider>" the payment card
    And I see the paymentcard been deleted and status_code "<status_code>" appeared

    Examples:
      | payment_card_provider | status_code |
      | master                | 202         |
      | amex                  | 202         |
      | visa                  | 202         |

   Scenario Outline: Delete payment card which is already deleted from the wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    Then I verify the paymentcard "<payment_card_provider>" been added into my wallet
    And I perform DELETE request to delete "<payment_card_provider>" the payment card
    And I see the paymentcard been deleted and status_code "<status_code>" appeared
    And I perform DELETE request to delete the payment card which is already deleted
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code | status_code_returned | error_message                       | error_slug |
      | master                | 202         | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |
      | amex                  | 202         | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |
      | visa                  | 202         | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND  |


  Scenario Outline: Client does not have valid token
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    Then I perform DELETE request to delete "<payment_card_provider>" the payment card with invalid token
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code_returned | error_message                                        | error_slug    |
      | master                | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |
      | amex                  | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |
      | visa                  | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |
