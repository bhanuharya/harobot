from BoyerMoore import *
from KnuthMorrisPratt import *

def helpBot():
    fitur = ("Menambah task baru", "Melihat daftar task", "Menampilkan deadline task tertentu", "Memperbaharui task", "Menandai task sudah selesai dikerjakan", "Menampilkan opsi bantuan yang difasilitasi oleh assistant")
    kataPenting = ("Kuis", "Ujian", "Tucil", "Tubes", "Tugas")
    message = "Fitur : <br>"
    for tuple in fitur:
        fiturLIst = tuple
        fiturLIst = "["+str(fitur.index(tuple)+1)+"] "+str(fiturLIst)+"\n"+"<br>"
        message = message + fiturLIst
    
    message = message + "<br> Kata Penting :" + "<br>"
    for tuple in kataPenting:
        kataList = tuple
        kataList = "["+str(kataPenting.index(tuple)+1)+"] "+str(kataList)+"\n"+"<br>"
        message = message + kataList
    return message

# print(helpBot())