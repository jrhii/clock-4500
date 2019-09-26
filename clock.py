IN_FILE = "clock.in"
CLOCK_OFFSET = 100

#returns {before: {hour: 00, minute: 00}, after: {hour: 00, minute: 00}}
def getTimes(inFileStr):
    with open(inFileStr, 'r') as inFile:
        beforeTimeList = inFile.readline.strip().split(":")
        afterTimeList = inFile.readline.strip().split(":")

        return {
            "before": {
                "hour": beforeTimeList[0],
                "minute": beforeTimeList[1]
            },
            "after": {
                "hour": afterTimeList[0],
                "minute": afterTimeList[1]
            }
        }

#time: 0000, origin: {"x","y"}
def drawClock(time, origin)

#return 0000
def getDifference(beforeTime, afterTime):
    minutesDifference = afterTime["minute"] - beforeTime["minute"]
    hoursDifference = afterTime["hour"] - beforeTime["hour"]

    #if minutes is neg, add 60 and subtract from hours
    #if hours is neg, add 24

    return 0

times = getTimes(IN_FILE)

timeDiff = getDifference(times["before"], times["after"])

drawClock(times["before"], {"x": 0, "y": 0})
drawClock(time["after", {"x": 0, "y": CLOCK_OFFSET}])
drawClock(timeDiff, {"x": 0, "y": CLOCK_OFFSET * 2})