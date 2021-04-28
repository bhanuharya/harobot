def buildLast(pattern):
    last = [-1 for i in range(256)]

    for i in range(len(pattern)):
        last[ord(pattern[i])] = i

    return last

def bmMatch(text, pattern):
    last = buildLast(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1

    if (i > n-1):
        return -1 # tidak match kalau pattern lebih panjang dari text

    j = m-1
    while (i<n-1):
        if pattern[j]==text[i]:
            if j==0 :
                return i
            else:
                i-=1
                j-=1
        else:
            lo = last[ord(text[i])]
            i = i+m - min(j,1+lo)
            j = m-1

    return -1 # Tidak match

# text = "bacaaaa"
# pattern1 = "aca"
# pattern2 = "acb"

# txt = "ABAAAABBABAABCDABC"
# pat = "AABC"

# tes1 = bmMatch(text, pattern1)
# tes2 = bmMatch(text, pattern2)
# tes3 = bmMatch(txt, pat)

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