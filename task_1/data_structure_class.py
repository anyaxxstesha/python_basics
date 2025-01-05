from task_1.item_class import ObjList


class LinkedList:
    def __init__(self, head=None, tail=None) -> None:
        self.head: ObjList | None = head
        self.tail: ObjList | None = tail

    def add_obj(self, obj: ObjList) -> None:
        """Добавление нового объекта obj класса ObjClass в конец связного списка"""
        if self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self) -> None:
        """Удаление последнего объекта из связного списка"""
        if self.head != self.tail:
            prev_obj = self.tail.get_prev()
            prev_obj.set_next(None)
            self.tail = prev_obj
        else:
            self.head = None
            self.tail = None

    def get_data(self) -> list[str]:
        """Получение списка из строк локального свойства __data всех объектов связного списка"""
        data = []
        if self.head:
            current_obj = self.head
            while current_obj.get_next():
                data.append(current_obj.get_data())
                current_obj = current_obj.get_next()
            data.append(current_obj.get_data())
        return data
