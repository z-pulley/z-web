function clearInput(val, input) {
	if(input.value == val) {
		input.value = "";
	}
	
	input.className = "text-input black";
}

function restoreInput(val, input) {
	if(input.value == "") {
		input.value = val;
		input.className = "text-input";
	}
}

function validEmail(email) {
  var filter = /^([a-zA-Z0-9_.-])+@([a-zA-Z0-9_.-])+\.([a-zA-Z])+([a-zA-Z])+/;
  if (!filter.test(email)) {
    return false;
  } else {
    return true;
  }
}

function submitForm() {
	var input = document.getElementById('email-address');
	
	if(!validEmail(input.value)) {
		input.className = "text-input error";
		return false;
	} else {
		input.className = "text-input black";
	}
	
	return true;
}