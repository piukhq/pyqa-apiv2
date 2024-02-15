# Created by rupalpatel at 20/09/2021
@membership_cards
Feature: Add a loyalty card
  As a Bink user
  I want to store a loyalty card in my wallet
  so that I can display the barcode in-store, and (if applicable) authorise the loyalty card at a later stage

  @bink_regression_api2
  Scenario Outline: Add field journey only
    Given I am a bos user
    When I perform POST request to add "<merchant>" membership card
    Then verify that for bos_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type |
      | Viator   | Add_field    |
