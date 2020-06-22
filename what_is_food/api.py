from frappe import _
from frappe.sessions import Session
import frappe
import json

def on_session_creation(bootinfo):
	print('*'*100)
	bootinfo['home_page'] = 'trackme'
	# frappe.response['type'] = 'redirect'
	# frappe.response.location = 'http://localhost:8000/desk#trackme'
	# frappe.local.response["home_page"] = "/desk#trackme"
