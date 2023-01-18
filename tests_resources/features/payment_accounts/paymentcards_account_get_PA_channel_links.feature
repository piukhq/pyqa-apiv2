# Created by nehapatil at 13/01/2023
@trusted_channel_transparency @trusted @bink_regression_api2 @actual_tc
Feature: Provide Payment Card Channel Transparency to Trusted Channels
  As a trusted channel, I want to know which channel(s) a given loyalty card has payment cards linked in
  so that users are informed which channel(s) they need to go to, to manage their payment cards.


  @tc_pay_ac_channel_links
  Scenario Outline: Single wallet channel transparency in Trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>

    Examples:
      | merchant      | status_code_returned |payment_card_provider |
      | SquareMeal    | 200                  | master               |


  @tc_pay_ac_channel_links
  Scenario Outline: Single wallet channel transparency in Trusted channel 2 payment cards
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>

    Examples:
      | merchant      | status_code_returned |payment_card_provider |
      | SquareMeal    | 200                  | master               |


  @get_pa_invalid_token
  Scenario Outline: Verify invalid token scenario for get payment account channel links
    Given I am a squaremeal user
    When I perform GET request with <invalid> to view payment_account_channel_links
    Then I see a <status_code_returned>
    And I verify "<error_message>" "<error_slug>" of payment_account response

    Examples:
      | status_code_returned | error_message             | error_slug    |invalid|
      | 401                  | Supplied token is invalid | INVALID_TOKEN |token  |




  @multiplewallet
  Scenario Outline: Multiple wallet channel transparency in Trusted channel
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a 202
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>


    Examples:
      | payment_card_provider | merchant | status_code_returned |
      | master                | SquareMeal| 200                 |
      | amex                  | SquareMeal| 200                 |
      | visa                  | SquareMeal| 200                 |




  @get_pa_non_tc
  Scenario Outline: Get payment account channel links in non TC
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    When For bink_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>

    Examples:
      | status_code_returned |
      | 403                  |


  @tc_pa_inactive_pll @inactive
  Scenario Outline: Single wallet channel transparency in Trusted channel with inactive pll
    Given I am a squaremeal user
    When I perform POST request to add a <payment_status> "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>

    Examples:
      | merchant      | status_code_returned |payment_card_provider |payment_status|
      | SquareMeal    | 200                  | master               |pending       |
      | SquareMeal    | 200                  | master               |invalid_card_detail |
      | SquareMeal    | 200                  | master               |duplicate       |


  @multiplewallet_inactive @inactive
  Scenario Outline: Multiple wallet channel transparency in Trusted channel with inactive pll
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a <payment_status> "<payment_card_provider>" payment card to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    Then I see a 202
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>


    Examples:
      | merchant      | status_code_returned |payment_card_provider |payment_status|
      | SquareMeal    | 200                  | master               |pending       |
      | SquareMeal    | 200                  | master               |invalid_card_detail |
      | SquareMeal    | 200                  | master               |duplicate       |


  @multiplewallet_unauth_get_pa
  Scenario Outline: Multiple wallet channel transparency in Trusted channel with unauthorised LC in non-TC
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>
    Given I am a Lloyds user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add and auth "<merchant>" membership card with "unauthorised" with "202"
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>


    Examples:
      | payment_card_provider | merchant | status_code_returned |
      | master                | SquareMeal| 200                 |


  @get_pa_2_lc
  Scenario Outline: Single wallet channel transparency in Trusted channel with 2 loyalty cards
    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When I perform put request with successful_payload to update trusted_add for <merchant>
    Then I see a 201
    When I perform POST request to add trusted channel "<merchant>" loyalty card
    Then I see a 201
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>
    Examples:
      | payment_card_provider | merchant | status_code_returned |
      | master                | SquareMeal| 200                 |

