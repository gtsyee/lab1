from abc import ABC, abstractmethod
class Repository(ABC):
    @abstractmethod
    def add(self, item):
        pass
    @abstractmethod
    def get(self, item_id):
        pass
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def update(self, item):
        pass
    @abstractmethod
    def delete(self, item_id):
        pass
class MemoryRepository(Repository):
    def __init__(self):
        self._items = {}
        self._next_id = 1
    def add(self, item):
        if item.id is not None:
            raise ValueError("объект уже был сохранен")
        item.id = self._next_id
        self._items[item.id] = item
        self._next_id += 1
        return item
    def get(self, item_id):
        if item_id not in self._items:
            raise ValueError(f"объект с id {item_id} не найден")
        return self._items[item_id]
    def get_all(self):
        return list(self._items.values())
    def update(self, item):
        self.get(item.id)
        self._items[item.id] = item
        return item
    def delete(self, item_id):
        self.get(item_id)
        del self._items[item_id]