from typing import Optional


class ObjList:
    __next: Optional["ObjList"]
    __prev: Optional["ObjList"]
    __data: str
    def __init__(self, data) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    def get_next(self) -> "ObjList":
        return self.__next

    def set_next(self, obj: "ObjList"):
        self.__next = obj

    def get_prev(self) -> "ObjList":
        return self.__prev

    def set_prev(self, obj: "ObjList"):
        self.__prev = obj

    def get_data(self) -> str:
        return self.__data

    def set_data(self, data: str):
        self.__data = data
