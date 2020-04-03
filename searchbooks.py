import pandas as pd

data = pd.read_csv("books.csv")
def convertBookname(bookname):
    result = ''.join([i for i in bookname if not i.isdigit()])
    result.replace(" ", "")
    result.replace(" ", "")
    result.replace(" ", "")
    result.replace(" ", "")
    result.replace(" ", "")

    # print(result)
    return result

def setSearchArray(converted_searchstring,searchstring):
    # Loop through each character in the converted_searchstring,
    # check if it is equal to the one searchstring if yes set position
    retArray =[]
    counter=0
    findcounter=0
    searchstringCounter = 0
    for x in converted_searchstring:
        found = False
        while found == False:
            Char = (converted_searchstring[counter:counter + 1]).lower()
            TargetChar = searchstring[findcounter:findcounter + 1].lower()

            if Char == TargetChar:
                retArray.append(findcounter)
                found = True
            findcounter = findcounter+1
        counter = counter + 1
    return retArray


# print(data)
searchstring = "LET'S SEE HOW OBSERVANT YOU ARE. There are names of sixteen (16) books of the bible hidden in the paragraph below. Let me see how many you can find. A preacher found 15 books in twenty minutes; it took him 3 weeks just to find the 16th one, HAVE FUN! I once made a remark about the hidden books of the Bible. A certain luke, kept people looking so hard for facts, and for others, it was a revelation. Some were in a jam, especially since the names of the books were not capitalized. But the truth finally struck home to numbers of our readers. To others it was a job. We want it to be a most fascinating little moment for you. Yes, there will be some really easy ones to spot. Others may require judges to help find them. I will  quickly admit it usually takes the preacher to find one of them, and there will be loud lamentations when it is found. A little lady says she brews a cup of tea so she can concentrate better. See how you will compete. Relax now, for there really are sixteen books of the Bible in this paragraph. LIST THE 16 BOOKS.HAPPY SEARCHING!!!"
# define punctuation
punctuations = '''!()-[]{};:'"\,<>. /?@#$%^&*_~'''
no_punct = ""
for char in searchstring:
   if char not in punctuations:
       no_punct = no_punct + char

converted_searchstring = no_punct.lower()
# display the unpunctuated string

converted_searchstring = ''.join([i for i in converted_searchstring if not i.isdigit()])
searchArray = setSearchArray(converted_searchstring,searchstring)
# print(searchArray[2])
# print(searchArray)

searchcounter= 1
oldbookname = ""

for ind in data.index:
     # print(data['BookName'][ind])
     bookname = convertBookname(data['BookName'][ind].lower())
     bookname = bookname.replace(" ","")
     # print("#" + bookname +"#")
     # print(bookname)
     strlocation = converted_searchstring.find(bookname)
     booklength = len(bookname)
     if strlocation > -1:
         if oldbookname != bookname:
            origArraypos =searchArray[strlocation]
            findstring = "..." +searchstring[origArraypos:origArraypos+20]+ "..."
            # findstring = "..." + converted_searchstring[strlocation-5:strlocation+booklength+5] + "..."
            #  findstring =""
            # print(findstring)
            print(searchcounter, data['BookName'][ind],findstring)
            searchcounter =searchcounter+1
     oldbookname = bookname





print(converted_searchstring)