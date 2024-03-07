# Created by nehapatil on 26/07/2022
@loyalty_cards_update_failed_join @membership_cards
Feature: Update failed join
  As a Bink user
  I want to update loyalty cards failed to join
  so that I do not have to remove the loyalty card and re-add


  Scenario Outline: Update same loyalty card which failed to join
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform enrol_failed POST request to join "<merchant>" membership card
    And I perform put request with successful_payload to update failed join for <merchant>
    And I perform POST request to add a new "master" payment account to wallet
    And I perform GET Wallet
    Then Verify Wallet fields for <merchant> with join_success

    Examples:
      | merchant      |
      |Viator         |
