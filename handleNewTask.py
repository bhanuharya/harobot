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

def reverseDate(date): # bertipe string
    listTampungan = []
    newDate = ''
    if (date[2] == '-'):
        listTampungan = date.split('-')
        newDate = listTampungan[2] + "-" + listTampungan[1] + "-" + listTampungan[0]
    elif (date[2] == '/'):
        listTampungan = date.split('/')
        newDate = listTampungan[2] + "/" + listTampungan[1] + "/" + listTampungan[0]
    return newDate

def getKodeMatkul(command):
    matchObject = None
    allowedKodeFormat = '[A-Z][A-Z]\d\d\d\d'
    if (re.search(allowedKodeFormat,command)):
        matchObject = re.search(allowedKodeFormat,command)
    if (matchObject):
        kodeFormat - matchObject.group()
        return kodeFormat
    else:
        return None

def handleNewTask(command, jenisTask):
    