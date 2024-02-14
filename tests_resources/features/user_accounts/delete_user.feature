# Created by bularaghavan at 17/01/2022
@bink_regression_api2
Feature: Delete User feature
  As a Bink ‘B2B’ user
  I want to delete my Bink account because I no longer wish to be enrolled in the service


  Scenario: Delete User success
    Given I am in Bink channel to get b2b token
    When I perform POST token request for token type "b2b" to get access token
    Then I perform DELETE request to delete user successfully

     @fixme
    Scenario Outline: soft delete pll links
      Given I am a Lloyds user
      When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
      And I add and authorise "<merchant>" membership card
      Then I see a <status_code_returned>
      And verify that for lloyds_user data stored in after "<journey_type>" journey for "<merchant>"
      And verify that for lloyds_user data stored in after "<journey_type2>" journey for "<merchant>"
      And I perform DELETE request to delete user successfully
      And verify that the PLL links are deleted from the scheme account for "<journey_type2>"

     Examples:
       |payment_card_provider| merchant      | status_code_returned | journey_type      |journey_type2      |
       |master               | Viator        | 202                  | add_and_authorise  |pll               |
