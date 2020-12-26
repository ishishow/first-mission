class TaxiAlgo:

    def fileLoader(self):
        f = open('test.txt', 'r', encoding='UTF-8')
        data = f.read().split("\n")
        f.close()
        return data

    def sumDistance(self, data):
        total_distance = 0
        for i in range(1, len(data)):
            total_distance += float(data[i].split(" ")[1])

        return total_distance

    def costCalc(self, data):
        sum_cost = 0
        sum_distance = self.sumDistance(data)
        sum_cost += self.distanceCost(sum_distance)
        sum_cost += self.sumLowSpeedTimeCost(data)
        return sum_cost

    def sumLowSpeedTimeCost(self, data):
        sum_low_speed_time = 0
        sum_low_speed_time_cost = 0
        for i in range(1, len(data)):
            time_arrayA = data[i - 1].split(" ")[0].split(":")
            secondA = float(time_arrayA[0]) * 3600 + float(time_arrayA[1]) * 60 + float(time_arrayA[2])
            time_arrayB = data[i].split(" ")[0].split(":")
            secondB = float(time_arrayB[0]) * 3600 + float(time_arrayB[1]) * 60 + float(time_arrayB[2])
            distance = float(data[i].split(" ")[1]) / 1000
            speed_per_hour = distance / (secondB - secondA) * 3600

            if speed_per_hour < 10.0:
                sum_low_speed_time += (secondB - secondA)

        while sum_low_speed_time > 0:
            sum_low_speed_time -= 90.0
            sum_low_speed_time_cost += 80
        return sum_low_speed_time_cost

    def distanceCost(self, sum_distance):
        distance_cost = 410
        if sum_distance <= 1052.0:
            return
        sum_distance -= 1052.0
        while sum_distance > 0:
            sum_distance -= 237.0
            distance_cost += 80
        return distance_cost


Algo = TaxiAlgo()
data = Algo.fileLoader()

sum_cost = Algo.costCalc(data)
print(sum_cost)

# 	運賃
# 0 m を超え、1052 m 以下	410 円
# 1052 m を超え、1289 m 以下	490 円
# 1289 m を超え、1526 m 以下	570 円
# ...
