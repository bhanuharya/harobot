from BoyerMoore import *
from KnuthMorrisPratt import *
import re
from handleNewTask import *

def getID(command):
    matchObject = None
    allowedIDFormat = '\s[0-9]*\s'
    if (re.search(allowedIDFormat,command)):
        matchObject = re.search(allowedIDFormat,command)
    if (matchObject):
        IDFomat = matchObject.group()
        newIDFormat = getStringFromResult(IDFomat)
        return newIDFormat
    else: # Input tidak sesuai format
        return None

def handleUpdateTask(command):
    # Define error message
    isIDError = False
    isTanggalError = False
    errorMessageID = 'Terdapat kesalahan penulisan format ID!\n'
    errorMessageTanggal = 'Terdapat kesalahan penulisan format tanggal atau tanggal yang dimasukkan tidak valid!\n'
    errorMessage = ''

    # Check ID error
    ID = getID(command)
    if (ID == None):
        isIDError = True
    
    # Check Tanggal error
    tanggal_baru = getDateWithRegex(command)
    if (tanggal_baru == None):
        isTanggalError = True
    else:
        tanggal_baru = reverseDate(getDateWithRegex(command))
    
    # Generate Output
    if (isIDError or isTanggalError):
        if (isIDError):
            errorMessage = errorMessage + errorMessageID
        if (isTanggalError):
            errorMessage = errorMessage + errorMessageTanggal
        return errorMessage
    else: # Cari ID di database
        # Establish connection to DB
        mydb = mysql.connector.connect(
            # host="localhost",
            # user="root",
            # password="placeholder",
            # database="task"
            host="localhost",
            user="hariya",
            password="31213121",
            database="task"
        )
        mycursor = mydb.cursor()

        # Generate select statement
        searchQuery = 'SELECT id_task FROM taskList WHERE id_task='+ID+";"
        mycursor.execute(searchQuery)
        result = mycursor.fetchall()
        if (len(result) == 0): # List kosong, artinya tidak ada hasil yang diinginkan
            return "ID Task yang dimasukkan tidak terdapat dalam database!\n"
        else: # List tidak kosong, ada hasilnya
            # Generate update statement
            updateQuery = "UPDATE taskList SET tanggal_deadline=\'"+tanggal_baru+"\' WHERE id_task="+ID+";"
            mycursor.execute(updateQuery)
            mydb.commit()

            # Selecting previously updated task and generate success message
            # selectQuery = 'SELECT tanggal_deadline FROM tasklist WHERE id_task='+ID+';'
            # mycursor.execute(selectQuery)
            # result = mycursor.fetchall()
            newTanggal = reverseDate(tanggal_baru)
            successMessage = "Task berhasil di-update!\n"
            updatedTask = "Deadline task dengan ID = "+ID+" berhasil di-update menjadi tanggal "+newTanggal+"!\n"
            return successMessage + updatedTask