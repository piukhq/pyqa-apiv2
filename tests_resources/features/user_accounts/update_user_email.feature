# Created by bularaghavan at 16/11/2021
@membership_card_update_email @membership_cards @user_test
Feature: Update email feature
  As a Bink user
  I want to update my email address associated with my Bink account
  so that I can continue to use my Bink account with my preferred email address

  @sit @bink_regression_api2
  Scenario Outline: Update to new email success
    Given I am a Lloyds user
    When I perform POST request to update email
    Then I see a <status_code_returned>
    And I perform POST request to update email again
    Then I see a <status_code_returned>

    Examples:
    | status_code_returned |
    | 200                  |
