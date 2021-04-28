from BoyerMoore import bmMatch
from KnuthMorrisPratt import kmpMatch
from datetime import date, timedelta
from handleNewTask import reverseDate
import re
import mysql.connector
# Lihat daftar seluruh task
# Lihat daftar task berdasarkan periode waktu
# Lihat daftar task berdasarkan jenis task

# Command : "deadline" + <Jenis tugas> + waktu (interval, n minggu, n hari, hari ini, sejauh ini) + "apa saja"
# Trigger : if (kmpMatch(command.lower(),"deadline")!=-1 and kmpMatch(command, "apa saja")!=-1)

def showTask(command):
    # Connect database
    mydb = mysql.connector.connect(
        # host="localhost",
        # user="root",
        # password="",
        # database="task"
        host="localhost",
        user="hariya",
        password="31213121",
        database="task"
    )
    mycursor = mydb.cursor()

    #getJenisTugas
    jenis_tugas = getJenisTugas(command)
    selectQuery = ''
    if(kmpMatch(command, "ke depan")!=-1):
        if(kmpMatch(command, "minggu")!=-1):
            #getangka
            angka = getAngka(command)
            #gethariini
            today = getHariIni()
            updatedDay = getNHarikeDepan(angka*7)
            #select
            if(jenis_tugas==None):
                selectQuery = "SELECT * FROM taskList WHERE tanggal_deadline<=\'"+updatedDay+"\' and tanggal_deadline>=\'"+today+"\';"
            else:
                selectQuery = "SELECT * FROM taskList WHERE jenis_task = \'"+jenis_tugas+"\' and tanggal_deadline<=\'"+updatedDay+"\' and tanggal_deadline>=\'"+today+"\';"

        if(kmpMatch(command, "hari")!=-1):
            #getangka
            angka = getAngka(command)
            #gethariini
            today = getHariIni()
            updatedDay = getNHarikeDepan(angka)
            #select task from task where date >= today and date <= lastday
            if(jenis_tugas==None):
                selectQuery = "SELECT * FROM taskList WHERE tanggal_deadline<=\'"+updatedDay+"\' and tanggal_deadline>=\'"+today+"\';"
            else:
                selectQuery = "SELECT * FROM taskList WHERE jenis_task = \'"+jenis_tugas+"\' and tanggal_deadline<=\'"+updatedDay+"\' and tanggal_deadline>=\'"+today+"\';"

    else:
        if(kmpMatch(command, "antara")!=-1):
            #get date1, date2
            date1, date2 = getDates(command)
            #select task from task where date >=date1 and date <=date2
            if(jenis_tugas==None):
                selectQuery = "SELECT * FROM taskList WHERE tanggal_deadline<=\'"+date2+"\' and tanggal_deadline>=\'"+date1+"\';"
            else:
                selectQuery = "SELECT * FROM taskList WHERE jenis_task = \'"+jenis_tugas+"\' and tanggal_deadline<=\'"+date2+"\' and tanggal_deadline>=\'"+date1+"\';"

        else:
            if(kmpMatch(command, "hari ini")!=-1):
                #gethariini
                today = getHariIni()
                #select task from task where date = today
                if(jenis_tugas==None):
                    selectQuery = "SELECT * FROM taskList WHERE tanggal_deadline=\'"+today+"\';"
                else:
                    selectQuery = "SELECT * FROM taskList WHERE jenis_task = \'"+jenis_tugas+"\' and tanggal_deadline=\'"+today+"\';"
            else:
                if(kmpMatch(command, "sejauh ini" )!=-1):
                    #select all
                    if jenis_tugas == None:
                        # selectQuery = "SELECT * FROM taskList WHERE tanggal_deadline >= "+getHariIni()+";"
                        selectQuery = "SELECT * FROM taskList WHERE isDone = \'Belum\' and tanggal_deadline >= \'"+getHariIni()+"\';"
                    else:
                        selectQuery = "SELECT * FROM taskList WHERE isDone = \'Belum\' and jenis_task =\'"+jenis_tugas+"\' and tanggal_deadline >= \'"+getHariIni()+"\';"
                
    print(selectQuery)
    mycursor.execute(selectQuery)
    result = mycursor.fetchall()
    
    if len(result)==0:
        return "Tidak ada deadline :D"
    else:
        message = "[Daftar Deadline]<br>"
        n = 1
        for tup in result:
            idTask = tup[0]
            deadline = toDate(str(tup[1]))
            matkul = tup[2]
            jenis = tup[3]
            topik = tup[4]
            task = str(n) + ". (ID: "+ str(idTask) + ") "+str(deadline)+" - "+ matkul + " - " + jenis + " - " + topik + "<br>"
            message = message + task
            n+=1
        return message

def getAngka(command):
    x = re.search("\d+ minggu|\d+ hari", command)
    a = x.group()
    y = re.search("\d+", a)
    angka = y.group()
    return int(angka)  

def getDates(command):
    x = re.findall("\d\d\/\d\d\/\d\d\d\d", command)
    date1 = reverseDate(x[0])
    date2 = reverseDate(x[1])
    return date1,date2

def getHariIni():
    fdate = date.today().strftime('%Y-%m-%d')
    return fdate

def getNHarikeDepan(N):
    fdate = date.today() + timedelta(days=N)
    fdate = fdate.strftime('%Y-%m-%d')
    return fdate

def getJenisTugas(command):
    jenisTugas = ["PR", "Praktikum", "Tubes", "Tucil", "Kuis", "UTS", "UAS"]
    for jenis in jenisTugas:
        if(kmpMatch(command.lower(), jenis.lower())!=-1):
            return jenis
    return None

def toDate(tanggal):
    list = tanggal.split("-")
    newDate = list[2]+"/"+list[1]+"/"+list[0]
    return newDate