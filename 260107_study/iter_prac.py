
class Season:
    def __init__(self):
        self.data =["봄", "여름", "가을", "겨울"]
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            cur_season = self.data[self.index]
            self.index +=1
            return cur_season
        else:
            raise StopIteration
        
s = Season()
ir = iter(s)
print(next(ir))
print(next(ir))
print(next(ir))

def add_1(n):
    return n + 1

target = [1, 2, 3, 4, 5]

result = map(add_1, target)

print(list(result))
