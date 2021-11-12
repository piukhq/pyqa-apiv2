# Created by bularaghavan on 11/11/2021
@membership_cards_wallet @membership_cards
Feature: View Wallet
    As a Bink user I want to view my loyalty cards in awallet-only state
    so that I can see the cards that support store only functionality

  @view_wallet_wasabi @bink_regression_api2
    Scenario Outline: View Wallet wasabi
    Given I am a Bink Wallet user1
    When I perform GET request to view Wallet for "<merchant>"
    Then I see a <status_code_returned>
    And I can see all Wallet fields successfully for the "<merchant>"

    Examples:
   | merchant| status_code_returned |
   | Wasabi  | 200                  |

   @view_wallet_iceland @bink_regression_api2
    Scenario Outline: View Wallet iceland
    Given I am a Bink Wallet user2
    When I perform GET request to view Wallet for "<merchant>"
    Then I see a <status_code_returned>
    And I can see all Wallet fields successfully for the "<merchant>"

    Examples:
   | merchant| status_code_returned |
   | Iceland  | 200                 |

    @view_wallet_join @bink_regression_api2
    Scenario Outline: View Wallet joins
    Given I am a Bink Wallet user3
    When I perform GET request to view Wallet for "<merchant>"
    Then I see a <status_code_returned>
    And I can see all join Wallet fields successfully for the "<merchant>"


    Examples:
   | merchant| status_code_returned |
   | Iceland  | 200                 |

   @wallet_invalid_token @bink_regression_api2
   Scenario Outline: Verify invalid token scenario for get Wallet
     Given I am a Bink Wallet user1
     When I perform GET request to view Wallet for "<merchant>" with invalid token
     Then I see a <status_code_returned>
     And I see a "<error_message>" error message
     And I see a "<error_slug>" error slug

     Examples:
     | status_code_returned | error_message              | error_slug      | merchant|
     | 401                  | Supplied token is invalid   | INVALID_TOKEN   | Wasabi |

