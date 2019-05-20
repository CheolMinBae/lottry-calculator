def loadData(f_name):
    data  = f_name.read().split("\n")
    data = data[:len(data)-1]
    label = []
    for i in range(len(data)):
        data[i] = data[i].split("\t")
        data[i] = [float(x) for x in data[i]]
        label.append(data[i][len(data[i])-1])
        data[i] = data[i][0:len(data[i])-1]

    return data[:-2],label[2:]  #Removing first two and last two so each X[i] tries to predict Y[i+2] (i've used i+2 and not to i+1 to force it to predict the future (O) )
def loadResultData(f_name):
    data  = f_name.read().split("\n")
    data = data[:len(data)-1]
    label = []
    for i in range(len(data)):
        data[i] = data[i].split(",")
        data[i] = [float(x) for x in data[i]]
        label.append(data[i][len(data[i])-1])
        data[i] = data[i][0:len(data[i])-1]

    return data[:-2],label[2:]  #Removing first two and last two so each X[i] tries to predict Y[i+2] (i've used i+2 and not to i+1 to force it to predict the future (O) )
def getMaxCnt(array):
    max = 0
    max_numbers = []
    for i in range(len(array)):
        max =  array[i].getCnt() if max < array[i].getCnt() else max
    for j in range(len(array)):
        if array[j].getCnt() == max:
            max_numbers.append(array[j].number)
    
    return max, max_numbers
def getMinCnt(array):
    cnt_array = []
    min_numbers = []
    for i in range(len(array)):
        if array[i].number != 0:
            cnt_array.append(array[i].getCnt())

    cnt_array = sorted(cnt_array)
    min = cnt_array[0]
    for j in range(len(array)):
        if array[j].number == 0:
            array[j].updateCnt(min)
        else:
            if array[j].getCnt() == min:
                min_numbers.append(array[j].number)
    return min, min_numbers
def exceptionMaxMinData(array, max, min):
    exception_array = []
    for i in range(len(array)):
        if array[i].getCnt() > min and array[i].getCnt() < max:
            exception_array.append(array[i].number)
    return exception_array