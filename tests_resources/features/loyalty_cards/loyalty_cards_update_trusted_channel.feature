# Created by nehapatil 14/11/2022
@bink_regression_api2
Feature: update loyalty card in Trusted channel
  As a Trusted Channel I want to update loyalty card
  so that the scheme account is updated and pll is updated for the wallet

  Scenario Outline: PUT Add_Credential_2 in tc wallet after Add_Credential_1 in tc wallet and Add_Credential_2 exists in another wallet
      Given I am a halifax user
      When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a 202
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a 201
      When I perform put request with successful_payload to update trusted_add for <merchant>
      Then I see a 201
      When For squaremeal_user I perform GET Wallet
      Then Wallet fields are correctly populated for <merchant> when lc_in_non_tc
      When For squaremeal_user I perform GET Wallet_overview
      Then Wallet_overview fields are correctly populated for <merchant> when lc_in_non_tc
      When For squaremeal_user I perform GET Wallet_by_card_id
      Then Wallet_by_card_id fields are correctly populated for <merchant> when lc_in_non_tc

    Examples:
      | merchant   |
      | SquareMeal |


  Scenario Outline: Update merchant_identifier in TC wallet
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a 201
      When I perform put request with new_merchant_id to update trusted_add for <merchant>
      Then I see a 201
      When For squaremeal_user I perform GET Wallet
      Then Wallet fields are correctly populated for <merchant> when lc_in_only_tc
      When For squaremeal_user I perform GET Wallet_overview
      Then Wallet_overview fields are correctly populated for <merchant> when lc_in_only_tc
      When For squaremeal_user I perform GET Wallet_by_card_id
      Then Wallet_by_card_id fields are correctly populated for <merchant> when lc_in_only_tc


    Examples:
      | merchant     |
      | SquareMeal   |

  Scenario Outline: PUT Add_Credential_2 in wallet 2 after Add_Credential_1 in wallet 1 and in wallet 2 and Add_Credential_2 exists in another wallet
      Given I am a halifax user
      When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a 202
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a 202
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a 201
      When I perform put request with successful_payload to update trusted_add for <merchant>
      Then I see a 201
      When For squaremeal_user I perform GET Wallet
      Then Wallet fields are correctly populated for <merchant> when lc_in_non_tc
      When For squaremeal_user I perform GET Wallet_overview
      Then Wallet_overview fields are correctly populated for <merchant> when lc_in_non_tc
      When For squaremeal_user I perform GET Wallet_by_card_id
      Then Wallet_by_card_id fields are correctly populated for <merchant> when lc_in_non_tc

    Examples:
      | merchant   |
      | SquareMeal |


  Scenario Outline: PUT Add_Credential_2 in TC wallet after Add_Credential_1 in wallet 1 and in wallet 2 and Add_Credential_2 does not exist in any other wallet
      Given I am a halifax user
      When I perform POST request to add and authorise "<merchant>" membership card
      Then I see a 202
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a 201
      When I perform put request with successful_payload to update trusted_add for <merchant>
      Then I see a 201
      When For squaremeal_user I perform GET Wallet
      Then Wallet fields are correctly populated for <merchant> when lc_in_only_tc
      When For squaremeal_user I perform GET Wallet_overview
      Then Wallet_overview fields are correctly populated for <merchant> when lc_in_only_tc
      When For squaremeal_user I perform GET Wallet_by_card_id
      Then Wallet_by_card_id fields are correctly populated for <merchant> when lc_in_only_tc

    Examples:
      | merchant     |
      | SquareMeal   |


  Scenario Outline: Verify conflict when email is updated and email is already linked with other card and merchant id
    Given I am a halifax user
    When I perform POST request to add and authorise "SquareMeal" membership card with transactions and vouchers
    Then I see a 202
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "SquareMeal" loyalty card
    Then I see a 201
    When I perform put request with <request_payload> to update trusted_add for SquareMeal
    Then I see a 409

    Examples:
   | request_payload|
   |update_email|
   |conflict|



    Scenario Outline: Verify email is updated successfully in trusted channel
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a <status_code_returned>
    When I perform put request with <request_payload> to update trusted_add for <merchant>
    Then I see a <status_code_returned>

      Examples:
      |status_code_returned|merchant|request_payload|
      |201                 |SquareMeal|update_email |
