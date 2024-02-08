# import logging
# import time

# from pytest_bdd import parsers, scenarios, then, when

# from tests.helpers import constants
# from tests.helpers.database.query_snowstorm import QuerySnowstorm
# from tests.helpers.test_context import TestContext
# from tests.helpers.test_data_utils import TestDataUtils
# from tests.requests.service import CustomerAccount
# from tests.step_definitions import test_loyalty_cards, test_paymentcard_account

# scenarios("events/")

# """Step definitions - Events """


# # @when(parsers.parse('I perform POST request to add "{merchant}" membership card'))
# # def add_field_loyalty_cards(merchant):
# #     test_loyalty_cards.add_field_loyalty_cards(merchant)


# # @when(
# #     parsers.parse(
# #         'I perform POST request to add and auth "{merchant}" {membership_card} '
# #         'with "{request_payload}" with "{status_code}"'
# #     )
# # )
# # def event_verify_invalid_request_for_add_and_auth_journey(merchant, membership_card, request_payload, status_code):
# #     test_loyalty_cards.verify_invalid_request_for_add_and_auth_journey(
# #         merchant, membership_card, request_payload, status_code
# #     )

# # @when(parsers.parse('I add and authorise "{merchant}" membership card'))
# # def post_add_and_auth(merchant):
# #     test_loyalty_cards.verify_add_and_auth(merchant)


# # @when(parsers.parse('I perform PUT request to authorise "{merchant}" above wallet only membership card'))
# # def authorise_post_membership_card(merchant):
# #     test_loyalty_cards.verify_authorise_post_membership_card(merchant)


# # @when(parsers.parse('I perform {scheme_state} POST request to join "{merchant}" membership card'))
# # def fail_join_scheme(scheme_state, merchant):
# #     test_loyalty_cards.fail_join_scheme(scheme_state, merchant)


# # @when(
# #     parsers.parse(
# #         'I perform POST request to add a {payment_status} "{payment_card_provider}" payment account to wallet'
# #     )
# # )
# # def add_payment_card_event(payment_card_provider, payment_status):
# #     test_paymentcard_account.add_payment_account(payment_card_provider, payment_status)


# # @when(parsers.parse('I perform POST request to add existing payment card "{payment_card_provider}" second wallet'))
# # def event_add_existing_payment_cardpayment_card_provider(payment_card_provider):
# #     test_paymentcard_account.add_existing_payment_card_in_another_wallet(payment_card_provider)


# # @when(parsers.parse('I perform POST request to {join} "{merchant}" membership card'))
# # def join_scheme(join, merchant, test_email):
# #     test_loyalty_cards.join_scheme(join, merchant, test_email)


# # @then(parsers.parse('verify that for {user} data stored in after {journey_type} journey for "{merchant}"'))
# # def verify_loyalty_card_into_database_trusted(user, journey_type, merchant):
# #     test_loyalty_cards.verify_loyalty_card_into_database_trusted(user, journey_type, merchant)


# @then(parsers.parse("I verify that {journey_type} event is created for {user}"))
# def verify_loyalty_card_into_event_database(journey_type, user):
#     TestContext.extid = TestContext.external_id[user]
#     time.sleep(5)
#     logging.info(TestDataUtils.TEST_DATA.event_type.get(journey_type))
#     event_record = QuerySnowstorm.fetch_event(TestDataUtils.TEST_DATA.event_type.get(journey_type), TestContext.extid)
#     logging.info(str(event_record))

#     assert (
#         event_record.event_type == TestDataUtils.TEST_DATA.event_type.get(journey_type)
#         and event_record.json["external_user_ref"] == TestContext.extid
#         and event_record.json["channel"] == TestDataUtils.TEST_DATA.event_info.get(constants.CHANNEL_LLOYDS)
#         and event_record.json["email"] == TestContext.email
#     )
#     return event_record


# @then(parsers.parse("I verify {journey_type} loyalty scheme event is created for {user}"))
# def verify_scheme_into_event_database(journey_type, user):
#     match user:
#         case "lloyds_user":
#             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CHANNEL_LLOYDS)
#         case "halifax_user":
#             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CHANNEL_HALIFAX)
#         case "bos_user":
#             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CHANNEL_BOS)
#         case "bink_user":
#             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CHANNEL_BINk)
#     TestContext.extid = TestContext.external_id[user]
#     time.sleep(5)
#     logging.info(TestDataUtils.TEST_DATA.event_type.get(journey_type))
#     TestContext.event_record = QuerySnowstorm.fetch_event(
#         TestDataUtils.TEST_DATA.event_type.get(journey_type), TestContext.extid
#     )
#     logging.info(str(TestContext.event_record))
#     assert TestContext.event_record.event_type == TestDataUtils.TEST_DATA.event_type.get(
#         journey_type
#     ), "event type do not match"
#     assert TestContext.event_record.json["external_user_ref"] == TestContext.extid, "external_user_ref do not match"
#     assert TestContext.event_record.json["channel"] == channel, "channel do not match"
#     assert TestContext.event_record.json["email"] == TestContext.user_email, "email do not match"
#     assert (
#         TestContext.event_record.json["scheme_account_id"] == TestContext.current_scheme_account_id
#     ), "scheme_account_id do not match"

