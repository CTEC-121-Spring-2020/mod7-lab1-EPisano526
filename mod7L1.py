"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    myStri = "Hello World"

    print()
    '''
    print(myStri)
    print(myStri[6])
    print(myStri[len(myStri)-1])
    print(myStri[10])
    print(myStri[11])
    print(myStri[0])
    print(myStri[-1])   
    print(myStri[-5])
    print(myStri[-len(myStri)])

    word1 = "Hello"
    word2 = "World"
    myStri2 = word1 + " " + word2
    print(myStri2)
    myStri3 = word1 + word2
    print(myStri3)

    print(myStri2[6:len(myStri2)])

    print()

# section 2
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("Enter a month number (1 - 12): "))
    pos = (n-1) * 3
    print(pos)
    # slice to get abbreviation
    monthAbr = months[pos:pos+3]
    print(monthAbr)

    print()

    # list
    # create a empty list
    myList = []
    print("myList:", myList)

    myList2 = [1, 2, 3, 4]
    print("myList2:", myList2)

    myList3 = [42, "forty-two", 3.14]
    print("myList3: ", myList3)

    print("thrid element of myList2:", myList2[2])

    # initializing example
    for i in range(1, 6):
        myList.append(i)
    print("myList1:", myList)

    # illustrate insert()
    myList.insert(2, 3.14)
    print("myList1:", myList)

    # sort()
    myList.sort()
    print("myList:", myList)
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month number(1-12): "))
    print(months[n-1])

    print("A:", ord('A'))
    print("97", chr(97))
    print()
    
    myStri = "text \n"
    print("*", myStri, "*", sep="")
    print()
    myStri = myStri.rstrip()
    print("*", myStri, "*", sep="")

    myStri = "CamelCase"
    print(myStri)
    s1 = myStri.upper()
    print(s1)
    s2 = myStri.lower()
    print(s2)
'''
    total = 0
    for i in range(10):
        total = total + 1

    print()


main()
