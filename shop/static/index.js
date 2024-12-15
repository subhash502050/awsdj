var searchButton = document.getElementById("search");
var searchData = document.getElementById("searchdata");

searchButton.addEventListener("click",()=>{
    window.location.assign("http://127.0.0.1:8000/uploads/?id="+searchData.value);
});

var description = document.getElementById("description");
var truncate = document.getElementById("truncate");
var load = document.getElementById("load");

var check = true;

load.addEventListener("click",(e)=>{
    if(check){
        description.setAttribute("class","card-text d-block");
        truncate.setAttribute("class","d-none");
        load.textContent = "Hide";
        check = false;
    }else{
        description.setAttribute("class","card-text d-none");
        truncate.setAttribute("class","d-block");
        load.textContent = "Show More";
        check = true;
    }
    
    
    
});

