import requests


class classDojo():
	#Init
	def __init__(self, classId, cookie):
		self.PUPIL_URL = f"https://teach.classdojo.com/api/dojoClass/{classId}/student"
		self.GROUP_URL = f"https://teach.classdojo.com/api/dojoClass/{classId}/group"
		self.userAgent = {'User-agent': 'Mozilla/5.0', "cookie": cookie}

		self.refresh()

		self.IndexedPupilData = {}

		for i in range(len(self.pupilData['_items'])):
			self.IndexedPupilData[i] = self.pupilData['_items'][i]

		self.IndexedGroupData = {}

		for i in range(len(self.groupData['_items'])):
			self.IndexedGroupData[i] = self.groupData['_items'][i]


	#Get Data From API
	def refresh(self):
		response = requests.get(self.PUPIL_URL, headers=self.userAgent)
		self.pupilData = response.json()

		response = requests.get(self.GROUP_URL, headers=self.userAgent)
		self.groupData = response.json()

	#Get Amount of Points by Index in IndexedPupilData
	def getPointsByIndexOfPupil(self, index):
		positive = self.IndexedPupilData[index]['positivePoints']
		negative = self.IndexedPupilData[index]['negativePoints']
		return positive - negative

	#Get Amount of Points by Index in IndexedGroupData
	def getPointsByIndexOfGroup(self, index):#
		positive = self.IndexedGroupData[index]['positivePoints']
		negative = self.IndexedGroupData[index]['negativePoints']
		return positive - negative

	#Get Index of Last Name in IndexedPupilData
	def getIndexByLastName(self, lastname):

		for i in range(len(self.IndexedPupilData)):
			if self.IndexedPupilData[i]['lastName'] == lastname:
				return i

		return -1

	#Get Index of Group Name in IndexedGroupData
	def getIndexByGroupName(self, groupname):
		for i in range(len(self.IndexedPupilData)):
			if self.IndexedGroupData[i]['name'] == groupname:
				return i

		return -1

	#Combines getIndexByLastName and getPointsByIndexOfPupil to make a more user friendly function
	def getPointsByLastName(self, lastname):
		index = self.getIndexByLastName(lastname)

		if (index == -1):
			return ("Surname not in class")

		return self.getPointsByIndexOfPupil(index)

	#Combines getIndexByGroupName and getPointsByIndexOfGroup to make a more user friendly function
	def getPointsByGroupName(self, groupname):
		index = self.getIndexByGroupName(groupname)

		if (index == -1):
			return ("Group not in class")

		return self.getPointsByIndexOfGroup(index)

	#Gets points by combining surname followed by first letter of first name eg. DoeJ
	def getPointsByCombinedName(self, name):
		for i in range(len(self.IndexedPupilData)):
			if self.IndexedPupilData[i]['firstName'][0] == name[-1:] and self.IndexedPupilData[i]['lastName'] == name[:-1]:
				index = i
				break
		
		return self.getPointsByIndexOfPupil(index)

classId = "5f80a73155fc639d90406ded"
cookie = 'dojo_log_session_id=7c03a8dc-d349-4553-8d32-479fc40a7798; _ga=GA1.2.898831097.1602269772; _gid=GA1.2.761379133.1602269772; dojorrt=1602354174700; dojo_login.sid=s%3ARoWQ7Dtwao3ZYVvC1xl0u1-VDJqDJH9q.sxsShkDasxGjsbxY%2BbbqSQOKlH%2Fk0Mn7HECB0EAGIWA; dojo_teach_login.sid=s:RoWQ7Dtwao3ZYVvC1xl0u1-VDJqDJH9q.sxsShkDasxGjsbxY+bbqSQOKlH/k0Mn7HECB0EAGIWA'

_class = classDojo(classId, cookie)
