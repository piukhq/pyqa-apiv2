# Created by bularaghavan on 14/03/2022
@bink_regression_api2
Feature: View Loyalty Plan by id
 As a consuming channel
 I want to retrieve the details of a given loyalty plan
 so that I can present these to a user, should they want to find out more, as well as so that I do not have to call the whole loyalty_plan endpoint for this information

  Scenario Outline: View Loyalty Plan Details
    Given I am a Lloyds user
    When I perform GET request to view and compare "<loyalty_scheme>" loyalty plan details
    Then I verify the <status_code> for loyalty plan

    Examples:
      | loyalty_scheme      | status_code |
      | SquareMeal          | 200         |
      | Trenette            | 200         |
      | Viator              | 200         |
      | The_Works           | 200         |

  Scenario Outline: Verify loyalty plan details gives correct error messages with invalid token
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan details with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme | status_code | error_message             | error_slug    |
      | Viator         | 401         | Supplied token is invalid | INVALID_TOKEN |

  Scenario Outline: Verify loyalty plan details gives correct error messages with invalid loyalty scheme
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request to view "<loyalty_scheme>" loyalty plan details with invalid resource
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme      | status_code | error_message                     | error_slug         |
      | Merchant_not_exists | 404         | Could not find this Loyalty Plan  | RESOURCE_NOT_FOUND |
