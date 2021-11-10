# Created by rupalpatel at 10/11/2021
@membership_card_remove_failed_join @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to join a loyalty scheme
  so that I can use the Bink functionality with the relevant loyalty plan

  @delete_fail_scheme @bink_regression_api2
  Scenario Outline: Remove a failed join request from the wallet
    Given I am a Bink user
    When I perform fail POST request to join "<merchant>" membership card
    And I perform DELETE request to delete the "<scheme_state>" membership card for "<merchant>"
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Examples:
      | merchant      | status_code_returned | journey_type | scheme_state |
      | Iceland       | 200                  | join_failed  | fail         |
      | Wasabi        | 200                  | join_failed  | fail         |
      | HarveyNichols | 200                  | join_failed  | fail         |

  @remove_active_scheme @bink_regression_api2
  Scenario Outline: Remove active scheme from the wallet
    Given I am a Bink user
    When I perform POST request to join "<merchant>" membership card
    And I perform DELETE request to delete the "<scheme_state>" membership card for "<merchant>"
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I perform DELETE request to delete the "<merchant>" membership card
    Examples:
      | merchant      | status_code_returned | journey_type | scheme_state | error_message                               | error_slug |
      | Iceland       | 409                  | join         | active       | Could not process request due to a conflict | CONFLICT   |
      | Wasabi        | 409                  | join         | active       | Could not process request due to a conflict | CONFLICT   |
      | HarveyNichols | 409                  | join         | active       | Could not process request due to a conflict | CONFLICT   |

#  @remove_join_in_progress_scheme @bink_regression_api2
#  Scenario Outline: Remove join in progress scheme from the wallet
#    Given I am a Bink user
#    When I perform POST request to join in progress "<merchant>" membership card
#    And I perform DELETE request to delete the "<scheme_state>" membership card for "<merchant>"
#    Then I see a <status_code_returned>
#    And I see a "<error_message>" error message
#    And I see a "<error_slug>" error slug
#    And I wait 10 second to get scheme active
#    And I perform DELETE request to delete the "<merchant>" membership card
#    Examples:
#      | merchant      | status_code_returned | scheme_state | error_message                                                       | error_slug       |
#      | Iceland       | 409                  | active       | Loyalty card cannot be deleted until the Join process has completed | JOIN_IN_PROGRESS |

  @invalid_token_fail_join @bink_regression_api2
  Scenario Outline: Sending invalid token with bearer prefix in header for join journey (Unauthorized) and delete the fail scheme
    Given I am a Bink user
    When I perform fail POST request to join "<merchant>" membership card
    And I perform DELETE request to delete the membership card for "<merchant>" with invalid token
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    Examples:
      | merchant      | status_code_returned | error_message             | error_slug    |
      | Iceland       | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi        | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | HarveyNichols | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @delete_fail_scheme_again @bink_regression_api2
  Scenario Outline: Delete failed scheme again when scheme already deleted from the wallet
    Given I am a Bink user
    When I perform fail POST request to join "<merchant>" membership card
    And I perform DELETE request to delete the "<scheme_state>" membership card for "<merchant>"
    When I perform DELETE request to delete the failed membership card which is already deleted
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug
    Examples:
      | merchant      | status_code_returned | scheme_state | error_message                       | error_slug         |
      | Iceland       | 404                  | fail         | Could not find this account or card | RESOURCE_NOT_FOUND |
      | Wasabi        | 404                  | fail         | Could not find this account or card | RESOURCE_NOT_FOUND |
      | HarveyNichols | 404                  | fail         | Could not find this account or card | RESOURCE_NOT_FOUND |