import operator
from .models import cpuset, ramset, diskset, outputset


def cpufuzzylogic(cpu):
    smallSet = []
    mediumSet = []
    largeSet = []
    inputsetwithdegrees = {}
    if cpu <= 0:
        not_available = 1.0
    else:
        not_available = 0.0

    x = float(40 - cpu) / float(40 - 20)
    smallSet.extend((x, 1))
    smallSetDegree = min(smallSet)
    if smallSetDegree < 0:
        smallSetDegree = 0.0
    inputsetwithdegrees['SMALL'] = smallSetDegree

    y = float(cpu - 20) / float(40 - 20)
    z = 1.0
    t = float(80 - cpu) / float(80 - 60)
    mediumSet.extend((y, z, t))
    mediumsetdegree = min(mediumSet)
    if mediumsetdegree < 0:
        mediumsetdegree = 0.0
    inputsetwithdegrees['MEDIUM'] = mediumsetdegree

    y = float(cpu - 60.) / float(80 - 60)
    z = 1.0
    largeSet.extend((y, z))
    largesetdegree = min(largeSet)
    if largesetdegree < 0:
        largesetdegree = 0.0
    inputsetwithdegrees['LARGE'] = largesetdegree
    cpuset.objects.create(SMALL=inputsetwithdegrees['SMALL'], MEDIUM=inputsetwithdegrees['MEDIUM'],
                          LARGE=inputsetwithdegrees['LARGE'])
    return inputsetwithdegrees


def ramfuzzylogic(ram):
    smallSet = []
    mediumSet = []
    largeSet = []
    inputsetwithdegrees = {}
    if ram <= 0:
        not_available = 1.0
    else:
        not_available = 0.0

    x = float(40 - ram) / float(40 - 20)
    smallSet.extend((x, 1))
    smallSetDegree = min(smallSet)
    if smallSetDegree < 0:
        smallSetDegree = 0.0
    inputsetwithdegrees['SMALL'] = smallSetDegree

    y = float(ram - 20) / float(40 - 20)
    z = 1.0
    t = float(80 - ram) / float(80 - 60)
    mediumSet.extend((y, z, t))
    mediumsetdegree = min(mediumSet)
    if mediumsetdegree < 0:
        mediumsetdegree = 0.0
    inputsetwithdegrees['MEDIUM'] = mediumsetdegree

    y = float(ram - 60.) / float(80 - 60)
    z = 1.0
    largeSet.extend((y, z))
    largesetdegree = min(largeSet)
    if largesetdegree < 0:
        largesetdegree = 0.0
    inputsetwithdegrees['LARGE'] = largesetdegree

    ramset.objects.create(SMALL=inputsetwithdegrees['SMALL'], MEDIUM=inputsetwithdegrees['MEDIUM'],
                          LARGE=inputsetwithdegrees['LARGE'])
    return inputsetwithdegrees


def diskfuzzylogic(disk):
    smallSet = []
    mediumSet = []
    largeSet = []
    inputsetwithdegrees = {}
    if disk <= 0:
        not_available = 1.0
    else:
        not_available = 0.0
    x = float(40 - disk) / float(40 - 20)
    smallSet.extend((x, 1))
    smallSetDegree = min(smallSet)
    if smallSetDegree < 0:
        smallSetDegree = 0.0

    inputsetwithdegrees['SMALL'] = smallSetDegree

    y = float(disk - 20) / float(40 - 20)
    z = 1.0
    t = float(80 - disk) / float(80 - 60)
    mediumSet.extend((y, z, t))
    mediumsetdegree = min(mediumSet)
    if mediumsetdegree < 0:
        mediumsetdegree = 0.0
    inputsetwithdegrees['MEDIUM'] = mediumsetdegree
    y = float(disk - 60.) / float(80 - 60)
    z = 1.0
    largeSet.extend((y, z))

    largesetdegree = min(largeSet)
    if largesetdegree < 0:
        largesetdegree = 0
    inputsetwithdegrees['LARGE'] = largesetdegree
    print inputsetwithdegrees
    diskset.objects.create(SMALL=inputsetwithdegrees['SMALL'], MEDIUM=inputsetwithdegrees['MEDIUM'],
                           LARGE=inputsetwithdegrees['LARGE'])
    return inputsetwithdegrees


def outputmemberfunction(serverindex):
    emptySet = []
    almostemptySet = []
    mediumSet = []
    almostFullSet = []
    FullSet = []
    inputsetwithdegrees = {}
    x = float(0.3 - serverindex) / float(0.3 - 0.2)
    emptySet.extend((x, 1))
    emptySetDegree = min(emptySet)
    if emptySetDegree < 0:
        emptySetDegree = 0.0
    inputsetwithdegrees['EMPTY'] = emptySetDegree

    y = float(serverindex - 0.2) / float(0.35 - 0.2)
    t = float(0.5 - serverindex) / float(0.5 - 0.35)
    almostemptySet.extend((y, t))
    almostemptysetdegree = min(almostemptySet)
    if almostemptysetdegree < 0:
        almostemptysetdegree = 0.0
    inputsetwithdegrees['ALMOSTEMPTY'] = almostemptysetdegree

    y = float(serverindex - 0.35) / float(0.5 - 0.35)
    t = float(0.65 - serverindex) / float(0.65 - 0.5)
    mediumSet.extend((y, t))
    mediumsetdegree = min(mediumSet)
    if mediumsetdegree < 0:
        mediumsetdegree = 0.0
    inputsetwithdegrees['MEDIUM'] = mediumsetdegree

    y = float(serverindex - 0.5) / float(0.65 - 0.5)
    t = float(0.8 - serverindex) / float(0.8 - 0.65)
    almostFullSet.extend((y, t))
    almostfullSetdegree = min(almostFullSet)
    if almostfullSetdegree < 0:
        almostfullSetdegree = 0
    inputsetwithdegrees['ALMOSTFULL'] = almostfullSetdegree

    y = float(serverindex - 0.65) / float(0.80 - 0.65)
    t = float(1.0 - serverindex) / float(1.0 - 0.80)
    FullSet.extend((y, t))
    fullSetdegree = min(FullSet)
    if fullSetdegree < 0:
        fullSetdegree = 0
    inputsetwithdegrees['FULL'] = fullSetdegree
    outputset.objects.create(EMPTY=inputsetwithdegrees['EMPTY'], ALMOSTEMPTY=inputsetwithdegrees['ALMOSTEMPTY'],
                             MEDIUM=inputsetwithdegrees['MEDIUM'], ALMOSTFULL=inputsetwithdegrees['ALMOSTFULL'],
                             FULL=inputsetwithdegrees['FULL'])
    return inputsetwithdegrees


def ruletable(cpu, ram, disk):
    states = {'SMALL': 2, 'MEDIUM': 1, 'LARGE': 0}
    cpusets = cpufuzzylogic(cpu)

    cpuresult = max(cpusets, key=cpusets.get)

    ramsets = ramfuzzylogic(ram)
    ramresult = max(ramsets, key=ramsets.get)

    disksets = diskfuzzylogic(disk)
    print disksets
    diskresult = max(disksets, key=disksets.get)

    serverIndex = float(states[cpuresult] + states[ramresult] + states[diskresult]) / 6.0
    output = outputmemberfunction(serverIndex)

    outputresult = max(output, key=output.get)
    # if __name__ == "__main__":
    #     ruletable(25,60,85)
