import util
import random
import numpy as np
# 자동 뽑은 것들 중에 풀랜덤 5개
# 10회 당첨 내용 중에 안나온 것, 많이 나온 것 조합
class NumberCnt:
  def __init__(self, number, cnt):
    self.number = number
    self.cnt = cnt

  def updateCnt (self, cnt):
    self.cnt = cnt

  def getCnt (self):
    return self.cnt

file_name = 'data.csv'
unique_numbers = []
number_cnt_array = []
d = open(file_name, 'r')
data, labels = util.loadData(d)
data = np.int_(data)
for i in range(46):
  number_cnt_array.append(NumberCnt(i, 0))


for x in range(len(data)):
    for y in range(len(data[x])):
      numbersCnt = number_cnt_array[data[x][y]].getCnt()
      number_cnt_array[data[x][y]].updateCnt(numbersCnt + 1)
      if data[x][y] not in unique_numbers:
        unique_numbers.append(data[x][y])

print("random paper's full random combination!")
for z in range(5):
  ran_numbers = random.sample(unique_numbers, k=6)
  print(sorted(ran_numbers))

print("python random.sample combination")
for i in range(5):
  print(sorted(random.sample(range(1,45), 6)))

# for j in range(len(number_cnt_array)):
#   print("number %d's CNT: %d" % (j,number_cnt_array[j].getCnt()))
# ran_numbers = random.sample(unique_numbers, k=6)

# print(ran_numbers)
