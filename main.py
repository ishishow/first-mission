import service
import sys

answer = [1050, 970, 810, 490, 970, 810, 490, 490, 410, 970, 810, 490]

for i in range(1, 13):
    taxiAlgo = service.taxi_algo.TaxiAlgo()
    drive_log = service.file_loader.loadByPath("test/test" + str(i) + ".txt")
    try :
        print("------------------test" + str(i) + "-------------------")
        sum_cost = taxiAlgo.calcFare(drive_log)
        print(int(sum_cost))
        print(int(sum_cost) == answer[i - 1], "\n")
    except:
        print("!!! ExecutionError !!!")
        sys.exit("Error")

