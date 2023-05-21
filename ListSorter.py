import csv
import json
import math
import sys 
import ntpath
import os

if len(sys.argv) != 2:
    print("Error: Incorrect number of arguments.\n" +
    "Input a file path to a litematica material list file.\n" +
    "Ex. python listSorter.py <path to minecraft>\.minecraft\config\litematica\material_list_###.txt")
    sys.exit()

if (not os.path.isfile(sys.argv[1])):
    print("Error: File does not exist - " + sys.argv[1])
    sys.exit()

with open(sys.argv[1], newline='') as materialFile:
    fieldnames = ['blank', 'item', 'count', 'available', 'missing', 'blank2']
    wantedFieldNames = ['item','count']
    dictReader = csv.DictReader(materialFile, fieldnames, delimiter='|')
    itemList = list()
    for dict in dictReader:
        # create new dict only using item and count fields
        newDict = {x:dict[x] for x in wantedFieldNames}
        if (newDict["item"] is not None):
            # strip whitespace from each dict item
            strippedDict = { k:v.strip() for k, v in newDict.items()}
            itemList.append(strippedDict)
    # remove header and footer
    itemList.pop(0)
    itemList.pop(0)
    itemList.pop(-1)



with open(os.path.join(os.getcwd(), 'block-data', 'blockdata.json'), 'r') as blockDataFile:
    blocklist = json.load(blockDataFile)


with open(os.path.join(os.getcwd(), 'block-data', 'order.csv'), 'r') as orderFile:
    orderDict = {}
    reader = csv.reader(orderFile)
    for row in reader:
        orderDict[row[0]] = row[1]
    print(orderDict)

# organize items by block family and calculate stack/shulker counts
for item in itemList:
    matchingBlocks = list(filter(lambda block: block['displayName'] == item['item'], blocklist))
    if matchingBlocks:
        item['stackSize'] = matchingBlocks[0]['stackSize']
        item['order'] = orderDict[matchingBlocks[0]['family']]
        print(item['item'])
        print(matchingBlocks[0]['family'])
        print(item['order'])
    else:
        item['stackSize'] = 64
        item['order'] = orderDict['etc']
        print("no match for " + item['item'])
    stackCount = int(item['count']) / item['stackSize']
    item['stacks'] = 0 if stackCount < 1 else math.ceil(stackCount)
    shulkerCount = stackCount / 27
    item['shulkers'] = 0 if shulkerCount < 1 else math.ceil(shulkerCount)

sortedItemList = sorted(itemList, key=lambda x: int(x['order']))

# create lists folder
fileName = ntpath.basename(sys.argv[1]).replace('.txt', '_sorted.csv')
path = os.path.join(os.getcwd(), 'lists')
if not os.path.exists(path):
    os.mkdir(path)

# print out csv
outputFile = os.path.join(path, fileName)
print("Printing sorted csv to " + outputFile)
with open(outputFile, 'w', newline='') as sortedCsv:
    writer = csv.DictWriter(sortedCsv, fieldnames=['item', 'count', 'stacks', 'shulkers'], extrasaction='ignore')
    writer.writeheader()
    writer.writerows(sortedItemList)