#     return TestContext.event_record


# # @then(parsers.parse("I perform DELETE request to delete single user successfully"))
# # def delete_user_successfully(channel, env):
# #     response = CustomerAccount.delete_user(TestContext.token)
# #     assert response.status_code == 202, "The user deletion is not successful"
# #     logging.info("User is deleted successfully from the system")


# # @then(parsers.parse("verify consent in {journey_type} for {user} for {merchant}"))
# # def consent_in_event(journey_type, user, merchant):
# #     match journey_type:
# #         case journey_type if journey_type in ["lc_join_success", "lc_register_success"]:
# #             assert (
# #                 TestContext.event_record.json["consents"][0]["slug"] == TestDataUtils.TEST_DATA.consent_slug[merchant]
# #             ), f"consent slug do not match for {merchant}"
# #             assert (
# #                 TestContext.event_record.json["consents"][0]["response"] is True
# #             ), f"consent response do not match for {merchant}"


# # @when(parsers.parse("I perform POST request add and register for {merchant}"))
# # def add_and_register_field(merchant, test_email):
# #     test_loyalty_cards.add_and_register_field(merchant, test_email)


# # @when(parsers.parse("I perform POST request to add {merchant} membership card before {scheme_state} register"))
# # def add_before_register_field_loyalty_cards(merchant, scheme_state):
# #     test_loyalty_cards.add_before_register_field_loyalty_cards(merchant, scheme_state)


# # @when(parsers.parse("I perform PUT request to register {merchant} with {invalid_data} membership card"))
# # def verify_register_post_membership_card(merchant, invalid_data, test_email):
# #     test_loyalty_cards.verify_register_post_membership_card(merchant, invalid_data, test_email)


# # @when(parsers.parse('I perform POST request to result "{invalid_register}" add and register for {merchant}'))
# # def failed_add_and_register_field(invalid_register, merchant, test_email):
# #     test_loyalty_cards.failed_add_and_register_field(invalid_register, merchant, test_email)


# # @then(
# #     parsers.parse(
# #         "I verify {journey_type} pll event is created for {user} for status {from_state}"
# #         " to {to_state} and slug {slug}"
# #     )
# # )
# # def pll_link_status_change_event(journey_type, user, from_state, to_state, slug):
# #     match user:
# #         case "lloyds_user":
# #             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CLIENT_ID_LLOYDS)
# #         case "halifax_user":
# #             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CLIENT_ID_HALIFAX)
# #         case "bos_user":
# #             channel = TestDataUtils.TEST_DATA.event_info.get(constants.CLIENT_ID_BOS)
# #     TestContext.extid = TestContext.external_id[user]
# #     if slug == "null":
# #         TestContext.event_slug = ""
# #     else:
# #         TestContext.event_slug = slug
# #     time.sleep(8)
# #     logging.info(TestDataUtils.TEST_DATA.event_type.get(journey_type))
# #     TestContext.event_record = QuerySnowstorm.fetch_pll_event(
# #         TestDataUtils.TEST_DATA.event_type.get(journey_type),
# #         TestContext.extid,
# #         TestContext.event_slug,
# #     )
# #     logging.info(str(TestContext.event_record))
# #     assert TestContext.event_record.event_type == TestDataUtils.TEST_DATA.event_type.get(
# #         journey_type
# #     ), "event type do not match"
# #     assert TestContext.event_record.json["external_user_ref"] == TestContext.extid, "external_user_ref do not match"
# #     assert TestContext.event_record.json["channel"] == channel, "channel do not match"
# #     assert TestContext.event_record.json["email"] == TestContext.user_email, "email do not match"
# #     assert (
# #         TestContext.event_record.json["scheme_account_id"] == TestContext.current_scheme_account_id
# #     ), "scheme_account_id do not match"
# #     if slug == "null":
# #         assert TestContext.event_record.json["slug"] == "", "slug do not match"
# #     else:
# #         assert TestContext.event_record.json["slug"] == slug, "slug do not match"
# #     if from_state == "null":
# #         assert TestContext.event_record.json["from_state"] is None, "from_state do not match"
# #     else:
# #         assert TestContext.event_record.json["from_state"] == int(from_state), "from_state do not match"
# #     if to_state == "null":
# #         assert TestContext.event_record.json["to_state"] is None, "to_state do not match"
# #     else:
# #         assert TestContext.event_record.json["to_state"] == int(to_state), "to_state do not match"

# #     return TestContext.event_record
