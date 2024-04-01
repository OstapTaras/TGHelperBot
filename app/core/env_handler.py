import os

from dataclasses import dataclass

@dataclass
class Environment:
    TOKEN: str

def load_env():

    if os.environ.get('ENVIRONMENT') == 'LOCAL':
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.__file__)), '.env')
        load_dotenv(env_path)

    return Environment(
        TOKEN=os.environ.get('TOKEN')
    )
