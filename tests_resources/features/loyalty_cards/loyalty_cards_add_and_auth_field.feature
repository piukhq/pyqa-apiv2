# Created by rupalpatel at 23/09/2021
@loyalty_card_add_and_authorise @membership_cards
Feature: Add and authorise a loyalty card
  As a Bink user
  I want add an ‘Engage' or 'PLL’ type loyalty card to my wallet
  so that I am able to benefit from the Bink functionality

  @add_and_auth_field @bink_regression_api2 @sandbox_regression @chk
  Scenario Outline: Add and authorise field journey
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 202                  | add_and_authorise |
      | Trenette      | 202                  | add_and_authorise |
  #   | HarveyNichols | 202                  | add_and_authorise |

  @add_and_auth_existing_field @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add existing card again into wallet for add and authorise
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    And I perform POST request again with add and authorise to verify the "<merchant>" membership card is already added with "<status_code_returned>"
#    Then I see a <status_code_returned>
#    Then I see a "<error_message>" error message
#    And I see a "<error_slug>" error slug
    Then verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | merchant      | status_code_returned | journey_type      |
      | SquareMeal    | 409                  | add_and_authorise |
      | Trenette      | 409                  | add_and_authorise |

  @invalid_field_bad_request_add_authorise @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add field journey with Bad request for add and authorise
    Given I am a Lloyds user
    When I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | error_message             | error_slug             | request_payload | status_code |
      | SquareMeal  | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |
      | Trenette    | Could not validate fields | FIELD_VALIDATION_ERROR | invalid_request | 422         |

  @invalid_field @bink_regression_api2 @sandbox_regression
  Scenario Outline: Add and authorised field journey with Unprocessable entity
    Given I am a Lloyds user
    When I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" with "<status_code>"
#    And I perform GET request to verify the "<merchant>" membership card is added to the wallet
    Then I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant     | error_message | error_slug        | request_payload | status_code |
      | SquareMeal   | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |
      | Trenette     | Invalid JSON  | MALFORMED_REQUEST | invalid_json    | 400         |

  @sending_invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header for add and authoirse journey (Unauthorized)
    Given I am a Lloyds user
    When I perform POST <merchant> membership_card request for add_and_auth with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant     | status_code_returned | error_message             | error_slug    |
      | SquareMeal   | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | Trenette     | 401                  | Supplied token is invalid | INVALID_TOKEN |


  @add_already_then_add_auth @bink_regression_api2 @sandbox_regression
  Scenario Outline: Loyalty scheme already exist with add credential
    Given I am a Lloyds user
    When I perform POST request to add "<merchant>" membership card
    And I perform POST request to add and authorise "<merchant>" membership card which already exist with add credential
    Then I see a <status_code_returned>
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | status_code_returned | error_message                                                                                  | error_slug    |
      | Trenette    | 409                  | Card already added. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to authorise this card. | ALREADY_ADDED |


  @add_and_auth_with_different_authorised_field @bink_regression_api2 @sandbox_regression
  Scenario Outline: Already Add and authorised scheme then add with different auth credential
    Given I am a Lloyds user
    When I perform POST request to add and authorise "<merchant>" membership card
    And I perform POST request to add and authorise "<merchant>" with different auth credential
    Then I see a <status_code_returned>
#    And verify the data stored in DB after "<journey_type>" journey for "<merchant>"
    And I see a "<error_message>" error message
    And I see a "<error_slug>" error slug

    Examples:
      | merchant    | status_code_returned | error_message                                                                                                    | error_slug         |
      | SquareMeal  | 409                  |Card already authorised. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to modify authorisation credentials.  | ALREADY_AUTHORISED |
      | Trenette    | 409                  |Card already authorised. Use PUT /loyalty_cards/{loyalty_card_id}/authorise to modify authorisation credentials.  | ALREADY_AUTHORISED |

  @add_and_auth_pll @bink_regression_api2 @sandbox_regression
  Scenario Outline: verify PLL for add and authorise
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    And I perform POST request to add and authorise "<merchant>" membership card
    Then I see a <status_code_returned>
    And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"

    Examples:
      | payment_card_provider | merchant   | status_code_returned | journey_type |
      | master                | SquareMeal | 202                  | pll_active   |
      | master                | Trenette   | 202                  | pll_active  |
