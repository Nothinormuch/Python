import library

textWidthScalebility=50
functionDict={'Library':{'Add a book to the Library':(library.addBook,library.addBookInput),'Delete a book from the Library':(library.deleteBook,library.deleteBookInput),'Show the collection of the Library':(library.pushAll,library.pushAllInput),'Search for a book in the Library':(library.searchBook,library.searchBookInput)}}

def getCategoryTitlesMenu(functionDict,category="Main"):
    if category!="Main":
        functionDict=functionDict[category]
    vertex=f"+{"~"*textWidthScalebility}+"
    finalReturn=vertex+"\n"
    spaceWidth=textWidthScalebility-len(category)
    if spaceWidth%2==0:
        finalReturn+=f"|{" "*(int(spaceWidth/2))}{category}{" "*(int(spaceWidth/2))}|\n"
    else:
        finalReturn+=f"|{" "*(int((spaceWidth-1)/2))}{category}{" "*(int(((spaceWidth-1)/2)+1))}|\n"
    finalReturn+=vertex
    finalReturn+="\n"
    titleList=list(functionDict.keys())
    for i in range(len(titleList)):
        item=f" {i+1}. {titleList[i]}"
        finalReturn+=f"|{item+" "*(textWidthScalebility-len(item))}|\n"
    item=f" {len(titleList)+1}. Exit {category} Menu"
    finalReturn+=f"|{item+" "*(textWidthScalebility-len(item))}|\n"
    finalReturn+=vertex
    return finalReturn


def main():
    while True:
        print(getCategoryTitlesMenu(functionDict))
        choice=int(input("Enter the option you want to chose: "))
        if choice==(len(list(functionDict.keys()))+1):
            print(f"Exiting Main Menu!")
            break
        category=list(functionDict.keys())[choice-1]
        if category=="Library":
            Library=[]
            while True:
                print(getCategoryTitlesMenu(functionDict,category))
                choice=int(input("Enter the option you want to chose: "))
                if choice==(len(list(functionDict[category].keys()))+1):
                    print(f"Exiting {category} Menu!")
                    break
                function,inputfunction=list(functionDict[category].values())[choice-1]
                function(*inputfunction(Library))

main()