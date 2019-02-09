import re


def distribute(dramList):
    sortList = {}
    sortList['기묘한 이야기'] = []
    p1 = re.compile('기묘한[\s|\S]*이야기')
    sortList['킹덤'] = []
    p2 = re.compile('킹덤[\s|\S]*')
    sortList['나르코스'] = []
    p3 = re.compile('나르코스[\s|\S]*')
    for drama in dramList:
        if p1.findall(drama):
            sortList['기묘한 이야기'].append(drama)
        if p2.findall(drama):
            sortList['킹덤'].append(drama)
        if p3.findall(drama):
            sortList['나르코스'].append(drama)
    return sortList
