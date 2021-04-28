from BoyerMoore import *
from KnuthMorrisPratt import *
from handleUpdateTask import *

def getStringFromResult2(result): # version: input = string 
    temp = str(result)
    newString = ""
    for i in temp:
        if ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            newString = newString + i
    return newString

def handleMarkDoneTask(command):
    # Setup error message
    isIDError = False
    errorMessageID = 'Terdapat kesalahan penulisan format ID!\n'
    errorMessage = ''

    # Check ID Error
    ID = getID(command)
    if (ID == None):
        isIDError = True

    # Generate output
    if (isIDError):
        errorMessage = errorMessage + errorMessageID
        return errorMessage
    else:
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

        # Check if task already marked done
        # Creating select statement
        selectQuery = "SELECT isDone FROM taskList WHERE id_task="+ID+";"
        mycursor.execute(selectQuery)
        result = mycursor.fetchall()
        newResult = getStringFromResult2(result[0])
        if (newResult == 'Sudah'):
            return "Task sudah selesai dikerjakan!\n"
        else:
            # Creating update statement
            updateQuery = "UPDATE taskList SET isDone=\'Sudah\' WHERE id_task="+ID+";"
            mycursor.execute(updateQuery)
            mydb.commit()

            successMessage = "Task sudah ditandai selesai dikerjakan!\n"
            doneTask = "Task dengan ID = "+ID+" sudah selesai dikerjakan!\n"
            return successMessage + doneTask