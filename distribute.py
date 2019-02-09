import re


def distribute(dramList):
    sortList = {}
    pList = []
    sortList['기묘한 이야기'] = []
    pList.append(re.compile('기묘한[\s|\S]*이야기'))
    sortList['킹덤'] = []
    pList.append(re.compile('킹덤'))
    sortList['나르코스'] = []
    pList.append(re.compile('나르코스'))
    for drama in dramList:
        if pList[0].findall(drama):
            sortList['기묘한 이야기'].append(drama)
        if pList[1].findall(drama):
            sortList['킹덤'].append(drama)
        if pList[2].findall(drama):
            sortList['나르코스'].append(drama)
    return sortList
