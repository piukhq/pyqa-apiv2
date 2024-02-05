# Created by nehapatil on 10/08/2022
 @bink_regression_api2
Feature: View Wallets
  As a Bink user
  I want to view my loyalty cards in each wallet added in different channels
  so that I can see the card status is independent of other wallets


  Scenario Outline: View wallet in different channels when both LCs are authorised
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And For lloyds_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For bink_user I perform GET balance for loyalty card with authorised for <merchant>
    And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET balance for loyalty card with authorised for <merchant>
    And For lloyds_user I perform GET voucher for loyalty card with authorised for <merchant>

    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |



  Scenario Outline: View two wallet of same channel when LCs are authorised in both
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    When I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" to second wallet
    And I perform POST request to add and authorise "<merchant>" membership card with transactions and vouchers
    And For bink_user2 I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET Wallet
    Then I see a <status_code_returned>
    And All Wallet fields are correctly populated for <merchant>
    When For bink_user I perform GET transaction for loyalty card with authorised for <merchant>
    And For bink_user I perform GET balance for loyalty card with authorised for <merchant>
    And For bink_user I perform GET voucher for loyalty card with authorised for <merchant>
    And For bink_user2 I perform GET transaction for loyalty card with authorised for <merchant>
    And For bink_user2 I perform GET balance for loyalty card with authorised for <merchant>
    And For bink_user2 I perform GET voucher for loyalty card with authorised for <merchant>
    Examples:
      | merchant      | status_code_returned|payment_card_provider|
      |Viator        | 200                  |master              |
