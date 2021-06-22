def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False
def getDaysInMonth(month,year):
    thirtymonths=[4,6,9,11]
    thirtyonemonths = [1,3,5,7,8,10,12]
    if month in thirtymonths:
        return 30
    if month in thirtyonemonths:
        return 31
    if isLeapYear(year):
        return 29
    return 28

def isValidDate(day,month,year):
    if year<1:
        return False
    if month<1 or month>12:
        return False
    if day<1 or day>getDaysInMonth(month,year):
        return False
    return True
def dateCompare(d1,m1,y1,d2,m2,y2):
    # -1 if D1<D2 0 if D1=D2 1 if d1>D2
    if y1<y2:
        return -1
    if y1>y2:
        return 1
    if m1<m2:
        return -1
    if m1>m2:
        return 1
    if d1<d2:
        return -1
    if d1>d2:
        return 1
    return 0

def dateDifference(d1,m1,y1,d2,m2,y2):
    # Date D1 > Date D2
    #22-6-2021   to 15-8-1947
    cmp=dateCompare(d1,m1,y1,d2,m2,y2)
    if cmp==0:
        return 0
    sign=1
    if cmp<0:
        sign=-1
        d1,d2=d2,d1
        m1,m2=m2,m1
        y1,y2=y2,y1
    diff1 = d1-1
    diff2 = d2-1
    # 1-6-2021   to 1-8-1947
    diff3=0
    for m in range(1,m1):
        diff3 +=  getDaysInMonth(m,y1)
    diff4=0
    for m in range(1,m2):
        diff4 += getDaysInMonth(m,y2)
    # 1-1-2021   to 1-1-1947
    diff5 = 0
    for y in range(y2,y1):
        if isLeapYear(y):
            diff5 += 366
        else:
            diff5 += 365
    totaldiff = diff1 + diff3 + diff5 - diff2 -diff4
    return sign*totaldiff


print(dateDifference( 21,6,2019,21,6,2020))