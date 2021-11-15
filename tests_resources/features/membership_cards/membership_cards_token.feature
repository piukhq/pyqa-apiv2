# Created by
@get_token @membership_cards
Feature: Get Token
  As a Qa Engineer
  I want to automate POST /token endpoint
  so that I can include the tests in the regression test suite and also include the new tokens for existing test scripts.

  @token_success
  Scenario Outline: Verify success for post token
    Given I have token set up correctly
    When I perform POST token request for "<token_type>"
    Then I see a <status_code_returned>
    And I can see a valid access token and refresh token in the response

    Examples:
    | status_code_returned |token_type    |
    | 200                  |b2b           |
    | 200                  |refresh_token |

  @invalid_json_token
  Scenario Outline: Post token with invalid json
    Given I have token set up correctly
    And I perform POST token request for "<token_type>" with "<request_payload>" and "<status_code>"
    Then I see a "<status_code_returned>"
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

   Examples:
   |token_type     | error_message    |    error_slug     | request_payload | status_code_returned |
   | b2b           | Invalid JSON      | MALFORMED_REQUEST | invalid_json   | 400                  |
   | refresh_token | Invalid JSON      | MALFORMED_REQUEST | invalid_json   | 400                  |


  @invalid_json_token
  Scenario Outline: Post token with invalid json
    Given I have token set up correctly
    And I perform POST token request for "<token_type>" with  invalid token and bearer prefix
    Then I see a "<status_code_returned>"
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

   Examples:
   |token_type     | error_message                  | error_slug     | status_code_returned |
   | b2b           | Supplied token is invalid      | INVALID_TOKEN  | 401                  |
   | refresh_token | Supplied token is invalid      | INVALID_TOKEN  | 401                  |






