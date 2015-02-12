import requests, json, re, os, sys
import xml.etree.ElementTree as ET

class UpdateSetFetcher():
	def __init__(self, args):
		print 'Parsing through your Update Set!'
		self.environment = args[4]
		self.username = args[2]
		self.password = args[3]
		self.updateSet = args[1]

	def main(self):
		print self.updateSet + " is the Update Set Name, Going into " + self.environment + " as " + self.username + ":" + self.password
		r = requests.get("https://" + self.environment + ".service-now.com/sys_update_xml.do?JSON&sysparm_query=update_set.name=" + self.updateSet, auth=(self.username, self.password));
		data = r.json()['records']
		for x in range(0, len(data)):
			dataType = data[x]['type']
			targetName = data[x]['target_name']
			updater = data[x]['sys_updated_by']
			updated = data[x]['sys_updated_on']
			statement =  targetName + " of type " + dataType + " was updated by " + updater + " on " + updated	
			print statement
			payload =  data[x]['payload'].encode('utf-8')	
			tableName = self.determineTableName(data[x]['name'])
			tree = ET.fromstring(payload)
			sysIDs = tree.findall("./" + tableName + "//sys_id")
			for item in sysIDs:
				print self.getUpdateInformation(item.text, tableName)
			
	def getUpdateInformation(self, sysID, tableName):
		req = requests.get("https://" + self.environment + ".service-now.com/" + tableName +".do?JSON&sysparm_query=sys_id=" + sysID, auth=(self.username, self.password))
		data = req.json()['records']
		return data

	def determineTableName(self, name):
		return name[0:name.rindex('_')]	