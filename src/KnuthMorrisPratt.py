def computeFail(pattern):
    fail = [0 for i in range (len(pattern))]

    fail[0] = 0

    m = len(pattern)
    j = 0
    i = 1

    while i<m :
        if pattern[j] == pattern[i] :
            fail[i] = j+1
            i+=1
            j+=1
        
        elif j>0 :
            j = fail[j-1]
        else:
            fail[i] = 0
            i+=1
    return fail

def kmpMatch(text, pattern):
    n = len(text)
    m = len(pattern)

    fail = computeFail(pattern)

    i = 0
    j = 0

    while i<n :
        if pattern[j] == text[i]:
            if j == m-1 :
                return i-m+1
            i+=1
            j+=1
        elif j>0 :
            j = fail[j-1]
        else:
            i+=1   
    
    return -1 # tidak ada kesamaan
        
# text = "bacaaaa"
# pattern1 = "aca"
# pattern2 = "acb"

# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"

# tes1 = kmpMatch(text, pattern1)
# tes2 = kmpMatch(text, pattern2)
# tes3 = kmpMatch(txt, pat)

# if tes1 == -1 :
#     print("Tidak ada pola")
# else:
#     print("Pola ditemukan di indeks " + str(tes1))

# if tes2 == -1 :
#     print("Tidak ada pola")
# else:
#     print("Pola ditemukan di " + str(tes2))

# if tes3 == -1 :
#     print("Tidak ada pola")
# else:
#     print("Pola ditemukan di indeks " + str(tes3))