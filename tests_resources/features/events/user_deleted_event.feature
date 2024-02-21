# Created by npatil on 19/04/2023
@bink_regression_api2 @events
Feature: Add and authorise a loyalty card
  As a DM Administrator
  I want to see an Event logged when a user is deleted
  so that this Business Event can be written to ClickHouse for validation


  Scenario: Verify event for user deleted
    Given I am a Lloyds user
    Then I perform DELETE request to delete single user successfully
    Then I verify that user_deleted event is created for lloyds_user
