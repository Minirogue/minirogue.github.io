#!/usr/bin/env python3

import csv
import json

def main():
	convertToJsonByWholeItem('people')
	convertToJsonByWholeItem('companies')
	convertToJsonByWholeItem('media_types')
	convertToJsonByWholeItem('series')
	convertToJsonByWholeItem('database')
	convertToJsonById('version', idString='name')

def convertToJsonByWholeItem(csvName):
	itemList = list()
	with open('csv/%s.csv' % csvName) as csvFile:
		reader = csv.DictReader(csvFile)
		for row in reader:
			itemList.append(row)
	with open('json/%s.json' % csvName, 'w') as jsonFile:
		jsonFile.write(json.dumps(itemList, indent=4))

def convertToJsonById(csvName, idString):
	itemDict = dict()
	with open('csv/%s.csv' % csvName) as csvFile:
		reader = csv.DictReader(csvFile)
		for row in reader:
			itemDict[row[idString]] = row
	with open('json/%s.json' % csvName, 'w') as jsonFile:
		jsonFile.write(json.dumps(itemDict, indent=4))


if __name__ == '__main__':
	main()