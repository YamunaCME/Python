document.addEventListener("DOMContentLoaded",()=>{

const loginForm =
document.getElementById("loginForm");

if(loginForm){

loginForm.addEventListener("submit",(e)=>{

e.preventDefault();

let email =
document.getElementById("email").value;

let password =
document.getElementById("password").value;

if(email==="" || password===""){
alert("All fields required");
return;
}

window.location.href=
"dashboard.html";

});

}

const registerForm =
document.getElementById("registerForm");

if(registerForm){

registerForm.addEventListener("submit",(e)=>{

e.preventDefault();

let p1=
document.getElementById("regPassword").value;

let p2=
document.getElementById("confirmPassword").value;

if(p1!==p2){

alert("Passwords do not match");
return;

}

alert("Registration Success");

window.location.href=
"login.html";

});

}

});