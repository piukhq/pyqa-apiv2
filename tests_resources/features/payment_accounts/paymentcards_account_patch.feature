# Created by rupalpatel at 27/07/2021
@paymentcard_account_patch
Feature: As a Bink User
  I want to be able update some details on my payment account
  so that I can keep my account upto date and customize it.


  @patch_payment_account @bink_regression_api2
  Scenario Outline: update payment card
    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    And I perform PATCH request to update "<update_field>" and "<payment_card_provider>" payment card to wallet

    Then I verify the paymentcard "<payment_card_provider>" been updated with "<update_field>"
    And I see a "<status_code_returned>" status code for payment account
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

    Examples:
      | payment_card_provider | status_code_returned | update_field                                                   |
      | master                | 200                  | expiry_month                                                   |
      | master                | 200                  | expiry_year                                                    |
      | master                | 200                  | name_on_card                                                   |
      | master                | 200                  | card_nickname                                                  |
      | master                | 200                  | issuer                                                         |
      | master                | 200                  | expiry_month, expiry_year, name_on_card, card_nickname, issuer |
      | amex                  | 200                  | expiry_month                                                   |
      | amex                  | 200                  | expiry_year                                                    |
      | visa                  | 200                  | expiry_year                                                    |

  @sending_invalid_token_patch @bink_regression_api2
  Scenario Outline: Sending invalid token header for Patch payment account
#    Given I am a Bink user
    When I perform PATCH <payment_card_provider> payment_account request with invalid token
    Then I see a "<status_code_returned>" status code for payment account
    And I verify "<error_message> <error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code_returned | error_message                                        | error_slug    |
      | master                | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |
      | visa                  | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |
      | amex                  | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |

  @sending_invalid_token2_patch @bink_regression_api2
  Scenario Outline: Sending invalid token with bearer prefix in header
#    Given I am a Bink user
    When I perform PATCH <payment_card_provider> payment_account request with invalid token and bearer prefix
    Then I see a "<status_code_returned>" status code for payment account
    And I verify "<error_message> <error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code_returned | error_message             | error_slug    |
      | master                | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | amex                  | 401                  | Supplied token is invalid | INVALID_TOKEN |
      | visa                  | 401                  | Supplied token is invalid | INVALID_TOKEN |

  @empty_payload_patch @bink_regression_api2
  Scenario Outline: Sending empty payload to patch payment_account
    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform "<request_call>" payment_account request with empty_json payload
    Then I see a "<status_code_returned>" status code for payment account
    And I verify "<error_message> <error_slug>" of payment_account response
    Examples:
      | payment_card_provider | request_call | status_code_returned | error_message             | error_slug             |
      | master                | PATCH        | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |
      | amex                  | PATCH        | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |
      | visa                  | PATCH        | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |

  @empty_null_payload_patch @bink_regression_api2
  Scenario Outline: Sending null payload to patch payment_account
    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform "<request_call>" payment_account request with null_json payload
    Then I see a "<status_code_returned>" status code for payment account
    And I verify "<error_message> <error_slug>" of payment_account response
    Examples:
      | payment_card_provider | request_call | status_code_returned | error_message | error_slug        |
      | master                | PATCH        | 400                  | Invalid JSON  | MALFORMED_REQUEST |
      | amex                  | PATCH        | 400                  | Invalid JSON  | MALFORMED_REQUEST |
      | visa                  | PATCH        | 400                  | Invalid JSON  | MALFORMED_REQUEST |

  @resource_not_found_patch @bink_regression_api2
  Scenario Outline: Resource not found to patch payment_account
    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    Then I perform DELETE request to delete "<payment_card_provider>" the payment card
    When I perform PATCH request to update "<update_field>" and "<payment_card_provider>" payment card to wallet
    Then I see a "<status_code_returned>" status code for payment account
    And I verify "<error_message> <error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code_returned | update_field | error_message                       | error_slug         |
      | master                | 404                  | expiry_month | Could not find this account or card | RESOURCE_NOT_FOUND |
      | amex                  | 404                  | expiry_month | Could not find this account or card | RESOURCE_NOT_FOUND |
      | visa                  | 404                  | expiry_month | Could not find this account or card | RESOURCE_NOT_FOUND |

  @patch_with_all_credential @bink_regression_api2
  Scenario Outline: Patch call with giving all add credential
    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    And I perform PATCH request to update "<payment_card_provider>" payment card with add credential
    Then I see a "<status_code_returned>" status code for payment account
    And I verify "<error_message> <error_slug>" of payment_account response
    Then I perform DELETE request to delete "<payment_card_provider>" the payment card


    Examples:
      | payment_card_provider | status_code_returned | error_message             | error_slug             |
      | master                | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |
      | amex                  | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |
      | visa                  | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |