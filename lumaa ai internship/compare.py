#compare is the meat and potatoes of this program, it takes a string as an input, and returns a string
#
def main (query):

    wordsPath = "C:\\Users\\mccal\\Desktop\\lumaa ai internship\\words.txt"
    filename = "C:\\Users\\mccal\\Desktop\\lumaa ai internship\\movie_dataset.csv"

    
    

    #imports the idf method from idf
    import IDF as idf 
    #import CSV
    import csv
    #import math
    import math
    import trimmer as tm
    f = open(wordsPath, "r")
    wordList = (f.read())
    wordArr = wordList.splitlines()
    query = query.lower()
    query = tm.trimmer(query, wordArr)








    
    # csv file name

    #arrays to store the onfo taken from the CSV
    #there are 2 copys of some of the output integrity at the end
    title = []
    genere = []
    description = []
    keyWords = []
    titleT = []
    genereT = []
    descriptionT = []

    # reading csv file
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        try:
            for row in csv_reader:
            
                if line_count == 0:

                    line_count += 1
                else:
                    if (line_count > 2800):
                        break
                    #store the info of each in its true form
                    titleT.append(row[7])
                    genereT.append(row[2])
                    descriptionT.append(row[8])
                    #trim down the info taken from each to reduce the cost of future word processing
                    title.append((row[7]).lower())
                    genere.append((row[2]).lower())
                    description.append((row[8]).lower())
                    keyWords.append((row[5]).lower())
                    line_count += 1
        except:
            print ("error1")
            
  
    #the indexs and score array are used for the scoring and sorting process
    #as the scores are sorted, the index array is also sorted
    # the index array is 0-length of the movie list where the numbers are coorelated to the original index of the items
    # the score is an integer value of the movies score of similarity of the movie
    indexs = []
    scoreArr = []
    score= 0
    #this inputs all the title's genere's and keywords and returns a dictionary with KVP's of all the words present, number of times it occered
    idfDict = idf.idf(title,genere,keyWords,description)
    # here is the scoring process
    # for every movie's title, keywords, and genere are compared to the search term
    #for every movie
    for n in range(len(genere)):
        score = 0
        #check every search term in how it relates to
        for i in query.split(' '):
            
            
            splitArrGen = genere[n].split(" ")
            splitArrKey = keyWords[n].split(' ')
            splitArrTit = title[n].split(' ') 
            splitArrDes = description[n].split(' ')
            #every word in the genere
            for k in splitArrGen:
                #if a match is found
                if i == k and i != "":

                    try:
                        #multiply the base score by its TF-IDFvalue
                        score = score+1*math.log(len(genere),idfDict.get(i))*(1/len(splitArrGen))
                    except:
                        print(" floaterror")
            #every word in the key words
            for k in splitArrKey:

                #if a match is found
                if i == k and i != "":
                   
                    try:
                        #multiply the base score by its TF-IDFvalue
                        score = score+1*math.log(len(genere),idfDict.get(i))*(1/len(splitArrKey))
                    except:
                        print(" floaterror")
            #for every word in the title
            for k in splitArrTit:

                #if a match is found
                if i == k and i != "":

                    try:
                        #multiply the base score by its TF-IDFvalue
                        score = score+1*math.log(len(genere),idfDict.get(i))*(1/(len(splitArrTit)))
                    except:
                        print(" floaterror")
            for k in splitArrDes:

                #if a match is found
                if i == k and i != "":

                    try:
                        #multiply the base score by its TF-IDFvalue
                        score = score+1*math.log(len(genere),idfDict.get(i))*(1/(len(splitArrDes)))
                    except:
                        print(" floaterror")


        #if the score is not zero then add the movies score to scoreArr and log its index in indexs(which is an array)
        #it also sorts the indexs array accordingly
        if score != 0:
            scoreArr.append(score)
            indexs.append(n)
    #this is a sorting algorithm which sorts the highest values to the earliest indexes
    for n in range(len(scoreArr)):
        swap = False
        for i in range (len(scoreArr)-1):
            if scoreArr[i] < scoreArr[i+1]:
                swap = True
                temp = scoreArr[i+1]
                scoreArr[i+1] = scoreArr[i]
                scoreArr[i] = temp
                temp = indexs[i]
                indexs[i] = indexs[i+1]
                indexs[i+1] = temp
        #if no swaps are made it exits early
        if swap == False:
            break

    print (titleT[indexs[0]])
    print (titleT[indexs[1]])
    print (titleT[indexs[2]])
    print (titleT[indexs[3]])
    print (titleT[indexs[4]])
    #returns a legeble string value

    returnString =titleT[indexs[0]] +":  " + descriptionT[indexs[0]] +"\n\n"+ titleT[indexs[1]] +":  " + descriptionT[indexs[1]] +"\n\n"+titleT[indexs[2]] +":  " + descriptionT[indexs[2]] +"\n\n"+titleT[indexs[3]] +":  " + descriptionT[indexs[3]] +"\n\n"+titleT[indexs[4]] +":  " + descriptionT[indexs[4]]
    return returnString

        












