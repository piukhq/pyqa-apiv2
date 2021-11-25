# Created by bularaghavan at 16/11/2021
@membership_card_update_email @membership_cards
Feature: Update email feature
  As a Bink user
  I want to update my email address associated with my Bink account
  so that I can continue to use my Bink account with my preferred email address

  @update_new_email @bink_regression_api2
  Scenario Outline: Update to new email success
    Given I am a Bink user
    When I perform POST request to update email
    Then I see a <status_code_returned>
    And I perform POST request to update email again
    Then I see a <status_code_returned>

    Examples:
    | status_code_returned |
    | 200                  |

  @update_email_invalid_token @bink_regression_api2
  Scenario Outline: Email Update with invalid token
     Given I am a Bink user
     When I perform POST request to update email with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     | status_code_returned | error_message             | error_slug    |
     | 401                  | Supplied token is invalid | INVALID_TOKEN |

   @update_email_invalid_request @bink_regression_api2
   Scenario Outline: Email Update with invalid request
      Given I am a Bink user
      When I perform POST request to update email with "<request_payload>" with "<status_code>"
      Then I see a "<error_message>" error message
      And I see a "<error_slug>" error slug

     Examples:
       | error_message             | error_slug             | request_payload | status_code |
       |Could not validate fields | FIELD_VALIDATION_ERROR  | invalid_request  | 422         |


   @update_email_invalid_json @bink_regression_api2
   Scenario Outline: Email Update with Invalid Json
      Given I am a Bink user
      When I perform POST request to update email with "<request_payload>" with "<status_code>"
      Then I see a "<error_message>" error message
      And I see a "<error_slug>" error slug

     Examples:
       | error_message             | error_slug             | request_payload | status_code |
       | Invalid JSON              | MALFORMED_REQUEST       | invalid_json   | 400         |

   @duplicate_email @bink_regression_api2
   Scenario Outline: Email Update with duplicate email
      Given I am a Bink user
      When I perform POST request to update email with "<duplicate_email>"  with "<status_code>"
      Then I see a "<error_message>" error message
      And I see a "<error_slug>" error slug

     Examples:
       | error_message                                 | error_slug             | duplicate_email   | status_code |
       |This email is already in use for this channel  | DUPLICATE_EMAIL        |  space@test.com   | 409        |