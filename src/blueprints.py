from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator

from creator import nameOfTable, askForSystemOrEntity
from config import tab

def codeNameTableOptions() :
	questions = [
		{
			'type': 'checkbox',
			'message': 'Select extras',
			'name': 'extrasCodeNameTable',
			'choices': [ 
				{
					'name': 'Color code',
					'value': 'colorCode'
				},
				{
					'name': 'I18n name column',
					'value': 'i18n'
				},
				{
					'name': 'Basic entity columns',
					'value': 'basicEntity'
				}
			]
		}
	]

	answers = prompt(questions)
	return (answers['extrasCodeNameTable'])

def createCodeNameTable() :
	name = nameOfTable()
	tableOptions = codeNameTableOptions()

	sqlFileToWrite = ''

	sqlFileToWrite += 'CREATE TABLE ' + name + ' (\n'
	sqlFileToWrite += tab + 'Id ' + tab + 'int IDENTITY NOT NULL,\n'
	sqlFileToWrite += tab + 'Code ' + tab + ' varchar(10) NOT NULL UNIQUE,\n'
	sqlFileToWrite += tab + 'Name ' + tab + ' varchar(50) NOT NULL,\n'

	if 'colorCode' in tableOptions:
		sqlFileToWrite += tab + 'ColorCode ' + tab + ' varchar(7) NULL,\n'

	if 'i18n' in tableOptions:
		sqlFileToWrite += tab + 'NameI18nId ' + tab + ' int NULL,\n'

	if 'basicEntity' in tableOptions:
		sqlFileToWrite += tab +'CreatedDate' + tab + 'datetime2 DEFAULT SYSUTCDATETIME() NOT NULL,\n'
		sqlFileToWrite += tab +'ModifiedDate' + tab + 'datetime2 NULL,\n'
		sqlFileToWrite += tab +'CreatedUser' + tab + 'int NULL,\n'
		sqlFileToWrite += tab +'ModifiedUser' + tab + 'int NULL,\n'

	sqlFileToWrite += tab +'CONSTRAINT PK' + name + '\n'
	sqlFileToWrite += tab +'PRIMARY KEY (Id)\n'
	sqlFileToWrite += ');\n'

	if 'i18n' in tableOptions:
		sqlFileToWrite += 'ALTER TABLE ' + name + ' ADD CONSTRAINT FK' + name + 'NameI18n FOREIGN KEY (NameI18nId) REFERENCES I18n (Id);'

	sqlFile = open('files/V1_0__Create_Table_' + name + '.sql', 'w')
	sqlFile.write(sqlFileToWrite)