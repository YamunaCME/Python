const ctx =
document.getElementById("accuracyChart");

new Chart(ctx, {

type:"line",

data:{

labels:[
"Mon",
"Tue",
"Wed",
"Thu",
"Fri",
"Sat",
"Sun"
],

datasets:[{

label:"OCR Accuracy",

data:[
90,
92,
95,
96,
97,
96,
98
],

borderWidth:3

}]

}

});

const darkBtn =
document.getElementById("darkModeBtn");

darkBtn.addEventListener("click",()=>{

document.body.classList.toggle("light-mode");

});