# Created by bularaghavan at 31/10/2022
@bink_regression_api2 @membership_cards
Feature: Add and authorise a loyalty card into Trusted channel
  As a Trusted Channel I want to add a loyalty card into my user’s wallet, without needing to provide sensitive credential information
  so that I do not need to expose sensitive credential data within my system, and
  I can then link my user’s payment cards to their loyalty card, so my users can use PLL.


  Scenario Outline: Trusted channel adds loyalty card into wallet
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    Then Wallet fields are correctly populated for <merchant> when lc_in_only_tc
    When For squaremeal_user I perform GET Wallet_overview
    Then I see a 200
    Then Wallet_overview fields are correctly populated for <merchant> when lc_in_only_tc
    When For squaremeal_user I perform GET Wallet_by_card_id
    Then I see a 200
    Then Wallet_by_card_id fields are correctly populated for <merchant> when lc_in_only_tc

    Examples:
      | merchant      |journey_type      |
      | SquareMeal    | add_and_authorise|

   # card number missing https://hellobink.atlassian.net/browse/WAL-2853
  Scenario Outline: Trusted channel adds loyalty card into wallet which already exists in Non trusted channel
    Given I am a halifax user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I add and authorise "<merchant>" membership card
    Then I see a 202
    And verify that for halifax_user data stored in after "<journey_type>" journey for "<merchant>"
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"
    When For squaremeal_user I perform GET Wallet
    Then I see a 200
    And All Wallet fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_overview
    Then I see a 200
    And All Wallet_overview fields are correctly populated for <merchant>
    When For squaremeal_user I perform GET Wallet_by_card_id
    Then I see a 200
    And All Wallet_by_card_id fields are correctly populated for <merchant>

    Examples:
      | merchant      | journey_type      |payment_card_provider|
      | SquareMeal    | add_and_authorise |master               |

  # bug https://hellobink.atlassian.net/browse/WAL-2853
  Scenario Outline: Non Trusted channel adds loyalty card into wallet which already exists in Trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    # And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    # And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"
    When For lloyds_user I perform GET Wallet
    Then I see a 200
    And All Wallet fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_overview
    Then I see a 200
    And All Wallet_overview fields are correctly populated for <merchant>
    When For lloyds_user I perform GET Wallet_by_card_id
    Then I see a 200
    And All Wallet_by_card_id fields are correctly populated for <merchant>

    Examples:
      | merchant      | status_code_returned | journey_type      |payment_card_provider|
      | SquareMeal    | 202                  | add_and_authorise |master               |


  Scenario Outline: verify PLL for add card in trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    And verify that for squaremeal_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant   | status_code_returned | journey_type |
      | master                | SquareMeal | 201                  | pll_active   |
