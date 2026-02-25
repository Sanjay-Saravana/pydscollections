from abc import ABC, abstractmethod

class Collections(ABC):

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass