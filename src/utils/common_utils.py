import yaml
import os
import shutil
import logging
import json
import pandas as pd


def read_params(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    # logging.info(f"Read the Parameters")
    return config