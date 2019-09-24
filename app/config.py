import os
import yaml


class Config:

    def __init__(self):
        CONFIG_FILE = os.environ.get('MQTT_RECORDER_CONFIG_FILE', 'config/mqtt_recorder.yml')
        with open(CONFIG_FILE) as f:
            self.values = yaml.load(f, Loader=yaml.SafeLoader)

    def __getitem__(self, item):
        return self.values[item]
