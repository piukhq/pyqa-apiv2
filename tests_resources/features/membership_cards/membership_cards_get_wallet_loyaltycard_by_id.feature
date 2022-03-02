# Created by nehapatil on 22/02/2022
@membership_cards_by_id @membership_cards
Feature: View Wallet by loyalty card id
  As a Bink user
  I want to view details of single loyalty cards
  so t do not have to call multiple different endpoints



   @view_loyaltycard_by_id @bink_regression_api2
  Scenario Outline: View loyalty card by id
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET 'Wallet_by_card_id'
    Then I see a <status_code_returned>
    And All 'Wallet_by_card_id' fields are correctly populated for <merchant>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      | Wasabi        | 200                 |master               |
      |Iceland        |200                  |master               |
      |HarveyNichols  |200                  |master               |


  @wallet_loyaltycard_by_id_invalid @bink_regression_api2
  Scenario Outline: Verify invalid token scenario for get Wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform GET request to view 'Wallet_by_card_id' with <invalid>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    And I perform DELETE request to delete the "<merchant>" membership card

    Examples:
      | status_code_returned| error_message                      |error_slug        |merchant| invalid|
      | 401                  | Supplied token is invalid         |INVALID_TOKEN     |Wasabi  | token  |
      |404                   |Could not find this account or card|RESOURCE_NOT_FOUND|Wasabi  |scheme_account_id|
