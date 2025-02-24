#this is a method which takes three arrays of strings as an inputs 
# #returns a dictionary of all the words in the strings, and how many times they were in the strings (KVP)
def idf(arr1, arr2, arr3, arr4):
    #makes the dictionary
    idfDict = {'xyz' : 1.0}
    for i in arr1:
        #splits all the words in a string into an array of words
        arrSplit = i.split(' ')
        
        #itterate through that array
        for j in arrSplit:
            #if that word does not exist in the dictionary
            if idfDict.get(j) == None:
                #add it String : 1
                idfDict[j] = 1.0
            else:
                #otherwise increase that words number by one
                idfDict[j] = idfDict.get(j)+1
    #IDENTICAL TO PREVIOUS BUT WITH THE SECOND ARRAY
    for i in arr2:
        arrSplit = i.split(' ')
        for j in arrSplit:
            if idfDict.get(j) == None:
                idfDict[j] = 1.0
            else:
                idfDict[j] = idfDict.get(j)+1
    #IDENTICAL TO PREVIOUS BUT WITH THE THIRD ARRAY
    for i in arr3:    
        arrSplit = i.split(' ')
        for j in arrSplit:
            if idfDict.get(j) == None:  
                idfDict[j] = 1.0
            else:
                idfDict[j] = idfDict.get(j)+1
    #IDENTICAL TO PREVIOUS BUT WITH THE THIRD ARRAY
    for i in arr4:    
        arrSplit = i.split(' ')
        for j in arrSplit:
            if idfDict.get(j) == None:  
                idfDict[j] = 1.0
            else:
                idfDict[j] = idfDict.get(j)+1

    #return the dictionary
    return(idfDict)



    
