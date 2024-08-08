
  let url =document.getElementById("loggy");
  let urls=document.getElementById("sign");
  let urlss=document.getElementById("autos");
  let urlsss=document.getElementById("man");
  let urlssss=document.getElementById("ab");
  urls.onclick=function() {
    if (url.style.visibility!="visible") {
      url.style.visibility="visible";
      urlss.style.position="static";
      urlsss.style.position="static";
    } else {
      url.style.visibility="hidden";
      urlss.style.position="absolute";
      urlsss.style.position="static";
    }
  }
 let orb=document.getElementById("opens")
 let orbs=document.getElementById("hide")
 
 orb.onclick=function() {
    if(orbs.style.visibility!="visible") {
        orbs.style.visibility="visible";
       
        
    } else {
        orbs.style.visibility="hidden";
    }
 }
 let vibe=document.getElementById("hide")
 let vibes=document.getElementById("into-button")
 vibes.onclick=function() {
    if(vibe.style.visibility=="visible") {
            vibe.style.visibility="hidden";
            vibe.style.transition="all 0.5s ease";
            
        } else {
            vibe.style.visibility=="visible";
        }
 }
 var counter=1;
 setInterval(function(){
  document.getElementById("radio"+ counter).checked=true;
  counter++;
  if(counter>5){
    counter=1;
  }
 },4000);
 let wide=document.getElementById("ab");
 let wides=document.getElementById("loggy");
 wide.onclick=function() {
  if(wides.style.visibility=="visible") {
    wides.style.visibility="hidden";
    wides.style.transition="all 0.5s ease";
  }else {
    wides.style.visibility="visible";
  }
 }
let bad=document.getElementById("place");
let good=document.getElementById("into-button");
let goods=document.getElementById("location");
function show(){
  if (goods.style.top=="-100vh") {
    goods.style.top="0px";
    goods.style.transition="all 1s ease";
  }else {
    goods.style.top="-100vh";
    goods.style.transition="all 1s ease";
  }
}
function abi(){
  let oauth2Endpoint="https://accounts.google.com/o/oauth2/v2/auth"
  let form=document.createElement('form')
  form.setAttribute('method','GET')
  form.setAttribute('action',oauth2Endpoint)

  let params={
    "client_id":"49056160029-4otijq03bntca9jo932vrj3va91hslk5.apps.googleusercontent.com",
    "redirect_uri":"http://127.0.0.1:8000/signin/",
    "response_type":"token",
    "scope":"https://www.googleapis.com/auth/userinfo.profile",
    "include_granted_scopes":'true',
    'state':'pass-through-value'
  }
  for(var p in params){
    let input =document.createElement('input')
    input.setAttribute('type', 'hidden')
    input.setAttribute('name',p)
    input.setAttribute('value',params[p])
    form.appendChild(input)
  }
  document.body.appendChild(form)
  form.submit()
}
//getting all required item
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = document.querySelector(".autocom-box");


//if user press any key an release

inputBox.onkeyup = (e)=>{
    let userData = e.target.value; //user entered data
    let emptyArray = [];
    if(userData){
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user char tolowercase and return only those word/sentence which are starts with user entered word
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
            
        });
        emptyArray = emptyArray.map((data)=>{
            return data = '<li>'+ data +'</li>';

        });
        console.log(emptyArray);
        searchWrapper.classList.add("active"); //show auto complete box
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for(let i = 0; i < allList.length; i++){
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)");
        }
    }else{
        searchWrapper.classList.remove("active"); //hide auto complete box
    }
    
}

function select(element){
    let selectUserData = element.textContent;
    inputBox.value = selectUserData; //passing the user selected list item data in textfield
    searchWrapper.classList.remove("active"); //hide auto complete box
}

function showSuggestions(list){
    let listData;
    if(!list.length){
        userValue = inputBox.value;
        listData = '<li>'+ userValue +'</li>';
    }else{
        listData=list.join('');
    }
    suggBox.innerHTML = listData;
}


let suggestions=[
  "python",
  "react",
  "java",
  "javascript",
  "html",
  "css",
  "cadbury",
  "leo",
  "maamannan",
  "pichaikaran-2",
  "what-if?",
  "118",
  "thunivu",
  "araam",
  "bloody daddy",
];