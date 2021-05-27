# -*-coding:utf-8-*-


class SimpleClass(object):
    __instance = None
    stack = []

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance


simcla = SimpleClass("金毛")
simcla1 = SimpleClass('泰迪')
print(simcla, simcla1)
