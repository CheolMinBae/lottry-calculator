import util
import random
# 자동 뽑은 것들 중에 풀랜덤 5개
# 10회 당첨 내용 중에 안나온 것, 많이 나온 것 조합
file_name = 'data.csv'
unique_numbers = []
d = open(file_name, 'r')
data, labels = util.loadData(d)
print(data)
for x in range(len(data)):
    for y in range(len(data[x])):
      if data[x][y] not in unique_numbers:
        unique_numbers.append(data[x][y])
for z in range(5):
  ran_numbers = random.sample(unique_numbers, k=6)
  print(ran_numbers)
# ran_numbers = random.sample(unique_numbers, k=6)

# print(ran_numbers)
