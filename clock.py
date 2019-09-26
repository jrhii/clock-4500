IN_FILE = "clock.in"
CLOCK_OFFSET = 100

#returns {before: 0000, after: 0000}
def getTimes(inFileStr)

#time: 0000, origin: {"x","y"}
def drawClock(time, origin)

def getDifference(beforeTime, afterTime)

times = getTimes(IN_FILE)

timeDiff = getDifference(times["before"], times["after"])

drawClock(times["before"], {"x": 0, "y": 0})
drawClock(time["after", {"x": 0, "y": CLOCK_OFFSET}])
drawClock(timeDiff, {"x": 0, "y": CLOCK_OFFSET * 2})