import re
import database


def getList(dramaInfoList):
    sortList = {}
    pList = {}
    for dramaInfo in dramaInfoList:
        sortList[dramaInfo['name']] = []
        pList[dramaInfo['name']] = re.compile(dramaInfo['synonym'])
    return sortList, pList


def distribute(dramList):
    dramaInfoList = database.getDramaInfo()
    sortList, pList = getList(dramaInfoList)
    for drama in dramList:
        for dramaName in sortList.keys():
            if pList[dramaName].search(drama):
                sortList[dramaName].append(drama)
    return sortList
