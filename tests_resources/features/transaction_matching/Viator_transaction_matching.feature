@tm @viator
Feature: Merchant VIATOR - Ensure a customer can use Bink's Transaction Matching features
  As a customer
  I shopped at a Bink PLL partner that uses transaction matching
  So I can offer a near real time transaction matching service to merchants.

    Scenario Outline: Verify transaction spotting for Viator

     Given I am a bos user
    When I perform POST request to add a new <payment_card_provider> payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment Transaction File with <payment_card_transaction> <mid>
    Then I verify the reward transaction is exported using transaction-spotting
    Examples:
    | payment_card_provider|     mid       |payment_card_transaction    |
    |          visa        |  020150514    |visa-auth-spotting          |
    |          visa        |  020150514    |visa-settlement-spotting    |
    |          visa        |  020150514    |visa-refund-spotting        |
    |          master      |  020150514    |master-auth-spotting        |
# Already included in E2E Test    |          master      |  020150514    |master-settlement-spotting  |
    |          amex        |  9602929481   |amex-settlement-spotting     |
    |          amex        |  9602929481   |amex-refund-spotting        |


  Scenario Outline: Verify transaction Spotting for viator negative scenario(invalid mid)

    Given I am a bos user
    When I perform POST request to add a new <payment_card_provider> payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment Transaction File with <payment_card_transaction> <mid>
    Then I verify transaction is not streamed and exported


    Examples:
    | payment_card_provider|     mid       |payment_card_transaction |
    |          visa        |  29047530     |visa-auth-spotting       |
    |          visa        |  29047530     |visa-settlement-spotting |
    |          visa        |  29047530     |visa-refund-spotting     |
    |          master      |  29047530     |master-auth-spotting        |
    |          master      |  29047530     |master-settlement-spotting  |
    |          master      |  29047530     |master-refund-spotting      |



    Scenario: Verify transaction Viator MasterCard Transaction Spotting E2E(Settle, Refund)

    Given I am a bos user
    When I perform POST request to add a new visa payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment Transaction File with master-settlement-spotting and MID as 020150514
    Then I verify the reward transaction is exported using transaction-spotting
    When I send Payment Transaction File with master-refund-spotting and MID as 020150514
    Then I verify the reward transaction is exported using transaction-spotting-refund


