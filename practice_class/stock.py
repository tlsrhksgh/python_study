class Stock:
    def __init__(self):
        print("hello")
    
    def __getattribute__(self, name):
        print(name, "객체에 접근 하셨습니다.")


s = Stock()
s.asdf