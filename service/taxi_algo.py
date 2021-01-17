class TaxiAlgo:
    NIGHT_SURCHARGE = 1.5

    def calcFare(self, data):
        sum_cost = 0
        sum_distance = self.sumDistance(data)
        print("total distance is " + str(sum_distance) + "m")
        sum_cost += self.distanceCost(sum_distance)
        print("distance cost is " + str(sum_cost) + " yen")
        sum_low_speed_time = self.sumLowSpeedTime(data)
        sum_cost += self.lowSpeedTimeCost(sum_low_speed_time)
        print("lowspeedtime cost is " + str(self.lowSpeedTimeCost(sum_low_speed_time)) + " yen")
        return sum_cost

    def sumLowSpeedTime(self, data):
        sum_low_speed_time = 0
        for i in range(1, len(data)):
            speed_per_hour, hourA, hourB, secondA, secondB = self.timeConf(data, i)
            if speed_per_hour <= 10.0:
                time_status = self.isNightSurcharge(hourA, hourB)
                if time_status == "Night":
                    sum_low_speed_time += (secondB - secondA) * self.NIGHT_SURCHARGE
                elif time_status == "Price increase":
                    coefficient = hourA // 24
                    sum_low_speed_time += ((22.0 + coefficient * 24) * 3600 - secondA)
                    sum_low_speed_time += (secondB - (22.0 + coefficient * 24) * 3600) * self.NIGHT_SURCHARGE
                elif time_status == "Price decrease":
                    coefficient = hourA // 24
                    sum_low_speed_time += ((5.0 + coefficient * 24) * 3600 - secondA) * self.NIGHT_SURCHARGE
                    sum_low_speed_time += (secondB - (5.0 + coefficient * 24) * 3600)
                else:
                    sum_low_speed_time += (secondB - secondA)
        return sum_low_speed_time

    def sumDistance(self, data):
        total_distance = 0
        for i in range(1, len(data)):
            time_status = self.isNightSurcharge(int(data[i - 1].split(" ")[0].split(":")[0]), int(data[i].split(" ")[0].split(":")[0]))
            if time_status == "Night":
                total_distance += float(data[i].split(" ")[1]) * self.NIGHT_SURCHARGE
            elif time_status == "Price increase":
                speed_per_hour, hourA, hourB, secondA, secondB = self.timeConf(data, i)
                coefficient = hourA // 24
                total_distance += speed_per_hour * ((22.0 + coefficient * 24) * 3600 - secondA) / 3600 * 1000
                total_distance += speed_per_hour * (secondB - (22.0 + coefficient * 24) * 3600) / 3600 * self.NIGHT_SURCHARGE * 1000
            elif time_status == "Price decrease":
                speed_per_hour, hourA, hourB, secondA, secondB = self.timeConf(data, i)
                coefficient = hourB // 24
                total_distance += speed_per_hour * ((5.0 + coefficient * 24) * 3600 - secondA) / 3600 * self.NIGHT_SURCHARGE * 1000
                total_distance += speed_per_hour * (secondB - (5.0 + coefficient * 24) * 3600) / 3600 * 1000
            else:
                total_distance += float(data[i].split(" ")[1])
        return total_distance

    def lowSpeedTimeCost(self, sum_low_speed_time):
        sum_low_speed_time_cost = 0.0
        sum_low_speed_time -= 90.0
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

    def timeConf(self, data, i):
        time_arrayA = data[i - 1].split(" ")[0].split(":")
        secondA = float(time_arrayA[0]) * 3600 + float(time_arrayA[1]) * 60 + float(time_arrayA[2])
        time_arrayB = data[i].split(" ")[0].split(":")
        secondB = float(time_arrayB[0]) * 3600 + float(time_arrayB[1]) * 60 + float(time_arrayB[2])
        distance = float(data[i].split(" ")[1]) / 1000
        speed_per_hour = distance / (secondB - secondA) * 3600
        return speed_per_hour, int(time_arrayA[0]), int(time_arrayB[0]), secondA, secondB

    def isNightSurcharge(self, before_hour, after_hour):
        if ((before_hour % 24) < 5 or (before_hour % 24) >= 22) and ((after_hour % 24) < 5 or (after_hour % 24) >= 22):
            return "Night"
        elif (after_hour % 24) < 5 or (after_hour % 24) >= 22:
            return "Price increase"
        elif (before_hour % 24) < 5 or (before_hour % 24) >= 22:
            return "Price decrease"
        else:
            return "notNight"
