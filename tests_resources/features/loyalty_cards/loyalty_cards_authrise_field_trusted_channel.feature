# Created by nehapatil 14/11/2022
@trusted_channel_put_authorise @trusted
Feature: update loyalty card in Trusted channel
  As a Trusted Channel I want to update loyalty card
  so that the scheme account is updated and pll is updated for the wallet



  @put_manual_credential_tc
  Scenario Outline: PUT Add_Credential_2 in tc wallet after Add_Credential_1 in tc wallet and Add_Credential_2 exists in another wallet
      Given I am a halifax user
      When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a <status_code_returned>
#      Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a <status_code_returned>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For squaremeal_user I perform GET Wallet
      Then Loyalty_card2 Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant   |status_code_returned   |
      | SquareMeal | 202                   |


  @put_manual_credential_tc
  Scenario Outline: PUT Add_Credential_2 in tc wallet after Add_Credential_1 in tc wallet and Add_Credential_2 does not exist in any other wallet
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a <status_code_returned>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For squaremeal_user I perform GET Wallet
      Then Loyalty_card2 Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant     |status_code_returned |
      | SquareMeal   |202                  |



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
#      Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a <status_code_returned>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For squaremeal_user I perform GET Wallet
      Then Loyalty_card2 Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant   |status_code_returned   |
      | SquareMeal |202                    |



  @put_manual_credential_tc
  Scenario Outline: PUT Add_Credential_2 in wallet 2 after Add_Credential_1 in wallet 1 and in wallet 2 and Add_Credential_2 does not exist in any other wallet
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
#      And verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      Given I am a squaremeal user
      When I perform POST request to add trusted channel "<merchant>" loyalty card
      Then I see a <status_code_returned>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For squaremeal_user I perform GET Wallet
      Then Loyalty_card2 Wallet fields are correctly populated for <merchant>

    Examples:
      | merchant     |status_code_returned   |
      | SquareMeal   |202                    |

