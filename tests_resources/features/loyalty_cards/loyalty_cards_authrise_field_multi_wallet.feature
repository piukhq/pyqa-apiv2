# Created by rupalpatel at 04/10/2021, updated by BR on 29/07/2022
@membership_card_authorise_multi
Feature: Authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @multi_wallet_authorise_field @sandbox_regression
  Scenario Outline: Authorise multi wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned1>
    When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
    Then I see a <status_code_returned2>
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned3>
    When I perform PUT request to authorise "<merchant>" membership card with "<request_payload>" with "<status_code_returned2>"
    Then I see a <status_code_returned2>
    When I perform GET 'Wallet' for first user
    Then All Wallet fields are correctly populated for <merchant>
    When I perform GET request to view loyalty card transactions for "<merchant>"
    And I perform GET request to view loyalty card balance for "<merchant>"
    And I perform GET request to view loyalty card voucher for "<merchant>"
    When I perform GET 'Wallet' for second user
    Then Wallet fields are correctly populated for unauthorised LC of <merchant>

    Examples:
      | merchant |payment_card_provider| journey_type    |status_code_returned1 |status_code_returned2|status_code_returned3|request_payload|
      | Wasabi   |master               | authorise_field | 201                  |202                  |200                  |unauthorised   |

