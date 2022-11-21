# Created by bularagahavan 26/09/2022
@membership_card_authorise_multi @trusted
Feature: Authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  # add loyalty card in wallet 1
  # Authorise lc in wallet 1 with good credentials
  # add loyalty card in wallet 2
  # Authorise lc in wallet 2 with bad credentials
  # Check the status codes. This might change after TC changes
  # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
  # Get wallet 2 has unauthorised details .Also balance vouchers and transactions null
  @multi_wallet_authorise_1 @sandbox_regression
  Scenario Outline: PUT with good cred in wallet 1 and bad cred in wallet 2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned1>
    When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
    Then I see a <status_code_returned2>
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
#    Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add "<merchant>" membership card with transactions and vouchers
    Then I see a <status_code_returned>
    When I perform PUT request to authorise "<merchant>" membership card with "<request_payload>" with "<status_code_returned2>"
    Then I see a <status_code_returned2>
    When For bink_user I perform GET Wallet
    Then All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For bink_user I perform GET balance for loyalty card with authorised for <merchant>
    And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
    When For bink_user2 I perform GET Wallet
    Then Wallet fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user2 I perform GET Wallet_overview
    Then Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user2 I perform GET transaction for loyalty card with unauthorised for <merchant>
    And For bink_user2 I perform GET balance for loyalty card with unauthorised for <merchant>
    And For bink_user2 I perform GET voucher for loyalty card with unauthorised for <merchant>

    Examples:
      | merchant |payment_card_provider| status_code_returned1 |status_code_returned2|status_code_returned |request_payload|
      | Wasabi   |master               |  201                  |202                  |200                  |unauthorised   |
      | Iceland  |master               | 201                  |202                  |200                  |unauthorised   |

  # add and auth wallet 1 with good credentials
  # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
  # add and auth Wallet 2 with bad credentials
  # Check the status codes. This might change after TC changes
  # Get wallet 2 has unauthorised details .Also balance vouchers and transactions null
  # Then put Wallet 2 with good credentials
  # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
  @multi_wallet_authorise_2 @sandbox_regression
  Scenario Outline: PUT good cred in wallet 2 after good cred in wallet 1 and bad credentials in wallet 2
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
#      Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      When I am in Bink channel to get b2b token for second user
      And I perform POST token request for token type "b2b" to get access token for second user
      And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
      And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code_returned>"
      Then I see a <status_code_returned>
      When For bink_user2 I perform GET Wallet
      Then Wallet fields are correctly populated for unauthorised LC of <merchant>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For bink_user I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user I perform GET Wallet_overview
      Then All Wallet_overview fields are correctly populated for <merchant>
      When For bink_user I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
      When For bink_user2 I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user2 I perform GET Wallet_overview
      Then All Wallet_overview fields are correctly populated for <merchant>
      When For bink_user2 I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant |payment_card_provider| status_code_returned  |request_payload|
      | Wasabi   |master               |  202                  |unauthorised   |
      | Iceland  |master               |  202                  |unauthorised   |

    # add and auth wallet 1 with bad credentials
  # Get wallet 1 has unauthorised details .Also balance vouchers and transactions null
  # add and auth Wallet 2 with bad credentials
  # Get wallet 2 has unauthorised details .Also balance vouchers and transactions null
  # Then put Wallet 2 with good credentials
  # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
  # Get wallet 1 still has unauthorised details .Also balance vouchers and transactions null
  @multi_wallet_authorise_3 @sandbox_regression
  Scenario Outline: PUT good cred in wallet 2 and wallet 1 after bad cred in wallet 1 and wallet 2
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code_returned>"
      Then I see a <status_code_returned>
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
#      Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      When I am in Bink channel to get b2b token for second user
      And I perform POST token request for token type "b2b" to get access token for second user
      And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
      And I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code_returned>"
      Then I see a <status_code_returned>
      When For bink_user2 I perform GET Wallet
      Then Wallet fields are correctly populated for unauthorised LC of <merchant>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For bink_user I perform GET Wallet
      Then Wallet fields are correctly populated for unauthorised LC of <merchant>
      When For bink_user I perform GET Wallet_overview
      Then Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
      When For bink_user I perform GET transaction for loyalty card with unauthorised for <merchant>
      And For bink_user I perform GET balance for loyalty card with unauthorised for <merchant>
      And For bink_user I perform GET voucher for loyalty card with unauthorised for <merchant>
      When For bink_user2 I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user2 I perform GET Wallet_overview
      Then All Wallet_overview fields are correctly populated for <merchant>
      When For bink_user2 I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant |payment_card_provider| status_code_returned  |request_payload|
      | Wasabi   |master               |  202                  |unauthorised   |
      | Iceland  |master               |  202                  |unauthorised   |

    # add and auth wallet 1 with good credentials
    # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
    # add and auth Wallet 2 with good credentials
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
    # Then put Wallet 2 with bad credentials
    # Get wallet 2 has unauthorised details .Also balance vouchers and transactions null
    # Get wallet 1 still has authorised details. Also balance vouchers and transactions returned
  @multi_wallet_authorise_4 @sandbox_regression
  Scenario Outline: PUT bad cred in wallet 2 after good cred in wallet 1 and in wallet 2
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
#      Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      When I am in Bink channel to get b2b token for second user
      And I perform POST token request for token type "b2b" to get access token for second user
      And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
      And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When For bink_user2 I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user2 I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET voucher for loyalty card with authorised for <merchant>
      When I perform PUT request to authorise "<merchant>" membership card with "<request_payload>" with "<status_code_returned>"
      Then I see a <status_code_returned>
      When For bink_user I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user I perform GET Wallet_overview
      Then All Wallet_overview fields are correctly populated for <merchant>
      When For bink_user I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
      When For bink_user2 I perform GET Wallet
      Then Wallet fields are correctly populated for unauthorised LC of <merchant>
      When For bink_user2 I perform GET Wallet_overview
      Then Wallet_overview fields are correctly populated for unauthorised LC of <merchant>
      When For bink_user2 I perform GET transaction for loyalty card with unauthorised for <merchant>
      And For bink_user2 I perform GET balance for loyalty card with unauthorised for <merchant>
      And For bink_user2 I perform GET voucher for loyalty card with unauthorised for <merchant>

    Examples:
      | merchant |payment_card_provider| status_code_returned   |request_payload|
      | Wasabi   |master               |  202                   |unauthorised   |
      | Iceland  |master               |  202                   |unauthorised   |

    # add and auth wallet 1 with Add_Credential_1 and good credentials
    # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
    # add and auth wallet 2 with Add_Credential_1 and good credentials
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
    # Then put wallet 2 with Add_Credential_2 that already exists in wallet 3
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
  @multi_wallet_authorise_5 @sandbox_regression
  Scenario Outline: PUT Add_Credential_2 in wallet 2 after Add_Credential_1 with good cred in wallet 1 and in wallet 2
      Given I am a halifax user
      When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
      Then I see a <status_code_returned>
