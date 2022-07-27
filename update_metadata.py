import json

collectionName = "mycollectionname"
parentLink = "pinatacloudlink"
fileName = "propzz.txt"
outputFolder = "metadata"

def mainFunc():
    f = open(fileName, "r")
    f_lines = f.readlines()
    curNameAndCheck = ["name", False]
    curList = []
    for line in f_lines:
        if line[0] == "{":
            print("Reading entry " + curNameAndCheck[0] + "...")
            curNameAndCheck[1] = True
            curList.clear()
        elif line[0] == "}":
            generateMetaData(curNameAndCheck[0], curList)
            print("Closing entry " + curNameAndCheck[0] + "...")
            curNameAndCheck[0] = "Error"
            curNameAndCheck[1] = False
            curList.clear()
        elif curNameAndCheck[1]:
            (atrType, atrValue) = line.split()
            atrType, atrValue = atrType[:-1], atrValue[:-1] if atrValue[-1] == "," else atrValue
            atrType = atrType[1:-1]
            atrValue = atrValue[1:-1] 
            curObj = getAttribute()
            curObj["trait_type"] = atrType
            curObj["value"] = atrValue
            if atrType == "name":
                print("Changed name to " + atrValue)
                curNameAndCheck[0] = atrValue
            else:
                curList.append(curObj)
    f.close()

def generateMetaData(name, curList):
    print("--Generating object " + name + " --")
    print("DATA: " + name)
    newObj = getObjJson()
    newObj["image"] = parentLink + name + ".png"
    newObj["tokenId"] = int(name)
    newObj["name"] = "bear " + name
    newObj["attributes"] = curList
    f = open("./metadata/" + name + ".json", "x")
    json.dump(newObj, f)
    f.close()
    print("--Successfully generated object " + name + " --")

def getObjJson():
    return {
        "image": "",
        "tokenId": 0,
        "name": "",
        "attributes": []
        }

def getAttribute():
    return {
        "trait_type": "", 
        "value": ""
        }

mainFunc()