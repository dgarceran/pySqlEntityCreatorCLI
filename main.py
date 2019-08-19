from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from src import Cloner, Creator, CodeNameTable

''' 
BASIC SCRIPT THAT CREATES A TABLE FROM USER INPUT
*************************************************
'''

def askForTypeOfWork() :
	questions = [
		{
			'type': 'list',
			'message': 'Which action do you want to do?',
			'name': 'action',
			'choices': [
				{
					'name': 'Create new table from scratch',
					'value': 'fromScratch'
				},
				{
					'name': 'Copy table from another one in the system',
					'value': 'copy'
				},
				{
					'name': 'Create code/name basic table',
					'value': 'codeName'
				},
				{
					'name': 'Exit',
					'value': 'exit'
				}
			],
			'validate': lambda answer: 'You must choose at least one.' \
			if len(answer) == 0 else True
		}
	]

	answers = prompt(questions)
	return (answers['action'])

def exitApp() : 
	questions = [
		{
			'type': 'confirm',
			'message': 'Do you want to exit?',
			'name': 'exit'
		}
	]

	answers = prompt(questions)
	return (answers['exit'])

def callMenus() :
	userWantsToExit = False
	while userWantsToExit is False :
		typeOfWork = askForTypeOfWork()

		if typeOfWork == 'fromScratch':
			Creator()

		if typeOfWork == 'copy':
			Cloner()

		if typeOfWork == 'codeName':
			CodeNameTable()

		if typeOfWork == 'exit':
			break

		userWantsToExit = exitApp()

callMenus()