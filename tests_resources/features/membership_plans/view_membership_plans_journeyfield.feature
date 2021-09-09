# Created by rupalpatel at 06/09/2021
Feature: As a Bink API Consumer I want to view the all the fields a user is required to fill in in order to complete all supported loyalty card journeys
  so that I can display them to the user when required.

  @membership_plan @journey_type @bink_regression
  Scenario Outline: VIEW Loyalty Plans journey fields - Iceland
#    Given I am a Bink user
#    When I perform GET request to view all available membership plans
    When I perform GET request to view journey field for "<loyalty_scheme>"
#    Then I can see the journey fields of that merchant "<loyalty_scheme>"

    Examples:
      | loyalty_scheme |
      | Iceland        |