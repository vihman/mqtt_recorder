import logging
import psycopg2

from .config import Config

c = Config()

logger = logging.getLogger(__file__)


conn = psycopg2.connect("dbname={} user={} password={} host={}".format(c['db']['dbname'],
                                                                       c['db']['user'],
                                                                       c['db']['secret'],
                                                                       c['db']['server']
                                                                       )
                        )
cur = conn.cursor()


def insert_db(msg):
    topic = msg.topic
    payload = msg.payload.decode()
    try:
        cur.execute("INSERT INTO  mqtt_data (topic, data) "
                    "VALUES (%s, %s);", (topic, payload))
    except psycopg2.DataError as e:
        logger.error("Database insert error: %s" % str(e))
        conn.rollback()
    conn.commit()
