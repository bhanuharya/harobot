from BoyerMoore import *
from KnuthMorrisPratt import *

def helpBot():
    fitur = ("Menambah task baru", "Melihat daftar task")
    kataPenting = ("Kuis", "Ujian", "Tucil", "Tubes", "Tugas")
    message = ""
    for tuple in fitur:
        fiturLIst = tuple
        fiturLIst = "["+str(fitur.index(tuple)+1)+"] "+str(fiturLIst)+"\n"
        message = message + fiturLIst
    
    message = message + "\n"
    for tuple in kataPenting:
        kataList = tuple
        kataList = "["+str(kataPenting.index(tuple)+1)+"] "+str(kataList)+"\n"
        message = message + kataList
    return message

print(helpBot())