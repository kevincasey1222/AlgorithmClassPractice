import random

class RLG:

    def __init__(self, listlen, listscope):

            self.thelist = list()
            for i in range(0, listlen):
                self.thelist.append(random.randint(1, listscope))

    def printout(self):

        for i in range(0, len(self.thelist)):
            print(self.thelist[i])

    def insertionsort(self):

        swaps = 0
        for i in range(1, len(self.thelist)):
            j = i
            while j > 0 and self.thelist[j-1] > self.thelist[j]:
                holder = self.thelist[j]
                self.thelist[j] = self.thelist[j-1]
                self.thelist[j-1] = holder
                swaps = swaps + 1
                j = j-1
        return swaps


    def quicksort(self):
        pass

