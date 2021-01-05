import service
import sys

for i in range(1, 5):
    taxiAlgo = service.taxi_algo.TaxiAlgo()
    drive_log = service.file_loader.loadByPath("src/test" + str(i) + ".txt")
    try :
        sum_cost = taxiAlgo.costCalc(drive_log)
        print(sum_cost)
    except:
        print("!!! ExecutionError !!!")
        sys.exit("Error")

