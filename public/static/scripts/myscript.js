function showDiv()
{	
	if(document.getElementById("contactIcons").style.display="none"){
	$("#contactIcons").fadeIn();
	}
/*	var contactBox = document.getElementById("contactIcons");
	contactBox.style.display = "inherit";*/
}

function hideDiv()
{
	/*var contactBox = document.getElementById("contactIcons");
	contactBox.style.display = "none";*/
	$("#contactIcons").fadeOut(200);
}