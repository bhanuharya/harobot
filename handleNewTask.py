from KnuthMorrisPratt import *
from BoyerMoore import *
import re
import mysql.connector

def isDateValid(date): # bertipe string
    listTampungan = []
    if (date[2] == '-'):
        listTampungan = date.split('-')
    elif (date[2] == '/'):
        listTampungan = date.split('/')
    day = int(listTampungan[0])
    month = int(listTampungan[1])
    year = int(listTampungan[2])
    if (day >= 1 and day <= 28):
        return True
    elif (day == 29 or day == 30):
        if ((month >= 3 and month <= 12) or month == 1):
            return True
        else: # If month == 2 -> Februari
            if (day == 29): # Tanggal 29 Februari
                if (year % 4 == 0): # Tahun kabisat
                    return True
                else:
                    return False
            else: # Tanggal 30 Februari
                return False
    elif (day == 31):
        if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11):
            return False
        else:
            return True
    else:
        return False


def getDateWithRegex(command):
    matchObject = None
    # Format tanggal valid -> DD-MM-YYYY atau DD/MM/YYYY
    allowedDateFormat = ['\d\d-\d\d-\d\d\d\d','\d\d\/\d\d\/\d\d\d\d'] 
    for format in allowedDateFormat: # Pasti date yang ada sesuai sama salah satu format atau ga sama sekali
        if (re.search(format,command)):
            matchObject = re.search(format,command)
    if (matchObject):
        dateFormat = matchObject.group()
        if (isDateValid(dateFormat)):
            return dateFormat # bertipe string
        else: # Tanggal yang dimasukkan ga valid
            return None
    else: # Ada kesalahan penulisan tanggal (ga sesuai format)
        return None

def reverseDate(date): # bertipe string. Masukan berupa input string dari pengguna dan digunakan untuk SQL
    listTampungan = []
    newDate = ''
    if (date[2] == '-'):
        listTampungan = date.split('-')
    elif (date[2] == '/'):
        listTampungan = date.split('/')
    newDate = listTampungan[2] + "-" + listTampungan[1] + "-" + listTampungan[0]
    return newDate

def getKodeMatkul(command):
    matchObject = None
    allowedKodeFormat = '[A-Z][A-Z]\d\d\d\d'
    if (re.search(allowedKodeFormat,command)):
        matchObject = re.search(allowedKodeFormat,command)
    if (matchObject):
        kodeFormat = matchObject.group()
        return kodeFormat
    else: # Ada kesalahan penulisan format kode matkul
        return None

def getTaskTopic(command): # Topik task dikutip sama petik dua atau petik satu
    matchObject = None
    # allowedTopikFormat = ["\"(\w|\s)*\"","\'(\w|\s)*\'"]
    # for format in allowedTopikFormat:
    if (re.search("\"(\w|\s)*\"|\'(\w|\s)*\'",command)):
        matchObject = re.search("\"(\w|\s)*\"|\'(\w|\s)*\'",command)
    if (matchObject):
        topikFormat = matchObject.group()
        if (len(topikFormat) <= 255):
            return topikFormat
        else: # Panjang string melebihi 255 karakter
            return None
    else: # Ada kesalahan penulisan format topik task
        return None

def getStringFromResult(result):
    temp = str(result)
    newString = ""
    for i in temp:
        if (ord(i) >= 48 and ord(i) <= 57):
            newString = newString + i
    return newString

def handleNewTask(command, jenisTask):
    # Define error message
    isTanggalError = False
    isKodeError = False
    isTopikError = False
    errorMessageTanggal = 'Terdapat kesalahan penulisan format tanggal atau tanggal yang dimasukkan tidak valid!\n'
    errorMessageKode = 'Terdapat kesalahan penulisan format kode mata kuliah!\n'
    errorMessageTopik = 'Terdapat kesalahan penulisan format topik task atau panjang karakter topik melebih 255 karakter!\n'
    errorMessage = ''

    # Check Tanggal error
    tanggal_deadline = getDateWithRegex(command)
    if (tanggal_deadline == None):
        isTanggalError = True
    else:
        tanggal_deadline = reverseDate(getDateWithRegex(command)) # Disiapin buat dimasukin ke database
    
    # Check Kode error
    kode_matkul = getKodeMatkul(command)
    if (kode_matkul == None):
        isKodeError = True
    
    # Check Topik Error
    topik_task = getTaskTopic(command)
    if (topik_task == None):
        isTopikError = True
    
    # Generate output
    if (isTanggalError or isKodeError or isTopikError): # Return error message
        if (isTanggalError):
            errorMessage = errorMessage + errorMessageTanggal
        if (isKodeError):
            errorMessage = errorMessage + errorMessageKode
        if (isTopikError):
            errorMessage = errorMessage + errorMessageTopik
        return errorMessage
    else: # Put into database and return success message
        # Establish connection to DB
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

        # Generate insert statement
        insertQuery = "INSERT INTO taskList (tanggal_deadline,kode_matkul,jenis_task,topik_task,isDone) VALUES (\'"+tanggal_deadline+"\',\'"+kode_matkul+"\',\'"+jenisTask+"\',\'"+topik_task+"\',\'Belum\');"
        mycursor.execute(insertQuery)
        mydb.commit()
        
        # Selecting and returning the previously added task
        selectQuery = "SELECT id_task FROM taskList WHERE tanggal_deadline=\'"+tanggal_deadline+"\' and kode_matkul=\'"+kode_matkul+"\' and jenis_task=\'"+jenisTask+"\' and topik_task=\'"+topik_task+"\';"
        mycursor.execute(selectQuery)
        result = mycursor.fetchall()
        newID = getStringFromResult(result[0])
        successMessage = "Task berhasil ditambahkan!\n"
        newTask = "(ID: "+newID+") "+tanggal_deadline+" - "+kode_matkul+" - "+jenisTask+" - "+topik_task+"\n"
        return successMessage + newTask 
