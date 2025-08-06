class Task(object):
    def __init__(self,name,func,callback):
        self.name=name
        # 单下划线：保护属性，外部可以访问，但是不建议访问
        self._func=func
        # 双下划线：私有属性，外部不能访问，建议通过方法访问
        self.__callback=callback
    @property
    def get_name(self):
        return self.name
    @classmethod
    def class_method(cls):
        print(f'{cls} class_method')

    @staticmethod
    def static_method():
        print(f'static_method')


    def to_be_inherited(self):
        print(f'to_be_inherited')


task=Task("task1",lambda x,y:x+y,lambda x,y:x+y)
print(task.get_name)
Task.class_method()
Task.static_method()
# task._func(1,2)
# task.__callback(1,2)


class Task2(Task):

    def __init__(self, name, func, callback):
        super().__init__(name, func, callback)
    def to_be_inherited(self):
        print(f'Task2 to_be_inherited')


task2=Task2("task2",lambda x,y:x+y,lambda x,y:x+y)
print(task2.get_name)
task2.to_be_inherited()