# Created by bularaghavan on 26/10/2021
@loyalty_plan_by_id @loyalty_plans
Feature: View Loyalty Plan by id
 As a consuming channel
 I want to view a loyalty plan’s details available for my channel
 so that I can display this to users on the front end

  @loyalty_plan_id_success @journey_type @bink_regression_api2 @sandbox_regression
  Scenario Outline: View Loyalty Plan by id
    Given I am a Lloyds user
    When I perform GET request to view and compare "<loyalty_scheme>" loyalty plan by id
    Then I verify the <status_code> for loyalty plan

    Examples:
      | loyalty_scheme      | status_code |
      | Iceland             | 200         |
      | Wasabi              | 200         |
      | SquareMeal          | 200         |
      | Trenette            | 200         |
      | Viator              | 200         |
  #   | The_Works           | 200         |

  @loyalty_is_in_wallet @journey_type @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify is_in_wallet field for Loyalty Plan by id
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id and verify is_in_wallet field
    Then I verify the <status_code> for loyalty plan
    And  I can see the loyalty plan fields of that merchant "<loyalty_scheme>"

    Examples:
      | loyalty_scheme      | status_code |
      | Iceland             | 200         |
      | Wasabi              | 200         |
      | SquareMeal          | 200         |
      | Trenette            | 200         |
      | Viator              | 200         |
      | The_Works           | 200         |

  @loyalty_plan_id_invalid_token @invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify loyalty plan by id gives correct error messages with invalid token
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme | status_code | error_message             | error_slug    |
      | Iceland        | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi         | 401         | Supplied token is invalid | INVALID_TOKEN |
      | SquareMeal     | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Trenette       | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Viator         | 401         | Supplied token is invalid | INVALID_TOKEN |
      | The_Works      | 401         | Supplied token is invalid | INVALID_TOKEN |

  @loyalty_plan_id_invalid_resource @invalid_resource @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify loyalty plan by id gives correct error messages with invalid loyalty scheme
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request to view "<loyalty_scheme>" loyalty plan by id with invalid resource
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme      | status_code | error_message                       | error_slug       |
      | Merchant_not_exists | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
      | Wallis              | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
      | Bink Test Scheme    | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
