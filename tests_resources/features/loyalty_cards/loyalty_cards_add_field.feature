# Created by rupalpatel at 20/09/2021
@membership_card_add @membership_cards
Feature: Add a loyalty card
  As a Bink user
  I want to store a loyalty card in my wallet
  so that I can display the barcode in-store, and (if applicable) authorise the loyalty card at a later stage

  @bink_regression_api2  @fixme
  Scenario Outline: Add field journey only
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    Then I see a <status_code_returned>
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    And verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type | status_code_returned |
      | Viator | Add_field    | 202                  |
