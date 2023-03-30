 
var randomNumber1=Math.floor(Math.random() * 6)+1;
var randomNumber2=Math.floor(Math.random() * 6)+1;

var imagePath1="/static/section6/dice"+randomNumber1+".png"
var imagePath2="/static/section6/dice"+randomNumber2+".png"


document.querySelector(".img1").setAttribute("src", imagePath1);
document.querySelector(".img2").setAttribute("src", imagePath2);



if (randomNumber1==randomNumber2) {
    document.querySelector("h1").innerHTML="DRAW";
}

if (randomNumber1>randomNumber2) {
    document.querySelector("h1").innerHTML="Player 1 Win";
}

if (randomNumber1<randomNumber2) {
    document.querySelector("h1").innerHTML="Player 2 Win";
}
