# Created by braghavan on 28/03/2023
@user_created @events
Feature: Add and authorise a loyalty card
  As a DM Administrator
  I want to see an Event logged when a user is created
  so that this Business Event can be written to ClickHouse for validation

  @user_created_event @bink_regression_api2 @sandbox_regression @event
  Scenario: Verify event for user created
    Given I am a Lloyds user
    Then I verify that user_created event is created for lloyds_user

