# Created by rupalpatel at 06/10/2021
@membership_card_join @membership_cards
Feature: Add and register a loyalty card
  As a Bink user
  I want to join a loyalty scheme
  so that I can use the Bink functionality with the relevant loyalty plan

  @join_scheme @bink_regression_api2
  Scenario Outline: join journey
    Given I am a Bink user
    When I perform POST request to join "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I perform DELETE request to delete the "<merchant>" membership card
    Examples:
      | merchant      | status_code_returned | journey_type |
      | Iceland       | 202                  | join         |
      | Wasabi        | 202                  | join         |
      | HarveyNichols | 202                  | join         |
