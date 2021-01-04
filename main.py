import service

taxiAlgo = service.taxi_algo.TaxiAlgo()
data = service.file_loader.fileLoader("src/test2.txt")

sum_cost = taxiAlgo.costCalc(data)
print(sum_cost)

taxiAlgo = service.taxi_algo.TaxiAlgo()
data = service.file_loader.fileLoader("src/test3.txt")

sum_cost = taxiAlgo.costCalc(data)
print(sum_cost)
