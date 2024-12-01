from asyncore import read
import os
import argparse
import yaml
import logging
from src.utils.common_utils import read_params

def data_preparation(config_path, datasource):
    config = read_params(config_path=config_path)

    print(config)

  






if __name__ == '__main__':
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config","params.yaml")
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    
    try:
        data_preparation(config_path=parsed_args.config, datasource=parsed_args.datasource)
    except Exception as e:
        raise e


    


