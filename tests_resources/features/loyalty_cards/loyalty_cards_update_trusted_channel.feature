# Created by nehapatil 14/11/2022
@trusted_channel_put_authorise @trusted @bink_regression_api2 @actual_tc
Feature: update loyalty card in Trusted channel
  As a Trusted Channel I want to update loyalty card
  so that the scheme account is updated and pll is updated for the wallet

  @put_manual_credential_tc
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


  @put_manual_credential_tc
  Scenario Outline: PUT Add_Credential_2 in tc wallet after Add_Credential_1 in tc wallet and Add_Credential_2 does not exist in any other wallet
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


      @update_merchant_identifier_tc
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


    # add and auth wallet 1 with Add_Credential_1 and good credentials
    # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
    # add and auth wallet 2 with Add_Credential_1 and good credentials
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
    # Then put wallet 2 with Add_Credential_2 that already exists in wallet 3
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
  @put_manual_credential_tc
  Scenario Outline: PUT Add_Credential_2 in wallet 2 after Add_Credential_1 in wallet 1 and in wallet 2 and Add_Credential_2 exists in another wallet
      Given I am a halifax user
      When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a <status_code_returned>
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
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
      | merchant   |status_code_returned   |
      | SquareMeal |202                    |



  @put_manual_credential_tc @fix
  Scenario Outline: PUT Add_Credential_2 in TC wallet after Add_Credential_1 in wallet 1 and in wallet 2 and Add_Credential_2 does not exist in any other wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
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
      | merchant     |status_code_returned   |
      | SquareMeal   |202                    |


  @put_tc_invalid @invalid
  Scenario Outline: Verify invalid request payload scenarios
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When I perform put request with <request_payload> to update trusted_add for <merchant>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | status_code_returned| error_message                     |error_slug        |merchant| request_payload|
      |401                  |Supplied token is invalid          |INVALID_TOKEN     |SquareMeal  | invalid_token  |
      |404                  |Could not find this account or card|RESOURCE_NOT_FOUND|SquareMeal  |invalid_scheme_account_id|
#      |400                  |Invalid JSON                       |MALFORMED_REQUEST |SquareMeal  |invalid_json |
      |422                  |Could not validate fields          |FIELD_VALIDATION_ERROR|SquareMeal  |invalid_request|



  @put_tc_conflict @invalid
  Scenario Outline: Verify conflict request payload
    Given I am a halifax user
    When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    Then I see a 202
    Given I am a squaremeal user
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When I perform put request with <request_payload> to update trusted_add for <merchant>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      |status_code_returned| error_message                     |error_slug        |merchant| request_payload|
      |409                  |A loyalty card with this account_id has already been added in a wallet, but the key credential does not match.|CONFLICT| SquareMeal |conflict|