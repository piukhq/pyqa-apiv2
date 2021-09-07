# Created by rupalpatel at 06/09/2021
Feature: As a Bink API Consumer I want to view the all the fields a user is required to fill in in order to complete all supported loyalty card journeys
  so that I can display them to the user when required.

  @membership_plan
  Scenario Outline: VIEW Loyalty Plans journey fields - Iceland
##    Given I am a Bink user
##    When I perform GET request to view all available membership plans
#    When I perform GET request to view journey field for "<loyalty_scheme>"
##    Then I can ensure the "Wasabi" plan details match with expected data

    Examples:
      | loyalty_scheme |
      | Iceland        |