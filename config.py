import yaml
import os

import trafaret as t

ROOT_PATH = os.getcwd()
CONFIG_PATH = os.environ.get("CONFIG_PATH") or ROOT_PATH + "/configs/config-test.yaml"

schema = t.Dict(
    accessing=t.Dict(
        user_key=t.String,
        service_url=t.URL,
    ),
    namespaces=t.Dict(
        bir=t.String,
        pb=t.String,
    ),
)


def get_config(path=CONFIG_PATH):
    with open(path) as config:
        config = yaml.safe_load(config)
        schema.check(config)
        return config


CONFIG = get_config()
