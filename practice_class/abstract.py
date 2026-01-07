from abc import *

class Car(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass

    def stop(self):
        pass

class K5(Car):
    # pass # 오류 발생 abstractmethod를 구현하지 않았기 때문
    def drive(self):
        pass

k5 = K5()