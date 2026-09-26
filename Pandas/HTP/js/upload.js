const fileInput =
document.getElementById("fileInput");

const previewImage =
document.getElementById("previewImage");

const uploadBtn =
document.getElementById("uploadBtn");

const progressBar =
document.getElementById("uploadProgress");

fileInput.addEventListener("change",(e)=>{

const file =
e.target.files[0];

if(!file)
return;

const validTypes =

[
"image/jpeg",
"image/png",
"image/bmp"
];

if(!validTypes.includes(file.type)){

alert("Only JPG PNG BMP allowed");

return;

}

const reader =
new FileReader();

reader.onload=function(event){

previewImage.src=
event.target.result;

previewImage.style.display=
"block";

};

reader.readAsDataURL(file);

});

uploadBtn.addEventListener("click",()=>{

let progress = 0;

let interval =
setInterval(()=>{

progress += 10;

progressBar.style.width=
progress+"%";

progressBar.innerText=
progress+"%";

if(progress>=100){

clearInterval(interval);

alert("Upload Successful");

}

},200);

});