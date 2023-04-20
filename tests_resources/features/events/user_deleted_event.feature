# Created by npatil on 19/04/2023
@user_deleted @events
Feature: Add and authorise a loyalty card
  As a DM Administrator
  I want to see an Event logged when a user is deleted
  so that this Business Event can be written to ClickHouse for validation


  @user_deleted_event @bink_regression_api2
  Scenario Outline: Verify event for user created
    Given I am a Lloyds user
    Then I perform DELETE request to delete single user successfully
    Then verify that for lloyds_user the event created in database after <journey_type>

    Examples:
    |  journey_type  |
    | user_deleted   |
