// Copyright (c) 2020, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Media', {
	table_2_on_form_rendered: function(frm) {
		console.log('inside child table..form is opened')

	}
});
frappe.ui.form.on('Media Child', {
	select1: function(frm) {
		console.log('Media Childinside child table..form is opened')

	}
});