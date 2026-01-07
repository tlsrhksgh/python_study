# 딕셔너리
# 1.딕셔너리 {"a": 1, "b": 2}에서 key "a"의 값을 출력하라.
a = {"a": 1, "b": 2}
print(a["a"])

# 2.딕셔너리 {"a": 1}에 "b": 2를 추가하여 출력하라.
a = {"a": 1}
a["b"] = 2
print(a)

# 3.딕셔너리 {"a": 1, "b": 2}에서 모든 key를 출력하라.
a = {"a": 1, "b": 2}
print(*a.keys())

# 4.딕셔너리 {"a": 1, "b": 2}에서 모든 value를 출력하라.
print(*a.values())

# 5.딕셔너리 {"a": 1, "b": 2}에서 key "c"가 없으면 0을 출력하라.
print(a.get("c", 0))

# 6.딕셔너리 {"apple": 3, "banana": 5}에서 "apple"의 값을 10으로 변경하라.
a = {"apple": 3, "banana": 5}
a["apple"] = 10
print(a["apple"])

# 7.딕셔너리 {"a": 1, "b": 2}에서 key "b"를 삭제하라.
a = {"a": 1, "b": 2}
a.pop("b")
print(a)

# 8.딕셔너리의 모든 key와 value를 한 줄씩 출력하라.
a = a = {"a": 1, "b": 2, "c": 3}
for k, v in a.items():
    print(k, v)

# 9.리스트 [("a", 1), ("b", 2)]를 딕셔너리로 변환하여 출력하라.
a = [("a", 1), ("b", 2)]
for i in range(len(a)):
    a[i] = list(a[i])
print(a)

# 10.딕셔너리 {"a": 1, "b": 2, "c": 3}에서 value의 합을 출력하라.
a = {"a": 1, "b": 2, "c": 3}
print(sum(a.values()))