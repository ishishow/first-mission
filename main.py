import service

for i in range(1, 5):
    taxiAlgo = service.taxi_algo.TaxiAlgo()
    data = service.file_loader.fileLoader("src/test" + str(i) + ".txt")
    sum_cost = taxiAlgo.costCalc(data)
    print(sum_cost)

