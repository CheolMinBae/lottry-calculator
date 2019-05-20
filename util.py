def loadData(f_name):
    data  = f_name.read().split("\n")
    print(data)
    data = data[:len(data)-1]
    label = []
    for i in range(len(data)):
        data[i] = data[i].split("\t")
        data[i] = [float(x) for x in data[i]]
        label.append(data[i][len(data[i])-1])
        data[i] = data[i][0:len(data[i])-1]
    return data[:-2],label[2:]  #Removing first two and last two so each X[i] tries to predict Y[i+2] (i've used i+2 and not to i+1 to force it to predict the future (O) )
