import os

print("combining human evaluations..\n\n")

evalPath = "../Human_Summaries/eval"
mergePath = "../Human_Summaries"


def writeFile(file,text):
    print(os.path.join(mergePath, file))
    f = open(os.path.join(mergePath, file),'a')
    f.write(text)
    f.close()



def readDocs(path):
    docAsList=[]
    for doc in os.listdir(path):
        docPath=os.path.join(path,doc)
        with open(docPath) as file:
            inText=file.read()
            docAsList.append(inText)
            outFile=doc.split('.')[0]
            print(outFile)
            writeFile(outFile,inText)

            file.close()

    return docAsList


readDocs(evalPath)


