# Created by bularaghavan at 05/10/2021
@membership_card_register @membership_cards  @bink_regression_api2
Feature: Register a loyalty card
  As a Bink user
  I want to add registration credentials to an existing Store card,
  so that I can register the loyalty card with the merchant and enable the Bink functionality on the loyalty card

  Scenario Outline: Register field journey only
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | status_code_returned | journey_type   |
      | The_Works  | 202                  | register_field |


  Scenario Outline: verify PLL for update register
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    And I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant | status_code_returned | journey_type |
      | master                | The_Works  | 202                  | pll_active   |

  Scenario Outline: Add existing card again into different wallet via put register
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add "<merchant>" membership card already registered
    Then I see a 200
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a <status_code_returned>
    When For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success


    Examples:
      | merchant | status_code_returned |
      |The_Works | 202                   |


  Scenario Outline: Wallet1 add then register valid, wallet2 add then register same card with invalid details
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before registration_success register
    Then I see a 201
    When I perform PUT request to register <merchant> with registration_success membership card
    Then I see a 202
    Given I am a halifax user
    When I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add <merchant> membership card before <scheme_state> register
    Then I see a 200
    When I perform PUT request to register <merchant> with <scheme_state> membership card
    Then I see a 202
    When For halifax_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_failed
    Given I am a Lloyds user
    When For lloyds_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success


    Examples:
      | merchant | scheme_state      |
      |The_Works | registration_failed |
