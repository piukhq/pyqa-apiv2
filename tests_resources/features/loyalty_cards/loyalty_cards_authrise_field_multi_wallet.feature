# Created by bularagahavan 26/09/2022
 @membership_cards
Feature: Authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  # add loyalty card in wallet 1
  # Authorise lc in wallet 1 with good credentials
  # add loyalty card in wallet 2
  # Authorise lc in wallet 2 with bad credentials
  # Get wallet 1 has authorised details. Also balance vouchers and transactions returned
  # Get wallet 2 has unauthorised details .Also balance vouchers and transactions null
  @bink_regression_api2

  Scenario Outline: PUT with valid cred in wallet 1 and invalid cred in wallet 2
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Then I see a 201
    When I perform PUT request to authorise "<merchant>" wallet only membership card with transactions and vouchers
    Then I see a 202
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    When I add membership card with transactions and vouchers for "<merchant>"
    Then I see a 200
    When I perform PUT request to authorise "<merchant>" membership card with "unauthorised" with "202"
    Then I see a 202
    When For bink_user I perform GET Wallet
    Then All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet_overview
    Then All Wallet_overview fields are correctly populated for <merchant>
    When For bink_user2 I perform GET Wallet
    Then Wallet fields are correctly populated for unauthorised LC of <merchant>
    When For bink_user2 I perform GET Wallet_overview
    Then Wallet_overview fields are correctly populated for unauthorised LC of <merchant>

    Examples:
      | merchant |payment_card_provider |journey_type     |
      | Viator   |master                 |authorise_field |
