# Created by rupalpatel at 01/10/2021
@membership_card_delete @membership_cards
Feature: Delete a loyalty card
  As a Bink user
  I want to delete a loyalty card from my wallet
  because it is no longer relevant or needed

  @delete_add_and_authorise_loyalty_card @bink_regression_api2 @sandbox_regression
  Scenario Outline: Delete add and authorise
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card
    Then I perform DELETE request to delete the "<merchant>" membership card
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I see a <status_code_returned>

    Examples:
      | merchant | status_code_returned |journey_type|
      | Iceland  | 202                  |delete      |
      | Wasabi   | 202                  |delete      |

  @delete_add_loyalty_card @bink_regression_api2 @sandbox_regression
  Scenario Outline: Delete Add loyalty card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    Then I perform DELETE request to delete the "<merchant>" membership card
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I see a <status_code_returned>

    Examples:
      | merchant | status_code_returned |journey_type|
      | Iceland  | 202                  |delete      |
      | Wasabi   | 202                  |delete      |


  @sending_invalid_token_delete @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for delete journey (Unauthorized with add and auth journey)
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card
#    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Then I perform DELETE request to delete the "<merchant>" membership card with invalid token
    And I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message             | error_slug    |
      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi   | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @sending_invalid_token_for_add_delete @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for delete journey (Unauthorized with add journey)
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
#    Then verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Then I perform DELETE request to delete the "<merchant>" membership card with invalid token
    And I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message             | error_slug    |
      | Iceland  | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi   | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @resource_specified_not_found @bink_regression_api2 @sandbox_regression
  Scenario Outline: Resource specified could not be found in delete journey
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add and authorise "<merchant>" membership card
#    Then I see a <status_code_returned>
#    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    Then I perform DELETE request to delete the "<merchant>" membership card
    When I perform DELETE request to delete the membership card which is already deleted
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | status_code_returned | error_message                       | error_slug         |
      | Iceland  | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND |
      | Wasabi   | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND |

#  @multiple_wallet_delete @bink_regression_api2
#  Scenario Outline: Delete journey in multiple wallet
##    Given I am a Bink user
#    When I perform POST request to add and authorise "<merchant>" membership card
##    Then I see a <status_code_returned>
##    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
#    Then I perform DELETE request to delete the "<merchant>" membership card
#    When I perform DELETE request to delete the membership card which is already deleted
#    Then I see a <status_code_returned>
#    And I see a "<error_message>" error message
#    And I see a "<error_slug>" error slug
#
#    Examples:
#      | merchant | status_code_returned | error_message                       | error_slug         |
#      | Iceland  | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND |
#      | Wasabi   | 404                  | Could not find this account or card | RESOURCE_NOT_FOUND |

  @invalid_field_in_delete_journey @bink_regression_api2 @sandbox_regression
  Scenario Outline: DELETE journey with Unprocessable entity for add membership card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    Then I perform DELETE request with payload for "<merchant>"
    And I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant | error_message             | error_slug             | status_code_returned |
      | Iceland  | Could not validate fields | FIELD_VALIDATION_ERROR | 422                  |
      | Wasabi   | Could not validate fields | FIELD_VALIDATION_ERROR | 422                  |