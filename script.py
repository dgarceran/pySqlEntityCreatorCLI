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

def createNewTable():
	name = nameOfTable()
	systemOrBasic = askForSystemOrEntity()
	keepAddingColumn = True
	tab = '  '

	sqlFile = open('files/V1_0__Create_Table_' + name + '.sql', 'w')
	sqlFile.write('CREATE TABLE ' + name + ' (\n')
	sqlFile.write(tab + 'Id ' + tab + 'int IDENTITY NOT NULL,\n')

	while keepAddingColumn :
		columnName = askForColumnName()
		columnType = askForColumnType()
		columnSize = ''

		if columnType.encode("utf-8") == "varchar".encode("utf-8") :
			columnSize = askForColumnSize()

		sqlFile.write(tab)
		sqlFile.write(columnName + tab + columnType)

		if columnSize is not '':
			sqlFile.write('(' + columnSize + ')')

		if(isNullable() is True) :
			sqlFile.write(' NULL')
		else :
			sqlFile.write(' NOT NULL')

		if(isUnique() is True) :
			sqlFile.write(' UNIQUE')

		keepAddingColumn = addAnotherColumn()
		print(keepAddingColumn)
		sqlFile.write(',\n')

	sqlFile.write('CONSTRAINT PK' + name + '\n')
	sqlFile.write('PRIMARY KEY (Id)\n')
	sqlFile.write(');\n')

def callMenus() : 
	global isFinished
	
	isFinished = False

	while isFinished is False :
		 createNewTable()
		 isFinished = exitApp()

def testMenus(): 
	questions = [
		{
			'type': 'input',
			'message': 'Name of the table',
			'name': 'tableName'
		}
	]

	answers = prompt(questions)
	return (answers['tableName'])

callMenus()