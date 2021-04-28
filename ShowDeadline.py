from BoyerMoore import bmMatch
from KnuthMorrisPratt import kmpMatch
from handleNewTask import getKodeMatkul, getTaskTopic
from ShowTask import getJenisTugas, toDate
import re
import mysql.connector

# Menampilkan deadline suatu tugas
# Format Command: "Deadline" + <jenis_tugas> + <Kode kuliah> + "kapan" ?
# Trigger fungsi : kalo ada string "deadline" dan "kapan" (if kmpMatch(txtInput, "Deadline") != -1 and kmpMatch(txtInput, "kapan") != -1)

def showDeadline(command):
    # Connect database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="task"
        # host="localhost",
        # user="hariya",
        # password="31213121",
        # database="task"
    )
    mycursor = mydb.cursor()

    # getKodeKuliah
    kode_matkul = getKodeMatkul(command)
    
    # getJenisTugas
    jenis_tugas = getJenisTugas(command)

    # getTopik
    topik = getTaskTopic(command)

    # Search tanggal based on kodekuliah, jenistugas, topik
    #select
    selectQuery = ""
    if(jenis_tugas==None):
        selectQuery = "SELECT tanggal_deadline FROM taskList WHERE isDone = \'Belum\' and kode_matkul=\'"+kode_matkul+"\';"
    else:
        if(topik == None):
            selectQuery = "SELECT tanggal_deadline FROM taskList WHERE isDone = \'Belum\' and jenis_task = \'"+jenis_tugas+"\' and kode_matkul=\'"+kode_matkul+"\';"
        else:
            selectQuery = "SELECT tanggal_deadline FROM taskList WHERE jenis_task = \'"+jenis_tugas+"\' and kode_matkul=\'"+kode_matkul+"\' and topik_task=\'"+topik+"\';"
    print(selectQuery)
    mycursor.execute(selectQuery)
    result = mycursor.fetchall()

    if len(result)==0:
        return "Tidak ada deadline :D"
    else:
        message = ""
        for tuple in result:
            tanggal = toDate(str(tuple[0]))
            tanggal = str(tanggal)+"\n"
            message = message + tanggal
        return message
