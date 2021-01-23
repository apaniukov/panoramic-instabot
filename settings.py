from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union


@dataclass
class Settings:
    bot_token: Optional[str]

    @classmethod
    def from_env_file(cls, path: Union[str, Path]) -> "Settings":
        with open(path) as f:
            config = {}
            for line in f:
                key, val = line.rsplit("=", 1)
                config[key] = val

        return cls(**config)


config = Settings.from_env_file(".env")
