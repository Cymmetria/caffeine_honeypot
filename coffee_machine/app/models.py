import json
from copy import copy
from uuid import uuid4

import config
from tea_exceptions import NoSuchThingy


class TeaCup(object):
    REDIS_PREFIX = 'teacup'
    DEFAULT_OPTIONS = {
        'type': 'tea'
    }

    @staticmethod
    def _generate_uuid():
        return str(uuid4())

    def __init__(self, options):
        self.id = options.get('id', self._generate_uuid())
        self.options = copy(self.DEFAULT_OPTIONS)
        self.options.update(options)
        self.options['id'] = self.id

    @classmethod
    def _get_redis_key(cls, teacup_id):
        return '%s_%s' % (cls.REDIS_PREFIX, teacup_id)

    def save(self):
        config.get_redis_conn().set(self._get_redis_key(self.id), json.dumps(self.options))

    @classmethod
    def get_by_id(cls, teacup_id):
        raw_data = config.get_redis_conn().get(cls._get_redis_key(teacup_id))

        if not raw_data:
            raise NoSuchThingy

        return cls(options=json.loads(raw_data))
