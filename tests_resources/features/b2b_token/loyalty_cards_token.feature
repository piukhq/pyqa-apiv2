@b2b_token
Feature: Get B2b token
  As an authenticated API Client
  I want exchange a refresh token for a new access and refresh token
  so that I can continue using Bink API v2 without needing to re-authenticate.

  @bink_regression_api2 @post_b2b_token @token
  Scenario: Verify post token with grand type and scope
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    Then I see a 200

  @bink_regression_api2 @b2b_token_refresh_token @token
  Scenario: Verify access via refresh token for post token
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST refresh token with grant type "refresh_token"
    Then I see a 200

  @bink_regression_api2 @b2b_token_refresh_token @token
  Scenario: Verify access via refresh token for post token with invalid grant type
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST refresh token with grant type "refresh_token"
    And I perform POST request for token with "unsupported_grant_type"
    Then I see a 400
    And I see a "unsupported_grant_type" error message

  @bink_regression_api2 @unsupported_grant_type @token
  Scenario: Post token with invalid grant type
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request for token with "unsupported_grant_type"
    Then I see a 400
    And I see a "unsupported_grant_type" error message

  @bink_regression_api2 @invalid_request_token @token
  Scenario: Post token with invalid json
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request for token with "invalid_request"
    Then I see a 400
    And I see a "invalid_request" error message

  @bink_regression_api2 @invalid_client_token @token
  Scenario: Post token with invalid client
    Given I am a Bink user
    When I perform POST request for token with "invalid_client"
    Then I see a 400
    And I see a "unauthorized_client" error message
