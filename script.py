from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

''' 
BASIC SCRIPT THAT CREATES A TABLE FROM USER INPUT
*************************************************

1) ask if the table is system or entity (to add created/modified user/date).
2) ask name of each property until the user says there is no more
3) for each property ask for the db type
4) ask for lenght if var
5) ask for nullable
6) ask default
'''
tables = list()

def exitApp() : 
	global isFinished

	questions = [
		{
			'type': 'confirm',
			'message': 'Do you want to exit?',
			'name': 'exit'
		}
	]

	answers = prompt(questions)
	return (answers['exit'])

def addAnotherColumn() : 
	questions = [
		{
			'type': 'confirm',
			'message': 'Do you want to add another column?',
			'name': 'addAnotherColumn'
		}
	]

	answers = prompt(questions)
	return (answers['addAnotherColumn'])

def nameOfTable() :
	questions = [
		{
			'type': 'input',
			'message': 'Name of the table',
			'name': 'tableName'
		}
	]

	answers = prompt(questions)
	return (answers['tableName'])

def askForSystemOrEntity() :
	questions = [
		{
			'type': 'list',
			'message': 'Is this entity from system or a basic entity?',
			'name': 'systemOrEntity',
			'choices': [
				{'name': 'system'},
				{'name': 'basic'}
			],
			'validate': lambda answer: 'You must choose at least one.' \
			if len(answer) == 0 else True
		}
	]

	answers = prompt(questions)
	return (answers['systemOrEntity'])

def askForColumnName() :
	questions = [
		{
			'type': 'input',
			'message': 'Name of the column',
			'name': 'columnName'
		}
	]

	answers = prompt(questions)
	return (answers['columnName'])

def askForColumnType() :
	questions = [
		{
			'type': 'list',
			'message': 'Select type',
			'name': 'type',
			'choices': [
				{'name': 'int'},
				{'name': 'varchar'},
				{'name': 'datetime2'}
			],
			'validate': lambda answer: 'You must choose at least one.' \
			if len(answer) == 0 else True
		}
	]

	answers = prompt(questions)
	return (answers['type'])

def askForColumnSize() :
	questions = [
		{
			'type': 'input',
			'message': 'Size of the column',
			'name': 'columnSize'
		}
	]

	answers = prompt(questions)
	return (answers['columnSize'])

def askForTableTarget() :
	questions = [
		{
			'type': 'input',
			'message': 'Name of the table to target in the relationship',
			'name': 'tableTarget'
		}
	]

	answers = prompt(questions)
	return (answers['tableTarget'])

def askForColumnTarget() :
	questions = [
		{
			'type': 'input',
			'message': 'Name of the column to target in the relationship',
			'name': 'columnTarget'
		}
	]

	answers = prompt(questions)
	return (answers['columnTarget'])


def isNullable() :
	questions = [
		{
			'type': 'confirm',
			'message': 'Is it nullable?',
			'name': 'isItNullable'
		}
	]

	answers = prompt(questions)
	return (answers['isItNullable'])

def isUnique() :
	questions = [
		{
			'type': 'confirm',
			'message': 'Is it unique?',
			'name': 'isItUnique'
		}
	]

	answers = prompt(questions)
	return (answers['isItUnique'])

def addRelation() :
	questions = [
		{
			'type': 'confirm',
			'message': 'Add a relationship of a column with another one?',
			'name': 'addRelation'
		}
	]

	answers = prompt(questions)
	return (answers['addRelation'])

def checkOneColumn(columns) :
	questions = [
		{
			'type': 'list',
			'message': 'Select column to add a relation (DOES NOT WORKS)',
			'name': 'column',
			'choices': [],
			'validate': lambda answer: 'You must choose at least one.' \
			if len(answer) == 0 else True
		}
	]

	i = 0
	for c in columns:
		questions[0]['choices'].append(c)
		i = i + 1

	answers = prompt(questions)
	return (answers['column'])

def createNewTable():
	name = nameOfTable()
	tables.append(name)
	systemOrBasic = askForSystemOrEntity()
	keepAddingColumn = True
	tab = '  '
	columns = list()
	sqlFileToWrite = ''

	sqlFileToWrite += 'CREATE TABLE ' + name + ' (\n'
	sqlFileToWrite += tab + 'Id ' + tab + 'int IDENTITY NOT NULL,\n'

	while keepAddingColumn :
		columnName = askForColumnName()
		columnType = askForColumnType()
		columnSize = ''
		columns.append(columnName)

		if columnType.encode("utf-8") == "varchar".encode("utf-8") :
			columnSize = askForColumnSize()

		sqlFileToWrite += tab + columnName + tab + columnType

		if columnSize is not '':
			sqlFileToWrite += '(' + columnSize + ')'

		if(isNullable() is True) :
			sqlFileToWrite += ' NULL'
		else :
			sqlFileToWrite += ' NOT NULL'

		if(isUnique() is True) :
			sqlFileToWrite += ' UNIQUE'

		sqlFileToWrite += ',\n'
		keepAddingColumn = addAnotherColumn()

	if systemOrBasic == 'basic' :
		sqlFileToWrite += tab +'CreatedDate' + tab + 'datetime2 DEFAULT SYSUTCDATETIME() NOT NULL,\n'
		sqlFileToWrite += tab +'ModifiedDate' + tab + 'datetime2 NULL,\n'
		sqlFileToWrite += tab +'CreatedUser' + tab + 'int NULL,\n'
		sqlFileToWrite += tab +'ModifiedUser' + tab + 'int NULL,\n'

	sqlFileToWrite += tab +'CONSTRAINT PK' + name + '\n'
	sqlFileToWrite += tab +'PRIMARY KEY (Id)\n'
	sqlFileToWrite += ');\n'

	while addRelation() is True :
		column = checkOneColumn(columns)
		tableTarget = askForTableTarget()
		columnTarget = askForColumnTarget()

		sqlFileToWrite += 'ALTER TABLE ' + name + ' ADD CONSTRAINT FK' + name + column + ' FOREIGN KEY (' + column + ') REFERENCES ' + tableTarget + ' (' + columnTarget + ');\n'

	sqlFile = open('files/V1_0__Create_Table_' + name + '.sql', 'w')
	sqlFile.write(sqlFileToWrite)

def callMenus() : 
	global isFinished
	
	isFinished = False

	while isFinished is False :
		 createNewTable()
		 isFinished = exitApp()

callMenus()