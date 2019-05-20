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
result_file_name = 'result.csv'
unique_numbers = []
number_cnt_array = []
d = open(file_name, 'r')
result = open(result_file_name, 'r')
data, labels = util.loadData(d)
resultData, resultLables = util.loadResultData(result)
data = np.int_(data)
resultData = np.int_(resultData)
for i in range(46):
  number_cnt_array.append(NumberCnt(i, 0))


for x in range(len(resultData)):
    for y in range(len(data[x])):
      numbersCnt = number_cnt_array[resultData[x][y]].getCnt()
      number_cnt_array[resultData[x][y]].updateCnt(numbersCnt + 1)
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
max, max_numbers = util.getMaxCnt(number_cnt_array)
min, min_numbers = util.getMinCnt(number_cnt_array)
exception_array = util.exceptionMaxMinData(number_cnt_array, max, min)
print(exception_array)
print("historical data combination")
for k in range(5):
  print(sorted(random.sample(exception_array, k=6)))
# print(ran_numbers)
period = 0
# 
while True:
  # tmp = sorted(random.sample(exception_array, k=6))
  # tmp = sorted(random.sample(unique_numbers, k=6))
  tmp = sorted(random.sample(range(1,45), 6))
  if np.array_equal(tmp, [8,22,35,38,39,41]) is True:
    print("lucky first!" + "{:,}".format(period))
    break
  elif period > 10000000:
    print('oh my god!')
    break
  else:
    period+=1
