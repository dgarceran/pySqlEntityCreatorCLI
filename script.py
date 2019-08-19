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

def exitApp(isFinishedExternal) : 
	global isFinished

	if isFinishedExternal is '':
		isFinishedUser = raw_input("Exit? [Y/N]")

		if isFinishedUser is "Y" or isFinishedUser is "y":
			isFinished = True
		else :
			isFinished = False
	else : 
		isFinished = isFinishedExternal

def addAnotherColumn() : 
	addAnotherOne = raw_input("Add another column? [Y/N]")
	print("user says: " + addAnotherOne)
	if addAnotherOne is "Y" or addAnotherOne is "y":
		return True
	else :
		return False

def nameOfTable() :
	return raw_input("Name of table\n")

def askForSystemOrEntity() :
	return raw_input("Is it a system table [0] or basic table [1]? (NOT WORKING YET)\n")

def askForColumnName() :
	return raw_input("Column name\n")

def askForColumnType() :
	return raw_input("Column type\n")

def isNullable() :
	isNullable = raw_input("Is nullable? [Y/N]\n")

	if isNullable is "Y" or isNullable is "y":
		return True
	else :
		return False

def isUnique() :
	isUnique = raw_input("Is unique? [Y/N]\n")

	if isUnique is "Y" or isUnique is "y":
		return True
	else :
		return False

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

		sqlFile.write(tab)
		sqlFile.write(columnName + tab + columnType)

		if(isNullable() is True) :
			sqlFile.write(' NOT NULL')
		else :
			sqlFile.write(' NULL')

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
	exitApp(False)

	while isFinished is False :
		 createNewTable()
		 exitApp('')

callMenus()