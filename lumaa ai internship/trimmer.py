#This is a tool used to cut down in the time spent processing words. it extracts common words which are not helpfull to our search
#it inputs a string query and an array of common words
#it returns a string without those common words

#NOT IN USE ANYMORE but it works :>
def trimmer (inputArr, wordArr):
    inputArr = inputArr.split(' ')
    
    #print(inputArr)
    #print(wordArr)
    result = ''
    for i in inputArr:
        found = False
        for j in wordArr:
            
            if i == j:
                #print(i)
                #print(j)
                #print(i)
                
                found = True
        if found == False:
            result = result + " "+ i
    #print (result)
    return result