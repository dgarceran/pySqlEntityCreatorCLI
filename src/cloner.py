from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
import config as cfg
import os
from shutil import copyfile
import creator as c

def nameToSearch() :
	questions = [
		{
			'type': 'input',
			'message': 'Which table do you want to copy?',
			'name': 'tableToCopy'
		}
	]

	answers = prompt(questions)
	return (answers['tableToCopy'])

def nameToSearch() :
	questions = [
		{
			'type': 'input',
			'message': 'Which table do you want to copy?',
			'name': 'tableToCopy'
		}
	]

	answers = prompt(questions)
	return (answers['tableToCopy'])

def selectorOfTable(files) :
	questions = [
		{
			'type': 'list',
			'message': 'Select the file you want to copy',
			'name': 'file',
			'choices': [],
			'validate': lambda answer: 'You must choose at least one.' \
			if len(answer) == 0 else True
		}
	]

	i = 0
	for f in files:
		questions[0]['choices'].append(f)
		i = i + 1

	answers = prompt(questions)
	return (answers['file'])

def replaceTextElements() :
	questions = [
		{
			'type': 'confirm',
			'message': 'Do you want to replace text elements?',
			'name': 'replace'
		}
	]

	answers = prompt(questions)
	return (answers['replace'])

def wordToReplace(oldName) :
	questions = [
		{
			'type': 'input',
			'message': 'Word to replace',
			'name': 'wordToReplace',
			'default': oldName
		}
	]

	answers = prompt(questions)
	return (answers['wordToReplace'])

def newWord(newName) :
	questions = [
		{
			'type': 'input',
			'message': 'New word',
			'name': 'newWord',
			'default': newName
		}
	]

	answers = prompt(questions)
	return (answers['newWord'])

def searchEntityFiles(searchName) :
	files = []
	foundFiles = list()
	# r=root, d=directories, f = files
	for r, d, f in os.walk(cfg.srcUrl):
		for file in f:
			if '_' + searchName in file and 'Table' in file:
				files.append(os.path.join(r, file))

	for f in files:
		arrayElements = f.split('\\')
		foundFiles.append(arrayElements[len(arrayElements) - 1])

	return foundFiles

def copyElement(newFileName, fileName) :
	src = ''
	for r, d, f in os.walk(cfg.srcUrl):
		for file in f:
			if fileName in file:
				src = os.path.join(r, file)
	copyfile(src, 'files/V1_0__Create_Table_' + newFileName + '.sql')

def replaceElements(tableName, choosenFile):
	replacedWord = wordToReplace(choosenFile)
	replaceWord = newWord(tableName)

	sqlFile = open('files/V1_0__Create_Table_' + tableName + '.sql', 'r')
	replacedText = sqlFile.read().replace(replacedWord, replaceWord);
	sqlFileR = open('files/V1_0__Create_Table_' + tableName + '.sql', 'w')
	sqlFileR.write(replacedText)

def cleanChoosenFile(choosenFile):
	arrayElements = choosenFile.split('\\')
	internalArrayOfElements = arrayElements[len(arrayElements) - 1].split('_')
	return internalArrayOfElements[len(internalArrayOfElements) - 1].replace('.sql', '');

def cloneFile() : 
	# ask for name of the new file
	tableName = c.nameOfTable()
	# ask for name of the file to copy - use searchEntityFiles()
	files = searchEntityFiles(nameToSearch())
	choosenFile = selectorOfTable(files)

	# call copyElement() with the new file name and the choosen file
	copyElement(tableName, choosenFile)

	# ask to replace element names
	if replaceTextElements() is True :
		replaceElements(tableName, cleanChoosenFile(choosenFile))
