# Created by nehapatil at 10/11/2022
@trusted_channel_delete @trusted @bink_regression_api2 @actual_tc
Feature: delete loyalty card and delete payment card from Trusted channel
  As a Trusted Channel I want to delete loyalty card and delete payment card
  so that the card is deleted and pll is updated for the wallet


  @delete_loyalty_card_tc
  Scenario Outline: Delete loyalty card from Trusted channel wallet
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I perform DELETE request to delete the "<merchant>" membership card
#    And verify that for squaremeal_user data stored in after "delete" journey for "<merchant>"
    And I see a <status_code_returned>
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    And verify loyalty_card is deleted from the wallet

    Examples:
      | merchant      | status_code_returned |payment_card_provider |
      | SquareMeal    | 202                  |master               |


    @delete_payment_card_tc
  Scenario Outline: Delete payment card from Trusted channel wallet
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I perform DELETE request to delete "<payment_card_provider>" the payment card
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    And verify payment_card is deleted from the wallet

    Examples:
      | merchant      |payment_card_provider|
      | SquareMeal    |master               |


  @delete_lc_tc
  Scenario Outline: Delete loyalty card from Trusted channel wallet which already exists in Non trusted channel
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
#    When For squaremeal_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>
    Then I perform DELETE request to delete the "<merchant>" membership card
    And I see a <status_code_returned>
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    And verify loyalty_card is deleted from the wallet
#    When For halifax_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned |payment_card_provider |
      | SquareMeal    | 202                   |master               |

@delete_lc_ntc
  Scenario Outline: Delete loyalty card from non Trusted channel wallet which already exists in trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
#    When For lloyds_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>
    Then I perform DELETE request to delete the "<merchant>" membership card
    And I see a <status_code_returned>
    When For lloyds_user I perform GET Wallet
    Then I see a 200
    And verify loyalty_card is deleted from the wallet
#    When For squaremeal_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned | payment_card_provider |
      | SquareMeal    | 202                  | master               |


  @delete_pc_tc
  Scenario Outline: Delete payment card from Trusted channel wallet which already exists in Non trusted channel
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
#    When For squaremeal_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>
    And I perform DELETE request to delete "<payment_card_provider>" the payment card
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    And verify payment_card is deleted from the wallet
#    When For halifax_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned |payment_card_provider |
      | SquareMeal    | 202                   |master               |

@delete_pc_ntc
  Scenario Outline: Delete payment card from non Trusted channel wallet which already exists in trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
#    When For lloyds_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>
    And I perform DELETE request to delete "<payment_card_provider>" the payment card
    When For lloyds_user I perform GET Wallet
    Then I see a 200
    And verify payment_card is deleted from the wallet
#    When For squaremeal_user I perform GET Wallet
#    Then I see a 200
#    And All Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned | payment_card_provider |
      | SquareMeal    | 202                  | master               |
