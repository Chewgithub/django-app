
var userClickedPattern=[];

var gamePattern=[];

var cars = ["red", "blue", "green","yellow"];

let callCount=0;
let level = 0;
let gameStart=false;

var answer=false;
$(".btn").click(function () { 
    var userChosenColour=$(this).attr("id");
    playSound(userChosenColour);
    animatePress(userChosenColour);
    
    if (gameStart==true) {
        
        userClickedPattern.push(userChosenColour);
        console.log(gamePattern);
        console.log(userClickedPattern);
        answer=checkAnswer(userClickedPattern.length-1);

        if (answer==false) {
            playSound("wrong");
            $("body").addClass("game-over");

            setTimeout(function() {
                $("body").removeClass('game-over');
            }, 200);

            $("h1").text("Game Over, Press Any Key to Restart");
            startOver();

        }
        else{
        if (gamePattern.length==userClickedPattern.length) {
            setTimeout(function() {
                nextSequence();
            }, 1000);
            userClickedPattern=[];
        }
    }
    }


});


$(document).keypress(function (e) { 
    if (gameStart==false) {
        gameStart=true;
        nextSequence();
}});


function nextSequence(){
    var randomNumber=Math.floor(Math.random() * 4);

    var randomChosenColour=cars[randomNumber];

    gamePattern.push(randomChosenColour);
    
    $("div"+"#"+randomChosenColour).fadeOut(100).fadeIn(100).fadeOut(100).fadeIn(100);
    
    playSound(randomChosenColour);
    
    $("h1").text("Level "+level);
    level+=1;
    callCount+=1;
}


function playSound(name){
    var audio=new Audio("/static/section6/simon_sound/"+name+".mp3");
    audio.play();
}

function animatePress(currentColour){
    $("."+currentColour).addClass("pressed");

    setTimeout(function() {
        $("."+currentColour).removeClass('pressed');
    }, 100);
}


function checkAnswer(currentlevel) {
    if (userClickedPattern[currentlevel]==gamePattern[currentlevel]) {
        console.log("success");
        return true;
    }
    else{
        console.log("wrong");
        return false;
    }
}

function startOver(){
    gameStart=false;
    gamePattern=[];
    userClickedPattern=[];
    level = 0;
}