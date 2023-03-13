import time

import psutil


# ======================================================
# ======================== CPU =========================
# get cpu Frequency
def cpuFreqStat():
    rawData = psutil.cpu_freq()   # returns 3 data in 1 array (current, min, max)
    print(rawData)
    print(rawData[0] / 1000)      # converting to GHZ


# get cpu Core and Threads
def cpuCoreThreads():
    totalThreads = psutil.cpu_count()               # returns total number of Threads
    totalCore = psutil.cpu_count(logical=False)     # returns total number of Cores
    print(f"Total Cores:   {totalCore}")
    print(f"Total Threads: {totalThreads}")


# cpu Utilization it returns cpu usage.
def cpuUtilization():
    rawUtilize = psutil.cpu_percent(interval=1, percpu=False)
    Utilize = f"{int(rawUtilize)}%"
    print(Utilize)


# ======================================================
# ====================== Memory ========================

# gets the value of total memory/Ram size
def totalMemory():
    tMemory = psutil.virtual_memory()
    tMemory = tMemory[0] / 1024 / 1024 / 1024
    tMemory = f"{round(tMemory, 1)} GB"

    print(tMemory)


# gets the current memory/Ram usage
def usedMemory():
    uMemory = psutil.virtual_memory()
    uMemory = uMemory[3] / 1024 / 1024 / 1024
    uMemory = f"{round(uMemory, 1)} GB"

    print(uMemory)


# gets the value of total free/available memory
def freeMemory():
    fMemory = psutil.virtual_memory()
    fMemory = fMemory[1] / 1024 / 1024 / 1024
    fMemory = f"{round(fMemory, 1)} GB"

    print(fMemory)


# gets the percentage of memory
def memoryPercentage():
    pMemory = psutil.virtual_memory()
    pMemory = f"{pMemory[2]}%"

    print(pMemory)


# ======================================================
# ======================= Disk =========================
# detect all disk partitions
def diskPartitions():
    listOfDisks = []
    diskP = psutil.disk_partitions(all=False)
    for i in diskP:
        listOfDisks.append(i[0])

    return listOfDisks


# Get all the disk size
def diskUsage(path=None):
    returnData = []
    tempData = []

    if path is None:
        path = ['C://']

    for x in path:
        totalDisk = psutil.disk_usage(x)
        i = 0

        while i < len(x):
            size = round(totalDisk[i] / 1024 / 1024 / 1024, 1)
            if size > 1000:
                size = f"{size / 1000} TB"
            else:
                size = f"{size} GB"

            tempData.append(size)

            i += 1

        combineForASingleDisk = f"Total= {tempData[0]}, Used= {tempData[1]}, Free= {tempData[2]}, Percent= {totalDisk[3]}"
        returnData.append(combineForASingleDisk)
        print(combineForASingleDisk)
        tempData.clear()


        print("=========================================")




    # Main data
    # for x in path:
    #     totalDisk = psutil.disk_usage(x)
    #     # get the total size in GB
    #     size = round(totalDisk[0] / 1024 / 1024 / 1024, 1)
    #     # check data size
    #     if size > 1000:
    #         totalDisk = f"Disk {x[0:1]}: {size} TB"
    #     else:
    #         totalDisk = f"Disk {x[0:1]}: {size} GB"

        # returnData.append(totalDisk)
        # print(totalDisk)

    return returnData


if __name__ == "__main__":
    while True:
        cpuFreqStat()
        time.sleep(1)
    # data = diskPartitions()
    # y = diskUsage(data)
    # print(y)
