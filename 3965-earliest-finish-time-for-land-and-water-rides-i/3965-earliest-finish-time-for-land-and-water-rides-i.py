class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        minTime = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Land first
                endLand = landStartTime[i] + landDuration[i]
                startWater = max(waterStartTime[j], endLand)
                endWater = startWater + waterDuration[j]

                # Water first
                endWaterFirst = waterStartTime[j] + waterDuration[j]
                startLand = max(landStartTime[i], endWaterFirst)
                endLandSecond = startLand + landDuration[i]

                totalTime = min(endWater, endLandSecond)
                minTime = min(minTime, totalTime)

        return minTime