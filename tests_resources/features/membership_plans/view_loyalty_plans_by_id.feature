# Created by bularaghavan on 26/10/2021
@loyalty_plan_by_id @membership_plans
Feature: View Loyalty Plan by id
 As a consuming channel
 I want to view a loyalty plan’s details available for my channel
 so that I can display this to users on the front end

  @loyalty_plan_id_success @journey_type @bink_regression_api2
  Scenario Outline: View Loyalty Plan by id
    Given I am a Bink user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id
    Then I verify the <status_code> for loyalty plan
#    And  I can see the loyalty plan fields of that merchant "<loyalty_scheme>"

    Examples:
      | loyalty_scheme      | status_code |
      | Iceland             | 200         |
      | Wasabi              | 200         |
      | HarveyNichols       | 200         |

  @loyalty_plan_id_invalid_token @invalid_token @bink_regression_api2
  Scenario Outline: Verify loyalty plan by id gives correct error messages with invalid token
    Given I am a Bink user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme | status_code | error_message             | error_slug    |
      | Iceland        | 401         | Supplied token is invalid | INVALID_TOKEN |
      | Wasabi         | 401         | Supplied token is invalid | INVALID_TOKEN |
      | HarveyNichols  | 401         | Supplied token is invalid | INVALID_TOKEN |

  @loyalty_plan_id_invalid_resource @invalid_resource @bink_regression_api2
  Scenario Outline: Verify loyalty plan by id gives correct error messages with invalid loyalty scheme
    Given I am a Bink user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id with invalid resource
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme      | status_code | error_message                       | error_slug         |
      | Merchant_not_exists | 404         | Could not find this account or card | RESOURCE_NOT_FOUND |