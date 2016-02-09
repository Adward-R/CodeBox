__author__ = 'Adward'
from time import time
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def recFind(dict, iti, tN, depart):

            if depart not in dict:
                if tN:
                    return False
                else:
                    return True
            else:
                i = 0
                while i < len(dict[depart]) and not dict[depart][i]:
                    i += 1
                if i == len(dict[depart]):
                    if tN:
                        return False
                    else:
                        return True

                while i < len(dict[depart]):
                    dest = dict[depart][i]
                    iti.append(dest)
                    dict[depart][i] = None
                    if recFind(dict, iti, tN-1, dest):
                        return True
                    else:
                        dict[depart][i] = dest
                        i += 1
                        iti.pop()
                return False

        dict = {}
        iti = ['JFK']
        for depart, dest in tickets:
            if depart in dict:
                dict[depart].append(dest)
            else:
                dict[depart] = [dest]

        for depart in dict:
            dict[depart].sort()

        tN = len(tickets)
        recFind(dict, iti, tN, 'JFK')
        return iti


sol = Solution()
#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
t = time()
ss = ''
#for i in range(100):
ss = sol.findItinerary(tickets)
print(time()-t)
print(ss)