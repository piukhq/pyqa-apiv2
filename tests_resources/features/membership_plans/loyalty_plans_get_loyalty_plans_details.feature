# Created by bularaghavan on 14/03/2022
@loyalty_plan_details @membership_plans
Feature: View Loyalty Plan by id
 As a consuming channel
 I want to retrieve the details of a given loyalty plan
 so that I can present these to a user, should they want to find out more, as well as so that I do not have to call the whole loyalty_plan endpoint for this information

  @loyalty_plan_details_success @journey_type @bink_regression_api2 @sandbox_regression
  Scenario Outline: View Loyalty Plan Details
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan details
    Then I verify the <status_code> for loyalty plan

    Examples:
      | loyalty_scheme      | status_code |
      | Iceland             | 200         |
      | Wasabi              | 200         |
      | SquareMeal          | 200         |
      | Asos                | 200         |
      | Trenette            | 200         |
      | Viator              | 200         |
  #    | HarveyNichols       | 200         |

  @loyalty_plan_details_invalid_token @invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify loyalty plan details gives correct error messages with invalid token
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan details with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme | status_code | error_message             | error_slug    |
      | Iceland        | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi         | 401         | Supplied token is invalid | INVALID_TOKEN |
      | SquareMeal     | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Asos           | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Trenette       | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Viator         | 401         | Supplied token is invalid | INVALID_TOKEN |
  #    | HarveyNichols  | 401         | Supplied token is invalid | INVALID_TOKEN |

  @loyalty_plan_details_invalid_resource @invalid_resource @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify loyalty plan details gives correct error messages with invalid loyalty scheme
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request to view "<loyalty_scheme>" loyalty plan details with invalid resource
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme      | status_code | error_message                     | error_slug         |
      | Merchant_not_exists | 404         | Could not find this Loyalty Plan  | RESOURCE_NOT_FOUND |
      | Wallis             | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
      | Bink Test Scheme    | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
