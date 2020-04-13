import RLG
import datetime

listlen = 500
listscope = 5000
myRLG = RLG.RLG(listlen, listscope)
#myRLG.printout()
sdt = datetime.datetime.now()
swaps = myRLG.insertionsort()
edt = datetime.datetime.now()
print("Insertion swap finished in", swaps, "swaps and took", (edt-sdt).microseconds / 1000, "milliseconds")
#myRLG.printout()

