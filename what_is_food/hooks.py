# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "what_is_food"
app_title = "What Is Food"
app_publisher = "GreyCube Technologies"
app_description = "Customization for What is Food"
app_icon = "octicon octicon-device-mobile"
app_color = "yellow"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/what_is_food/css/what_is_food.css"
app_include_js = "/assets/what_is_food/js/lib/ag-grid-community.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/what_is_food/css/what_is_food.css"
# web_include_js = "/assets/what_is_food/js/what_is_food.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"
on_session_creation = "what_is_food.api.on_session_creation"
# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "what_is_food.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "what_is_food.install.before_install"
# after_install = "what_is_food.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "what_is_food.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"what_is_food.tasks.all"
# 	],
# 	"daily": [
# 		"what_is_food.tasks.daily"
# 	],
# 	"hourly": [
# 		"what_is_food.tasks.hourly"
# 	],
# 	"weekly": [
# 		"what_is_food.tasks.weekly"
# 	]
# 	"monthly": [
# 		"what_is_food.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "what_is_food.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "what_is_food.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "what_is_food.task.get_dashboard_data"
# }