#      Then verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
      When I am in Bink channel to get b2b token for second user
      And I perform POST token request for token type "b2b" to get access token for second user
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When For bink_user2 I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user2 I perform GET Wallet_overview
      Then All Wallet_overview fields are correctly populated for <merchant>
      When For bink_user2 I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET voucher for loyalty card with authorised for <merchant>


    Examples:
      | merchant |status_code_returned   |payment_card_provider|
      | Wasabi   |202                    |master               |


    # add and auth wallet 1 with Add_Credential_1 and good credentials
    # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
    # add and auth wallet 2 with Add_Credential_1 and good credentials
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
    # Then put wallet 2 with Add_Credential_2 that does not exist in the system
    # Get wallet 2 has authorised details. Also balance vouchers and transactions returned
  @multi_wallet_authorise_6 @sandbox_regression
  Scenario Outline: PUT Add_Credential_2 in wallet 2 after Add_Credential_1 with good cred in wallet 1 and in wallet 2
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
#      And verify the data stored in DB after "add_and_authorise" journey for "<merchant>"
      When I am in Bink channel to get b2b token for second user
      And I perform POST token request for token type "b2b" to get access token for second user
      And I perform POST request to add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
      When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
      Then I see a <status_code_returned>
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      When For bink_user2 I perform GET Wallet
      Then All Wallet fields are correctly populated for <merchant>
      When For bink_user2 I perform GET Wallet_overview
      Then All Wallet_overview fields are correctly populated for <merchant>
      When For bink_user2 I perform GET transaction for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET balance for loyalty card with authorised for <merchant>
      And For bink_user2 I perform GET voucher for loyalty card with authorised for <merchant>


    Examples:
      | merchant |status_code_returned   |payment_card_provider|
      | Wasabi   |202                    |master               |

