
for (let index = 0; index < document.querySelectorAll(".drum").length; index++) {
    document.querySelectorAll("button")[index].addEventListener("click",function(){
        
        var buttonInnerHTML=this.innerHTML;
        playSound(buttonInnerHTML);
        buttonAnimation(buttonInnerHTML);
    });
}

document.addEventListener("keydown",function(event){
    var letter=event.key;
    playSound(letter);
    buttonAnimation(letter);
}) 




function playSound(letter){
        
        switch (letter) {
            case "w":
                var audio=new Audio("/static/section6/tom-1.mp3");
                audio.play();
                break;
            case "a":
                var audio=new Audio("/static/section6/tom-2.mp3");
                audio.play();
                break;
            case "s":
                var audio=new Audio("/static/section6/tom-3.mp3");
                audio.play();
                break;
            case "d":
                var audio=new Audio("/static/section6/tom-4.mp3");
                audio.play();
                break;
            case "j":
                var audio=new Audio("/static/section6/snare.mp3");
                audio.play();
                break;
            case "k":
                var audio=new Audio("/static/section6/kick-bass.mp3");
                audio.play();
                break;
            case "l":
                var audio=new Audio("/static/section6/crash.mp3");
                audio.play();
                break;
            default:
                console.log(letter)
                break;
        }
}



function buttonAnimation(letter){
    var activeButton=document.querySelector("."+letter);
    
    activeButton.classList.add("pressed");
    
    setTimeout(function(){
        activeButton.classList.remove("pressed");
    },100)

}