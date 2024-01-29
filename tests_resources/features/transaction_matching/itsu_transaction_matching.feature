@itsu @bink_regression_api2

Feature: As a Bink user I want Bink to match and export my payment transactions to my itsu retailer transaction so that I am able to earn stamps and rewards via PLL.
# This Service Integration Suite contains end-to-end tests for Transaction Matching for itsu using Visa
#  Mastercard and Amex are not in-scope for real-world transactions.
# itsu Transactionmatching checks around Payment amount (export iff amount >=5) should
# be handled in component level

  Scenario: Verify transaction spotting for itsu using Visa E2E

    Given I am a bos user
    When I perform POST request to add a new visa payment account to wallet
    When I perform POST request to add and authorise "itsu" membership card with transactions and vouchers
    And  And I perform GET Wallet
    # Passing Scheme container_location, Payment provider and Location_id as parameters in below step
    When Send Retailer Transaction File with "scheme/itsu/" "visa" and "10"
    When I send Payment Transaction File with visa-auth-matching and MID as 554196505480673
    When I send Payment Transaction File with visa-settlement-matching and MID as 554196505480673
    # When I send Payment Transaction File with visa-refund-spotting-e2e and MID as 554196505480673
    Then I verify the reward transaction is exported using transaction_matching
