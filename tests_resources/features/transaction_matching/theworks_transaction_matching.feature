@tm @the_works

Feature: Merchant The Work - Ensure a customer can use Bink's Transaction Matching features
  As a customer
  I shopped at a Bink PLL partner that uses transaction matching
  So I can offer a near real time transaction matching service to merchants.

   @bink_regression_api2
  Scenario: Verify transaction spotting for TheWorks using Visa E2E

    Given I am a bos user
    When I perform POST request to add a new visa payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment Transaction File with visa-auth-spotting-e2e and MID as 1136668
    When I send Payment Transaction File with visa-settlement-spotting-e2e and MID as 1136668
    Then I verify the reward transaction is exported using transaction-spotting
    When I send Payment Transaction File with visa-refund-spotting-e2e and MID as 1136668
    Then I verify the reward transaction is exported using transaction-spotting

  #  Can not be tested as the Amex Mids are not available in staging
    Scenario: Verify transaction spotting for TheWorks using Amex E2E

    Given I am a bos user
    When I perform POST request to add a new visa payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment Transaction File with amex-settlement-spotting and MID as works0003
    Then I verify the reward transaction is exported using transaction-spotting
    When I send Payment Transaction File with amex-refund-spotting and MID as works0003
    Then I verify the reward transaction is exported using transaction-spotting

  @bink_regression_api2
    Scenario: Verify transaction spotting for TheWorks using Master E2E

    Given I am a bos user
    When I perform POST request to add a new visa payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment Transaction File with master-settlement-spotting and MID as 1136668
    Then I verify the reward transaction is exported using transaction-spotting
    When I send Payment Transaction File with master-refund-spotting-the-works and MID as 1136668
    Then I verify the reward transaction is exported using transaction-spotting-refund-the-works

   @bink_regression_api2
  Scenario Outline: Verify transaction spotting for TheWorks _ dedupe

    Given I am a bos user
    When I perform POST request to add a new <payment_card_provider> payment account to wallet
    When I perform POST request to add and authorise "The_Works" membership card with transactions and vouchers
    And  And I perform GET Wallet
    When I send Payment File with a duplicate transaction using <payment_card_transaction> and <mid>
    Then I verify the reward transaction is de-duplicated using dedupe and spotting
    Examples:

      | payment_card_provider | mid       | payment_card_transaction |
      | visa                  | 1136668   | visa-settle-spotting     |
