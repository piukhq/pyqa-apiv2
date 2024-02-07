# Created by bularaghavan on 26/10/2021
@bink_regression_api2 @fixme
Feature: View Loyalty Plan by id
 As a consuming channel
 I want to view a loyalty plan’s details available for my channel
 so that I can display this to users on the front end

  Scenario Outline: View Loyalty Plan by id
    Given I am a Lloyds user
    When I perform GET request to view and compare "<loyalty_scheme>" loyalty plan by id
    Then I verify the <status_code> for loyalty plan

    Examples:
      | loyalty_scheme      | status_code |
      | SquareMeal          | 200         |
      | Viator              | 200         |
      | The_Works           | 200         |

  Scenario Outline: Verify is_in_wallet field for Loyalty Plan by id
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id and verify is_in_wallet field
    Then I verify the <status_code> for loyalty plan
    And  I can see the loyalty plan fields of that merchant "<loyalty_scheme>"

    Examples:
      | loyalty_scheme      | status_code |
      | SquareMeal          | 200         |
      | Viator              | 200         |
      | The_Works           | 200         |

  Scenario Outline: Verify loyalty plan by id gives correct error messages with invalid token
    Given I am a Lloyds user
    When I perform GET request to view "<loyalty_scheme>" loyalty plan by id with invalid token
    Then I verify the <status_code> for loyalty plan
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme | status_code | error_message             | error_slug    |
      | The_Works      | 401         | Supplied token is invalid | INVALID_TOKEN |
