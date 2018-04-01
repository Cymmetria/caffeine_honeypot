import os
import redis

REDIS_CONFIGURATION_UUID_KEY = 'configuration_uuid'

MAZERUNNER_URL = os.environ.get('MAZERUNNER_URL')
DECOY_ID = os.environ.get('DECOY_ID')
COMMUNICATION_KEY = os.environ.get('COMMUNICATION_KEY')


def get_redis_conn():
    return redis.StrictRedis(host='localhost', port=6379, db=0)


def set_configuration_uuid(configuration_uuid):
    get_redis_conn().set(REDIS_CONFIGURATION_UUID_KEY, configuration_uuid)


def get_configuration_uuid():
    return get_redis_conn().get(REDIS_CONFIGURATION_UUID_KEY) or \
           '12345678-1234-1234-1234-123456789abc'
