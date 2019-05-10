function ajaxGetRequest(path, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
    callback(this.response);
    }
    };
    request.open("GET", path);
    request.send();
   }

function ajaxPostRequest(path, data, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
   }

function action_on_response(response){
    console.log("The server responded with: " + response);
    }

function call_on_key_pressed(){
    ajaxPostRequest("/some_path", "Button pressed", action_on_response);
   }


function loadTest(){
    ajaxGetRequest("/storage", renderTest);
   }

function sendTest(){
    var moveElement = document.getElementById("action");

    var action = moveElement.value;
    var toSend = JSON.stringify({"action": action});
    ajaxPostRequest("/send", toSend, game.py);
   }

function checkEnter(keyUpEvent){
    if(keyUpEvent.keyCode === 13){
        sendTest();
    }
   }


   function
