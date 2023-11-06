# Created by rupalpatel at 06/10/2021
 @membership_cards    @bink_regression_api2

Feature: Add and register a loyalty card
  As a Bink user
  I want to register a ghost loyalty card with the loyalty plan
  so that I can use the Bink functionality with the loyalty card


  Scenario Outline: add and register success in wallet1 then add and register success in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request add_and_register again for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success


    Examples:
      | merchant |
      |The_Works |

  Scenario Outline: add and register failed in wallet1 then add and register success in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to result "<journey_type>" add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>

    Examples:
      | merchant |  scheme_state      | journey_type |
       |The_Works |registration_failed| ghost_card_registration_failed_non_retryable_http_error |


  Scenario Outline: add and register success in wallet1 then add and register failed in wallet2
    Given I am a Lloyds user
    When I perform POST request add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For lloyds_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success
    Given I am a halifax user
    When I perform POST request to result "<journey_type>" add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For halifax_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    Given I am a Lloyds user
    When For lloyds_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with registration_success

    Examples:
      | merchant |  scheme_state      | journey_type |
      |The_Works |registration_failed| ghost_card_registration_failed_non_retryable_http_error |


  Scenario Outline: add and register failed in wallet1 then add and register failed in wallet2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to result "<journey_type>" add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to result "<journey_type>" add and register for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And For bink_user2 I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>
    When For bink_user I perform GET Wallet
    Then Verify Wallet fields for <merchant> with <scheme_state>

    Examples:
      | merchant |  scheme_state      |journey_type |
      |The_Works |registration_failed| ghost_card_registration_failed_non_retryable_http_error|
