from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	config = [
		{
			"label": _("Mobile"),
			"items": [
				{
					"type": "page",
					"name": "trackme",
					"label": _("Track Inventory"),
					"icon": "fa fa-bar-chart",
				},                
				{
					"type": "report",
					"name": "Driver Commission",
					"is_query_report": True,
					"doctype": "Sales Invoice"
				},
                {
                        "type": "report",
                        "name": "Driver Commission Detail",
                        "is_query_report": True,
                        "doctype": "Sales Invoice"
                }
			]
		}]
	return config
