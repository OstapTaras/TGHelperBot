from dataclasses import dataclass

@dataclass
class Environment:
    TOKEN: str

def load_env():
    return Environment()
