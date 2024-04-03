numb = int(input())
result = {}
for i in range(1, numb + 1):
    result.update({i: i * i})
print(result)
