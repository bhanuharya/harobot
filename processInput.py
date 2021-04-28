from BoyerMoore import *
from KnuthMorrisPratt import *
from handleUpdateTask import *
from handleMarkDoneTask import *
from handleNewTask import *
from ShowTask import showTask
from ShowDeadline import showDeadline
from helpBot import *

def removeNewLine(string):
    newString = ''
    for char in string:
        if (char != '\n'):
            newString = newString + char
    return newString

def checkIfTanggalExist(command):
    matchObject = None
    allowedDateFormat = ['\d\d-\d\d-\d\d\d\d','\d\d\/\d\d\/\d\d\d\d']
    for format in allowedDateFormat: # Pasti date yang ada sesuai sama salah satu format atau ga sama sekali
        if (re.search(format,command)):
            matchObject = re.search(format,command)
    if (matchObject): # Ada tanggal dalam command
        return True
    else:   # Tidak ada tanggal dalam command
        return False

def checkIfKodeExist(command):
    matchObject = None
    allowedKodeFormat = '[A-Z][A-Z]\d\d\d\d'
    if (re.search(allowedKodeFormat,command)):
        matchObject = re.search(allowedKodeFormat,command)
    if (matchObject): # Ada kode matkul
        return True
    else: # Tidak ada kode matkul
        return False

def checkIfTopikExist(command):
    matchObject = None
    if (re.search("\"(\w|\s)*\"|\'(\w|\s)*\'",command)):
        matchObject = re.search("\"(\w|\s)*\"|\'(\w|\s)*\'",command)
    if (matchObject):
        return True
    else:
        return False

def checkIfIDExist(command):
    matchObject = None
    allowedIDFormat = '\s[0-9]*\s'
    if (re.search(allowedIDFormat,command)):
        matchObject = re.search(allowedIDFormat,command)
    if (matchObject):
        return True
    else:
        return False

# Determine what kind of process (add, update, or mark as done)
def processInput(command):
    # Command List
    listTask = []
    listUpdateCommand = []
    listDoneCommand = []
    
    # Load keyword
    addToListTask = False
    addToListUpdateCommand = False
    addToListDoneCommand = False
    with open("KeywordList.txt",'r') as keywordFile:
        for line in keywordFile.readlines():
            # print(removeNewLine(line))
            if (bmMatch(removeNewLine(line),"Task:") != -1):
                addToListTask = True
                continue
            elif (bmMatch(removeNewLine(line),"Task Update:") != -1):
                addToListUpdateCommand = True
                addToListTask = False
                continue
            elif (bmMatch(removeNewLine(line),"Task Done:") != -1):
                addToListDoneCommand = True
                addToListUpdateCommand = False
                continue
            if (addToListTask):
                listTask.append(removeNewLine(line))
            elif (addToListUpdateCommand):
                listUpdateCommand.append(removeNewLine(line))
            elif (addToListDoneCommand):
                listDoneCommand.append(removeNewLine(line))
    
    # Process command
    for update in listUpdateCommand:
        if ((kmpMatch(command,update) != -1)  and (checkIfTanggalExist(command)) and (checkIfIDExist(command))):
            # Mengandung salah satu keyword untuk update, tanggal baru, dan ID Task
            return handleUpdateTask(command)
    
    for done in listDoneCommand:
        if ((kmpMatch(command,done) != -1) and (checkIfIDExist(command))):
            # Mengandung salah satu keyword untuk done dan ID Task
            return handleMarkDoneTask(command)
    
    for task in listTask: # Kalo mau pake command add task harus ada:
        if ((kmpMatch(command,task) != -1) and (checkIfTanggalExist(command)) and (checkIfKodeExist(command)) and (checkIfTopikExist(command))):
            # Mengandung salah satu keyword task (PR,Kuis,Praktikun,UTS,UAS,Tucil,Tubes), tanggal, kode matkul, dan topik task dalam command
            return handleNewTask(command,task)

    if(kmpMatch(command.lower(), "apa saja") != -1 and kmpMatch(command.lower(), "deadline")!=-1):
        return showTask(command)
    
    if(kmpMatch(command.lower(), "kapan") != -1 and kmpMatch(command.lower(), "deadline")!=-1):
        return showDeadline(command)

    if(kmpMatch(command.lower(), "bisa") != -1 and kmpMatch(command.lower(), "lakukan")!=-1):
        return helpBot()
    
    if(kmpMatch(command.lower(), "hi") != -1 or kmpMatch(command.lower(), "halo")!=-1):
        return "Hi!, Aku Harobot ^_^"
    
    if(kmpMatch(command.lower(), "exit") != -1 or kmpMatch(command.lower(), "keluar")!=-1):
        return exit()

    return "Command tidak dikenali!"    # Masuk kesini kalo di for loop task ga diketahuin task apa yg mau ditambahin
                                        # Artinya bisa langsung dikasih tau kalo commmand ga dikenalin

# com = str("Tubes IF2211 \"String Matching\" pada 14/07/2021")
# print(str(processInput(com)))

def exit():
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
    searchQuery = "DELETE FROM taskList;"
    mycursor.execute(searchQuery)
    mydb.commit()

    return "Terima kasih sudah menggunakan Harobot :)"