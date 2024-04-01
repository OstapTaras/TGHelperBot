import os

from dataclasses import dataclass


@dataclass
class Environment:
    TOKEN: str


def load_env():

    if os.environ.get('ENVIRONMENT') == 'LOCAL':
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.abspath(os.path.curdir), 'app', '.env')
        load_dotenv(env_path)

    return Environment(
        TOKEN=os.environ.get('TOKEN')
    )
