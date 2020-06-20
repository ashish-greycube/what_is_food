from frappe import _
from frappe.sessions import Session
import frappe

def on_session_creation(login_manager):
	frappe.local.response["home_page"] = "/desk#Form/Track%20Me"