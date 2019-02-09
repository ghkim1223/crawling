import re


def distribute(dramList):
    sortList = [[],[],[]]
    p1 = re.compile('기묘한[\s|\S]*이야기')
    p2 = re.compile('킹덤[\s|\S]*')
    p3 = re.compile('나르코스[\s|\S]*')
    for drama in dramList:
        if p1.findall(drama):
            sortList[0].append(drama)
        elif p2.findall(drama):
            sortList[1].append(drama)
        elif p3.findall(drama):
            sortList[2].append(drama)
    return sortList
