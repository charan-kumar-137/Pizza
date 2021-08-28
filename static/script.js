// Initialization
document.getElementById('submit').addEventListener('click', getData);
let action = document.getElementById('action');
let method = document.getElementById('method');
let id = document.getElementById('id')
let name = document.getElementById('name')
let type = document.getElementById('type')
let size = document.getElementById('size')
let toppings = document.getElementById('toppings')

let idInput = document.getElementById('idInput')
let nameInput = document.getElementById('nameInput')
let typeInput = document.getElementById('typeInput')
let sizeInput = document.getElementById('sizeInput')
let toppingsInput = document.getElementById('toppingsInput')

let response = document.getElementById('response');


/*
 desctiption - get the details from the form and make a request to the server and show the response

*/
function getData() {
	id_value = id.value;
	name_value = name.value;
	type_value = type.value;
	size_value = size.value;
	toppings_value = toppings.value;

	action_string = action.value
	method_string = method.value

	let xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		response.innerHTML = xhttp.responseText;
	};

	let url = 'http://127.0.0.1:8000/' + 'api/';

	if (action_string == 'CREATE') {
		xhttp.open(method_string, url + 'create', true);
		request_string = "name=" + name_value + "&type=" + type_value + "&size=" + size_value + "&toppings=" + toppings_value;
		xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		xhttp.send(request_string);

	} else if (action_string == 'GET') {
		xhttp.open(method_string, url + 'get/' + id_value, true);
		xhttp.send();

	} else if (action_string == 'LIST') {
		xhttp.open(method_string, url + 'list', true);
		xhttp.send();

	} else if (action_string == 'EDIT') {
		xhttp.open(method_string, url + 'edit/' + id_value, true);
		request_string = "name=" + name_value + "&type=" + type_value + "&size=" + size_value + "&toppings=" + toppings_value;
		xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		xhttp.send(request_string);

	} else if (action_string == 'DELETE') {
		xhttp.open(method_string, url + 'delete/' + id_value, true);
		xhttp.send();
	}


}

/*
 description - Render the form based on the choice made on the action by the user

*/

function renderForm() {
	action_string = action.value
	if (action_string == 'CREATE') {
		idInput.hidden = true;
		nameInput.hidden = false;
		typeInput.hidden = false;
		sizeInput.hidden = false;
		toppingsInput.hidden = false;
	} else if (action_string == 'GET') {
		idInput.hidden = false;
		nameInput.hidden = true;
		typeInput.hidden = true;
		sizeInput.hidden = true;
		toppingsInput.hidden = true;
	} else if (action_string == 'LIST') {
		idInput.hidden = true;
		nameInput.hidden = true;
		typeInput.hidden = true;
		sizeInput.hidden = true;
		toppingsInput.hidden = true;
	} else if (action_string == 'EDIT') {
		idInput.hidden = false;
		nameInput.hidden = false;
		typeInput.hidden = false;
		sizeInput.hidden = false;
		toppingsInput.hidden = false;
	} else if (action_string == 'DELETE') {
		idInput.hidden = false;
		nameInput.hidden = true;
		typeInput.hidden = true;
		sizeInput.hidden = true;
		toppingsInput.hidden = true;
	}
}
