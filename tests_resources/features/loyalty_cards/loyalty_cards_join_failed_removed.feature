# Created by rupalpatel at 10/11/2021
@membership_card_remove_failed_join @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to join a loyalty scheme
  so that I can use the Bink functionality with the relevant loyalty plan

  @delete_fail_scheme @bink_regression_api2
  Scenario Outline: Remove a failed join request from the wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform <scheme_state> POST request to join "<merchant>" membership card
    Then verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"
    When I perform DELETE request to delete the "<scheme_state>" membership card for "<merchant>"
    Then I see a <status_code_returned>

    Examples:
      | merchant      | status_code_returned | journey_type | scheme_state |
      | Viator       | 200                  | join_failed  | enrol_failed         |
