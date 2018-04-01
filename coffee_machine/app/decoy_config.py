import config
from decoy import Decoy


def get_decoy():
    return Decoy(decoy_id=config.DECOY_ID,
                 communication_key=config.COMMUNICATION_KEY,
                 mazerunner_url=config.MAZERUNNER_URL,
                 mazerunner_config={
                     Decoy.REPORT_CONFIGURATION_UUID_PARAM: config.get_configuration_uuid()
                 })
