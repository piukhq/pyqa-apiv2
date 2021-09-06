# Created by rupalpatel at 06/09/2021
@iceland @dev
Feature: Merchant Iceland - Ensure a customer can view Scheme plan details
  As a customer
  I want to access membership plans
  So I can choose a membership plan to view its details

  Verify a customer can use Banking API to view available Iceland membership plans v2.0


  @membership_plan @bink_regression @bmb_regression
   Scenario: Membership plan Iceland
#    Given I am a Bink user
#    When I perform GET request to view all available membership plans
    Then I can ensure the "Iceland" plan details match with expected data


