class TaxiAlgo:

    def fileLoader(self):
        f = open('test2.txt', 'r', encoding='UTF-8')
        data = f.read().split("\n")
        f.close()
        return data

    def sumDistance(self, data):
        total_distance = 0
        for i in range(1, len(data)):
            time_status = self.isNightSurcharge(int(data[i - 1].split(" ")[0].split(":")[0]), int(data[i].split(" ")[0].split(":")[0]))
            if time_status == "Night":
                total_distance += float(data[i].split(" ")[1]) * 1.5
            elif time_status == "Price increase":

                time_arrayA = data[i - 1].split(" ")[0].split(":")
                secondA = float(time_arrayA[0]) * 3600 + float(time_arrayA[1]) * 60 + float(time_arrayA[2])
                time_arrayB = data[i].split(" ")[0].split(":")
                secondB = float(time_arrayB[0]) * 3600 + float(time_arrayB[1]) * 60 + float(time_arrayB[2])
                distance = float(data[i].split(" ")[1]) / 1000
                speed_per_hour = distance / (secondB - secondA) * 3600

                coefficient = int(time_arrayA[0]) / 24 + 1
                total_distance += speed_per_hour * (22.0 * 3600 * coefficient - secondA) / 3600
                total_distance += speed_per_hour * (secondB - 22.0 * 3600 * coefficient) / 3600 * 1.5
            elif time_status == "Price increase":
                time_arrayA = data[i - 1].split(" ")[0].split(":")
                secondA = float(time_arrayA[0]) * 3600 + float(time_arrayA[1]) * 60 + float(time_arrayA[2])
                time_arrayB = data[i].split(" ")[0].split(":")
                secondB = float(time_arrayB[0]) * 3600 + float(time_arrayB[1]) * 60 + float(time_arrayB[2])
                distance = float(data[i].split(" ")[1]) / 1000
                speed_per_hour = distance / (secondB - secondA) * 3600

                coefficient = time_arrayB[0] / 24 + 1
                total_distance += speed_per_hour * (5.0 * 3600 * coefficient - secondA) / 3600 * 1.5
                total_distance += speed_per_hour * (secondB - 5.0 * 3600 * coefficient) / 3600
            else:
                total_distance += float(data[i].split(" ")[1])

        return total_distance

    def isNightSurcharge(self, before_hour, after_hour):
        if ((before_hour % 24) < 5 or (before_hour % 24) >= 22) and ((after_hour % 24) < 5 or (after_hour % 24) >= 22):
            return "Night"
        elif (after_hour % 24) < 5 or (after_hour % 24) >= 22:
            return "Price increase"
        elif (before_hour % 24) < 5 or (before_hour % 24) >= 22:
            return "Price decrease"
        else:
            return "notNight"

    def costCalc(self, data):
        sum_cost = 0
        sum_distance = self.sumDistance(data)
        print(sum_distance)
        print(sum_distance)
        sum_cost += self.distanceCost(sum_distance)
        print(sum_cost)
        sum_cost += self.sumLowSpeedTimeCost(data)
        return sum_cost

    def sumLowSpeedTimeCost(self, data):
        sum_low_speed_time = 0
        sum_low_speed_time_cost = 0.0
        for i in range(1, len(data)):
            time_arrayA = data[i - 1].split(" ")[0].split(":")
            secondA = float(time_arrayA[0]) * 3600 + float(time_arrayA[1]) * 60 + float(time_arrayA[2])
            time_arrayB = data[i].split(" ")[0].split(":")
            secondB = float(time_arrayB[0]) * 3600 + float(time_arrayB[1]) * 60 + float(time_arrayB[2])
            distance = float(data[i].split(" ")[1]) / 1000
            speed_per_hour = distance / (secondB - secondA) * 3600

            if speed_per_hour < 10.0:
                if self.isNightSurcharge(int(time_arrayA[0]), int(time_arrayB[0])):
                    sum_low_speed_time += (secondB - secondA) * 1.5
                else:
                    sum_low_speed_time += (secondB - secondA)

        while sum_low_speed_time > 0:
            sum_low_speed_time -= 90.0
            sum_low_speed_time_cost += 80
        return sum_low_speed_time_cost

    def distanceCost(self, sum_distance):
        distance_cost = 410
        if sum_distance <= 1052.0:
            return distance_cost
        sum_distance -= 1052.0
        while sum_distance > 0:
            sum_distance -= 237.0
            distance_cost += 80
        return distance_cost


Algo = TaxiAlgo()
data = Algo.fileLoader()

sum_cost = Algo.costCalc(data)
print(sum_cost)

