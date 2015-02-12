import requests, json, re, os, sys
import xml.etree.ElementTree as ET

class UpdateSetFetcher():
	def __init__(self):
		print 'Parsing through your Update Set!'

	def main(self, args):
		print args[1] + " is the Update Set Name"
		r = requests.get("https://" + args[3] + ".service-now.com/sys_update_xml.do?JSON&sysparm_query=update_set.name=" + args[1], auth=(args[2], self.password[3]));
		data = r.json()['records']
		for x in range(0, len(data)):
			dataType = data[x]['type']
			targetName = data[x]['target_name']
			updater = data[x]['sys_updated_by']
			updated = data[x]['sys_updated_on']
			statement =  targetName + " of type " + dataType + " was updated by " + updater + " on " + updated	
			payload =  data[x]['payload'].encode('utf-8')	
			tableName = self.determinteTableName(data[x]['name'])
			tree = ET.fromstring(payload)
			sysIDs = tree.findall("./" + tableName + "//sys_id")
			for item in sysIDs:
				print self.getUpdateInformation(item.text, tableName)
			
	def getUpdateInformation(self, sysID, tableName):
		req = requests.get("https://scrippsdev.service-now.com/" + tableName +".do?JSON&sysparm_query=sys_id=" + sysID, auth=(args[2], self.password[3]))
		data = req.json()['records']
		return data

	def determinteTableName(self, name):
		return name[0:name.rindex('_')]	