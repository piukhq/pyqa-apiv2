# Created by bularaghavan at 17/01/2022
@delete_user @membership_cards
Feature: Delete User feature
  As a Bink ‘B2B’ user
  I want to delete my Bink account because I no longer wish to be enrolled in the service

  @delete_user_success @bink_regression_api2
  Scenario: Delete User success
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    Then I perform DELETE request to delete user successfully


   @delete_user_invalid_token @bink_regression_api2
   Scenario Outline: Delete User with invalid token
   Given I am in Bink channel to get b2b token
   When I perform DELETE request to delete user with invalid token
   Then I see a <status_code_returned>
   And I see a "<error_message>" error message
   And I see a "<error_slug>" error slug

   Examples:
   | status_code_returned | error_message             | error_slug    |
   | 401                  | Supplied token is invalid | INVALID_TOKEN |


    @delete_scheme_account_pll_links @bink_regression_api2
    Scenario Outline: soft delete pll links
      Given I am in Bink channel to get b2b token
      When I perform POST token request for token type "b2b" to get access token
      And I perform POST request to add and authorise "<merchant>" membership card using b2b token
      Then I see a <status_code_returned>
      And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
      Then I perform DELETE request to delete user successfully
      And verify that the PLL links are deleted from the scheme account for "<journey_type2>"

     Examples:
      | merchant      | status_code_returned | journey_type      |journey_type2      |
      | Iceland       | 202                  | add_and_authorise |pll                |













