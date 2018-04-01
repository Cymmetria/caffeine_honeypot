import json
import requests


class Decoy(object):
    REPORT_DECOY_ID_PARAM = 'decoy_id'
    REPORT_COMMUNICATION_KEY_PARAM = 'communication_key'
    REPORT_CONFIGURATION_UUID_PARAM = 'configuration_uuid'
    REPORT_ALERT_PARAM = 'alert'
    REPORT_LOG_PARAM = 'log'
    REPORT_LOG_LEVEL_PARAM = 'level'
    REPORT_LOG_LINE_PARAM = 'message'

    CONFIGURATION_COMMUNICATION_KEY_PARAM = 'communication_key'
    CONFIGURATION_CONFIGURATION_UUID_PARAM = 'configuration_uuid'

    def __init__(self, decoy_id, communication_key, mazerunner_url, mazerunner_config):
        self.decoy_id = decoy_id
        self.communication_key = communication_key
        self.mazerunner_url = mazerunner_url
        self.mazerunner_config = mazerunner_config

    def report_status(self):
        data = {
            self.REPORT_DECOY_ID_PARAM: self.decoy_id,
            self.REPORT_COMMUNICATION_KEY_PARAM: self.communication_key,
            self.REPORT_CONFIGURATION_UUID_PARAM: self.mazerunner_config.get(
                self.CONFIGURATION_CONFIGURATION_UUID_PARAM)
        }

        response = requests.post(
            url='%s/report_status/' % self.mazerunner_url,
            data=data
        )
        return response

    def report_log(self, line, level):
        response = requests.post(
            url='%s/report_log/' % self.mazerunner_url,
            data={
                self.REPORT_DECOY_ID_PARAM: self.decoy_id,
                self.REPORT_COMMUNICATION_KEY_PARAM: self.communication_key,
                self.REPORT_LOG_PARAM: {
                    self.REPORT_LOG_LEVEL_PARAM: level,
                    self.REPORT_LOG_LINE_PARAM: line
                }
            }
        )
        return response

    def report_alert(self, alert_data):
        response = requests.post(
            url='%s/report_alert/' % self.mazerunner_url,
            data={
                self.REPORT_DECOY_ID_PARAM: self.decoy_id,
                self.REPORT_COMMUNICATION_KEY_PARAM: self.communication_key,
                self.REPORT_ALERT_PARAM: json.dumps(alert_data)
            }
        )
        return response
