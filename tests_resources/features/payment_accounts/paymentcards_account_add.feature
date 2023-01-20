# Created by rupalpatel at 16/07/2021
@paymentcard_account_add @paymentcard_account
Feature: As a Bink User
  I want to be able to add my payment card account to my bink wallet
  So that I can start to earn rewards when I use my payment card


  @enrol_new_paymentcard @bink_regression_api2 @sandbox_regression
  Scenario Outline: Enrol new payment card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
#    GET is not implemented
#    And I perform the GET request to verify the new payment card "<payment_card_provider>" has been added successfully to the wallet
    Then I verify the paymentcard "<payment_card_provider>" been added into my wallet
    Then I see a <status_code_returned>

    Examples:
      | payment_card_provider | status_code_returned |
      | master                | 201                  |
      | amex                  | 201                  |
      | visa                  | 201                  |

  @enrol_existing_paymentcard @bink_regression_api2 @sandbox_regression
  Scenario Outline: Replace expiry_month,expiry_year,name_on_card,card_nickname into payment card
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    And I replace "<payment_card_provider>" "<expiry_month>" "<expiry_year>" "<name_on_card>" "<card_nickname>" into the payment card
    Then I see a <status_code_returned>

    Examples:
      | payment_card_provider | expiry_month | expiry_year | name_on_card | card_nickname | status_code_returned |
      | master                | 12           | 2999        | Mr AutoBink  | qa_automation | 200                  |

  @empty_payload @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending empty payload
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform "<request_call>" payment_account request with empty json payload
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response
    Examples:
      | request_call | status_code_returned | error_message             | error_slug             |
      | POST         | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |

  @empty_null_payload @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending null payload
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform "<request_call>" payment_account request with null json in payload
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response
    Examples:
      | request_call | status_code_returned | error_message | error_slug        |
      | POST         | 400                  | Invalid JSON  | MALFORMED_REQUEST |

  @sending_invalid_token @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token header
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST <payment_card_provider> payment_account request with invalid token
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code_returned | error_message                                        | error_slug    |
      | master                | 401                  | Access Token must be in 2 parts separated by a space | INVALID_TOKEN |

  @sending_invalid_token2 @bink_regression_api2 @sandbox_regression
  Scenario Outline: Sending invalid token with bearer prefix in header
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST <payment_card_provider> payment_account request with invalid token and bearer prefix
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | payment_card_provider | status_code_returned | error_message             | error_slug    |
      | master                | 401                  | Supplied token is invalid | INVALID_TOKEN |


  @optional_field @field_verify @bink_regression_api2 @sandbox_regression
  Scenario Outline: Remove name_on_card,card_nickname,issuer,provider,type,country,currency_code from the payload
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new payment card by removing "optional" field to wallet
    Then I see a <status_code_returned>

    Examples:
   | status_code_returned |
   | 201                  |

  @mandatory_field @field_verify @bink_regression_api2 @sandbox_regression
  Scenario Outline: Remove expiry_month,expiry_year,token,last_four_digits,first_six_digits,fingerprint from the payload
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new payment card by removing "mandatory" field to wallet
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | status_code_returned | error_message             | error_slug             |
      | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR |

  @mandatory_field_empty_field @field_verify @bink_regression_api2 @sandbox_regression
  Scenario Outline: Leave expiry_month,expiry_year,token,last_four_digits,first_six_digits,fingerprint empty field from the payload
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add "<payment_card_provider>" payment card to wallet
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | status_code_returned | error_message             | error_slug             | payment_card_provider |
      | 422                  | Could not validate fields | FIELD_VALIDATION_ERROR | master                |

  @multiplewallet @bink_regression_api2 @sandbox_regression
  Scenario Outline: Successfully add existing payment card to second wallet, same details
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    And I am in Bink channel to get b2b token for second user
    And I perform POST token request for token type "b2b" to get access token for second user
    And I perform POST request to add existing payment card "<payment_card_provider>" second wallet
    Then I see an <existing_payment_card_status> status code
    And I perform DELETE request to delete "<payment_card_provider>" the payment card from another wallet

    Examples:
      | payment_card_provider |  existing_payment_card_status |
      | master                |  200                          |
      | amex                  |  200                          |
      | visa                  |  200                          |

  @multiplewallet_different_detail @bink_regression_api2 @sandbox_regression
  Scenario Outline: Successfully add existing payment card to second wallet, different details
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    And I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    Then I see a <status_code_returned>
    Given I am a Lloyds user
    Then I perform existing payment card "<payment_card_provider>" to my another wallet with different "<expiry_month>" "<expiry_year>" "<name_on_card>" "<card_nickname>"
    And I see an <existing_payment_card_status> status code
    And I perform DELETE request to delete "<payment_card_provider>" the payment card from another wallet

    Examples:
      | payment_card_provider | status_code_returned | existing_payment_card_status | expiry_month | expiry_year | name_on_card | card_nickname |
      | master                | 201                  | 200                          | 2            | 2999        | QA_auto      | QA_TEST       |
      | amex                  | 201                  | 200                          | 2            | 2999        | QA_auto      | QA_TEST       |
      | visa                  | 201                  | 200                          | 2            | 2999        | QA_auto      | QA_TEST       |
