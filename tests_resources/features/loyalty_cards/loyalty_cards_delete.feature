# Created by rupalpatel at 01/10/2021
@bink_regression_api2 @membership_cards
Feature: Delete a loyalty card
  As a Bink user
  I want to delete a loyalty card from my wallet
  because it is no longer relevant or needed

  Scenario Outline: Delete add and authorise
    Given I am a bos user
    When I add and authorise "<merchant>" membership card
    Then I perform DELETE request to delete the "<merchant>" membership card
    And verify that for bos_user data stored in after <journey_type> journey for "<merchant>"
    And I see a <status_code_returned>

    Examples:
      | merchant | status_code_returned |journey_type|
      | The_Works   | 202                  | delete       |

  Scenario Outline: Delete Add loyalty card
    Given I am a bos user
    When I perform POST request to add "<merchant>" membership card
    Then I perform DELETE request to delete the "<merchant>" membership card
    And verify that for bos_user data stored in after <journey_type> journey for "<merchant>"
    And I see a <status_code_returned>

    Examples:
      | merchant    | status_code_returned | journey_type |
      | The_Works   | 202                  | delete       |


  Scenario Outline: Add and auth lc in two wallets and delete the card from one wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I add and authorise "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned>
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    Then verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add and authorise "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned>
    When For bink_user I perform GET Wallet
    Then All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_by_card_id
    Then All Wallet_by_card_id fields are correctly populated for <merchant>
    When For bink_user2 I perform GET Wallet
    Then All Wallet fields are correctly populated for <merchant>
    When For bink_user2 I perform GET Wallet_overview
    Then All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user2 I perform GET Wallet_by_card_id
    Then All Wallet_by_card_id fields are correctly populated for <merchant>
    And I perform DELETE request to delete the "<merchant>" membership card
    And I see a <status_code_returned>
    When For bink_user I perform GET Wallet
    Then All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_by_card_id
    Then All Wallet_by_card_id fields are correctly populated for <merchant>

    Examples:
      | merchant | payment_card_provider | journey_type    | status_code_returned |
      | The_Works   | master                | authorise_field | 202                  |
