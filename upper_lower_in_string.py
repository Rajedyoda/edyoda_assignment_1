def string_given(str1):
    data={"UPPER_CASE":0, "LOWER_CASE":0}
    for char in str1:
        if char.isupper():
           data["UPPER_CASE"]+=1
        elif char.islower():
           data["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", str1)
    print ("No. of Upper case characters : ", data["UPPER_CASE"])
    print ("No. of Lower case Characters : ", data["LOWER_CASE"])

string_given('The quick Brow Fox')