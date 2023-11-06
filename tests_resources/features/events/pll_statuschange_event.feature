# Created by bularaghavan on 13/06/2024
@pll_statuschange_events @events
Feature: Verify event for pll status change
  As a Data Analyst, I want to see an Event logged whenever the state of the PLL link between a Payment Card and Loyalty Card changes,
  so that this Business Event can be written to ClickHouse for validation.


# Will only run successfully after bug fix WAL-3150
  @auth_success_plllink_statuschange
  Scenario: Verify events for pll link status change for add and auth success
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add "Viator" membership card
    And I perform PUT request to authorise "Viator" above wallet only membership card
    Then verify that for lloyds_user data stored in after authorise_field journey for "Viator"
    And I verify pll_link_statuschange pll event is created for lloyds_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for lloyds_user for status 0 to 1 and slug null


# Will only run successfully after bug fix WAL-3150
  @add_auth_fail_plllink_statuschange
  Scenario: Verify events for pll link status change for add and auth failure
    Given I am a halifax user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add and auth "Wasabi" membership card with "unauthorised" with "202"
    Then I verify pll_link_statuschange pll event is created for halifax_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for halifax_user for status 0 to 2 and slug LOYALTY_CARD_NOT_AUTHORISED

# Will only run successfully after bug fix WAL-3150
   @join_success_plllink_statuschange
  Scenario: Verify events for pll link status change for join success
    Given I am a halifax user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to join "Viator" membership card
    Then I verify pll_link_statuschange pll event is created for halifax_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for halifax_user for status 0 to 1 and slug null

# Will only run successfully after bug fix WAL-3150
   @join_fail_plllink_statuschange
  Scenario: Verify events for pll link status change for join failure
    Given I am a halifax user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform enrol_failed POST request to join "Viator" membership card
    Then I verify pll_link_statuschange pll event is created for halifax_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for halifax_user for status 0 to 2 and slug LOYALTY_CARD_NOT_AUTHORISED

# Will only run successfully after bug fix WAL-3150
    @register_success_plllink_statuschange
  Scenario: Verify events for pll link status change for register success
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request add and register for Viator
    Then I verify pll_link_statuschange pll event is created for lloyds_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for lloyds_user for status 0 to 1 and slug null

  # Will only run successfully after bug fix WAL-3150
  @register_fail_plllink_statuschange
  Scenario: Verify events for pll link status change for register failure
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add Viator membership card before registration_failed register
    And I perform PUT request to register Viator with registration_failed membership card
    Then I verify pll_link_statuschange pll event is created for lloyds_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for lloyds_user for status 0 to 2 and slug LOYALTY_CARD_NOT_AUTHORISED

  @lc_remove_plllink_statuschange @bink_regression_api2
  Scenario: Verify events for pll link status change after deleting loyalty card
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add and authorise "Viator" membership card
    Then I perform DELETE request to delete the "Viator" membership card
    And I verify pll_link_statuschange pll event is created for lloyds_user for status 1 to null and slug null

  @pc_remove_plllink_statuschange @bink_regression_api2
  Scenario: Verify events for pll link status change after deleting payment card
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add and authorise "Viator" membership card
    Then I perform DELETE request to delete "master" the payment card
    And I verify pll_link_statuschange pll event is created for lloyds_user for status 1 to null and slug null

  @pll_link_status_multi_wallet @bink_regression_api2 @event
  Scenario: Verify event generate for  add and auth success in multiwallet
    Given I am a Lloyds user
    When I perform POST request to add a new "master" payment account to wallet
    And I perform POST request to add and authorise "Viator" membership card
    Then I verify pll_link_statuschange pll event is created for lloyds_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for lloyds_user for status 0 to 1 and slug null

    Given I am a halifax user
    When I perform POST request to add existing payment card "master" second wallet
    And I perform POST request to add and authorise "Viator" membership card
    Then I verify pll_link_statuschange pll event is created for halifax_user for status null to 0 and slug LOYALTY_CARD_PENDING
    And I verify pll_link_statuschange pll event is created for halifax_user for status 0 to 1 and slug null
