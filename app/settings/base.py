from abc import ABC, abstractmethod

class BaseSettings(ABC):
    @property
    @abstractmethod
    def DATABASE_URL(self):
        pass

    @property
    @abstractmethod
    def LOG_LEVEL(self):
        pass
