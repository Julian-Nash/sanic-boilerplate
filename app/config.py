from typing import Type
import enum

from sanic.config import Config


class ConfigEnum(enum.Enum):
    """ Enumeration of config names """
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class BaseConfig(Config):
    """ Shared config class """


class ProdConfig(Config):
    """ Production config """


class DevConfig(BaseConfig):
    """ Development config """


class TestConfig(BaseConfig):
    """ Testing config """


def get_config(name: str) -> Type[BaseConfig]:
    """ Returns the config class based on the config name, always defaults to the ProdConfig class """
    return {
        ConfigEnum.PROD.value: ProdConfig,
        ConfigEnum.DEV.value: DevConfig,
        ConfigEnum.TEST.value: TestConfig
    }.get(name, ProdConfig)
