# Created by nehapatil on 26/07/2022
@loyalty_cards_update_failed_join @membership_cards
Feature: Update failed join
  As a Bink user
  I want to update loyalty cards failed to join
  so that I do not have to remove the loyalty card and re-add


   @update_failed_join_loyalty_card @bink_regression_api2
  Scenario Outline: Update same loyalty card which failed to join
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform enrol_failed POST request to join "<merchant>" membership card
    And I perform put request with successful_payload to update failed join for <merchant>
    When I perform GET 'Wallet'
    Then Verify 'Wallet' fields for <merchant> with join_success

    Examples:
      | merchant      |
      |Iceland        |



  @update_failed_join_invalid @bink_regression_api2
  Scenario Outline: Verify invalid request payload scenarios
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform asynchronous_join_in_progress POST request to join "<merchant>" membership card
    And I perform put request with <request_payload> to update failed join for <merchant>
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | status_code_returned| error_message                     |error_slug        |merchant| request_payload|
      |401                  |Supplied token is invalid          |INVALID_TOKEN     |Iceland  | invalid_token  |
      |404                  |Could not find this account or card|RESOURCE_NOT_FOUND|Iceland  |invalid_scheme_account_id|
      |400                  |Invalid JSON                       |MALFORMED_REQUEST |Iceland  |invalid_json |
      |422                  |Could not validate fields          |FIELD_VALIDATION_ERROR|Iceland  |invalid_request|
      |409                  |The Join cannot be updated while it is in Progress.|JOIN_IN_PROGRESS| Iceland |conflict|
