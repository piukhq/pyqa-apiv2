@transactionMatching @square_meal
Feature: Merchant SquareMeal - Ensure a customer can use Bink's Transaction Matching features
  As a customer
  I shopped at a Bink PLL partner that uses transaction matching
  So I can offer a near real time transaction matching service to merchants.

  @transactionMatchingSquareMeal @bink_regression @sanity @test
    Scenario Outline: Verify transaction streaming for squareMeal

    Given I am a squaremeal user
    When I perform POST request to add a new "<payment_card_provider>" payment account to wallet
    When I perform POST request to add and authorise "<merchant>" membership card
    And  And I perform GET Wallet
    When I send matching <payment_card_transaction> <mid> Authorisation
    Then I verify "<payment_card_transaction>","<mid>" and "auth_code" is spotted and exported


    Examples:
   | merchant  | payment_card_provider|     mid       |payment_card_transaction      |
   | SquareMeal|  visa                |  29047531     |visa-auth-spotting            |