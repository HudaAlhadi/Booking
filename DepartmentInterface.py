from abc import ABC, abstractmethod


class DepartmentInterface(ABC):
    @abstractmethod
    def select_department(self):
        pass
