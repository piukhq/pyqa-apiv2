# Created by rupalpatel at 10/09/2021
@loyalty_plans
Feature: view journey fields
  As a Bink API Consumer
  I want to view the all the fields a user is required to fill in in order to complete all supported loyalty card journeys
  so that I can display them to the user when required.

  @membership_plan_journeyfield @journey_type @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify VIEW Loyalty Plans journey fields for loyalty scheme
    Given I am a Lloyds user
    When I perform GET request to view journey field for "<loyalty_scheme>"
    Then I verify the <status_code> for journey field appeared
    And I can see the journey fields of that merchant "<loyalty_scheme>"

    Examples:
      | loyalty_scheme | status_code |
      | Iceland        | 200         |
      | Wasabi         | 200         |
      | SquareMeal     | 200         |
      | Asos           | 200         |
      | Trenette       | 200         |
  #    | Viator         | 200         |
  #    | HarveyNichols  | 200         |

  @membership_plan @invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify request does not have a valid token
    Given I am a Lloyds user
    When I perform GET request to view journey field for "<loyalty_scheme>" for invalid token
    Then I verify the <status_code> for journey field appeared
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

  @membership_plan @invalid_resource @bink_regression_api2 @sandbox_regression
  Scenario Outline: Verify Resource specified could not be found
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform GET request to view journey field for "<loyalty_scheme>" for invalid resource
    Then I verify the <status_code> for journey field appeared
    And I verify "<error_message>" "<error_slug>" in loyalty scheme response

    Examples:
      | loyalty_scheme      | status_code | error_message                       | error_slug         |
      | Merchant_not_exists | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
      | Wallis              | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |
      | Bink Test Scheme    | 404         | Could not find this Loyalty Plan | RESOURCE_NOT_FOUND |

