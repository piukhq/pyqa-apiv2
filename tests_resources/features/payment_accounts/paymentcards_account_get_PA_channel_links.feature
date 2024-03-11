# Created by nehapatil at 13/01/2023

Feature: Provide Payment Card Channel Transparency to Trusted Channels
  As a trusted channel, I want to know which channel(s) a given loyalty card has payment cards linked in
  so that users are informed which channel(s) they need to go to, to manage their payment cards.
  @bink_regression_api2
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
    When I add and authorise "<merchant>" membership card
    Then I see a 202
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>


    Examples:
      | payment_card_provider | merchant | status_code_returned |
      | master                | SquareMeal| 200                 |


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
    When I add and authorise "<merchant>" membership card
    Then I see a 202
    When For squaremeal_user I perform get payment_account_channel_links
    Then I see a <status_code_returned>
    Then verify response of get payment account channel links for <merchant>


    Examples:
      | merchant      | status_code_returned |payment_card_provider |payment_status|
      | SquareMeal    | 200                  | master               |pending       |
      | SquareMeal    | 200                  | master               |invalid_card_detail |
      | SquareMeal    | 200                  | master               |duplicate       |


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
