# Created by rupalpatel at 16/07/2021
@paymentcard_account
Feature: As a Bink User
  I want to be able to add my Payment Account to my bink account
  So that I can start to earn rewards when I use my payment card


  @enrol_new_paymentcard
  Scenario Outline: Enrol new payment card
#    Given I am a Bink user
    When I perform POST request to add a new "<payment_card_provider>" payment card to wallet
#    GET is not implemented
#    And I perform the GET request to verify the new payment card "<payment_card_provider>" has been added successfully to the wallet
    Then I verify the paymentcard "<payment_card_provider>" been added into my wallet
    And I perform DELETE request to delete "<payment_card_provider>" the payment card

    Examples:
      | payment_card_provider |
      | master                |
#    | amex                  |
#    | visa                  |

  