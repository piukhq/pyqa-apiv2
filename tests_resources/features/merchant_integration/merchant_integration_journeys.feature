# Created by njames on 22/03/2023
Feature: Basic Merchant Integration Journies
  As a Bank user
  I want check all Loyalty card features
  so that I am able to benefit from the Bink functionality


  Scenario Outline: Add existing card again into wallet
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<merchant>" membership card
    And I perform POST request again to verify the "<merchant>" membership card is already added with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then verify that for bink_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant | journey_type | status_code |
      | Iceland  | Add_field    | 200         |
      | Wasabi   | Add_field    | 200         |
      | Viator   | Add_field    | 200         |
      |SquareMeal| Add_field    | 200         |
