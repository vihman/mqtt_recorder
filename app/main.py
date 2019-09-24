
import logging
import paho.mqtt.client as mqtt

from .config import Config
from .db import insert_db

logger = logging.getLogger(__file__)

c = Config()


def on_disconnect(client, userdata, rc):
    logger.info("Disconnected from server with result code: %s " % str(rc))


def on_connect(client, userdata, flags, rc):
    logger.info("Connected to server {} with result code: {}".format(c['mqtt']['server'], str(rc)))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(c['topic'])


def on_message(client, userdata, msg):
    insert_db(msg)


def on_publish(client, userdata, mid):
    logger.info("published")


def make_client():
    m = mqtt.Client()
    m.enable_logger(logger)
    # client.tls_set(tls_version=ssl.PROTOCOL_TLSv1)
    m.tls_set()
    m.username_pw_set(c['mqtt']['user'], c['mqtt']['secret'])
    m.on_connect = on_connect
    m.on_message = on_message
    m.on_disconnect = on_disconnect
    m.on_publish = on_publish
    return m

def run():
    client = make_client()
    client.connect(c['mqtt']['server'], port=c['mqtt']['port'])
    client.loop_forever()
    """ 
    Blocking call that processes network traffic, dispatches callbacks and
    handles reconnecting. Other loop*() functions are available that give a threaded interface and a
    manual interface.
    """
    logger.info("Scheduler finished")