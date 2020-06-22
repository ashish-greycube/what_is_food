from frappe import _
from frappe.sessions import Session
import frappe

def on_session_creation(login_manager):
	print('*'*100)
	frappe.response['type'] = 'redirect'
	frappe.response.location = '/desk#trackme'
	# frappe.local.response["home_page"] = "/desk#trackme"
