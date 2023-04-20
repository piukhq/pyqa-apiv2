import datetime
import logging

from dataclasses import dataclass

import tests.helpers.database.setupdb as db

from tests.helpers.test_context import TestContext


@dataclass
class EventRecord:
    id: int
    event_date_time: datetime.datetime
    event_type: str
    json: bool


class QuerySnowstorm:
    @staticmethod
    def fetch_event(journey_type, external_id):
        """Fetch the event using scheme account id"""
        connection = db.connect_snowstorm_db()
        record = db.execute_query_fetch_one(connection, get_user_created_event(journey_type, external_id))

        if record is None:
            raise Exception(f"Record not found for {external_id}")
        else:
            event_record = EventRecord(record[0], record[1], record[2], record[3])
        db.clear_db(connection)
        return event_record


def get_user_created_event(journey_type, external_id):
    if journey_type == "":
        logging.info("Scheme did not attach to the wallet")
    elif TestContext.environ == "staging":
        if journey_type == "user_created":
            query_event_record = (
                """SELECT id, event_date_time, event_type, json
                           FROM snowstorm.public.events
                           WHERE event_type = 'user.created'
                           AND json ->> 'external_user_ref' = '%s'"""
                % external_id
            )
        elif journey_type == "user_deleted":
            query_event_record = (
                """SELECT id, event_date_time, event_type, json
                               FROM snowstorm.public.events
                               WHERE event_type = 'user.deleted'
                               AND json ->> 'external_user_ref' = '%s'"""
                % external_id
            )

    return query_event_record
