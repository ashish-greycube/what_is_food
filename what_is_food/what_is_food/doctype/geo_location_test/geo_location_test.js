frappe.ui.form.on('Geo Location Test', {
	am_in_office: function (frm) {

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(showPosition);
		} else {
			alert("Geolocation is not supported by this browser.");
		}

		function showPosition(position) {
			alert('Your latitude is  '+position.coords.latitude+ ' and logitude is  '+position.coords.longitude)
			alert ('office is at '+ frm.doc.latitude, frm.doc.longitude)
			alert('You are ' + calcCrow(position.coords.latitude, position.coords.longitude, frm.doc.latitude, frm.doc.longitude).toFixed(1) + ' kms away from office');
		}
		//This function takes in latitude and longitude of two location and returns the distance between them as the crow flies (in km)
		function calcCrow(lat1, lon1, lat2, lon2) {
			var R = 6371; // km
			var dLat = toRad(lat2 - lat1);
			var dLon = toRad(lon2 - lon1);
			var lat1 = toRad(lat1);
			var lat2 = toRad(lat2);

			var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
				Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(lat2);
			var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
			var d = R * c;
			return d;
		}
		// Converts numeric degrees to radians
		function toRad(Value) {
			return Value * Math.PI / 180;
		}
	}
});