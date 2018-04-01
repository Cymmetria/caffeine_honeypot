import json
from time import sleep
from decoy_config import get_decoy
import config

REPORTING_INTERVAL_SECONDS = 10

decoy = get_decoy()

while True:
    configuration = decoy.report_status().json().get('configuration')

    if configuration:
        print 'reporting...'
        parsed_config = json.loads(configuration).get('configuration_uuid')
        config.set_configuration_uuid(parsed_config)

    sleep(REPORTING_INTERVAL_SECONDS)
