var login = document.querySelector("#Login")
var sb = document.querySelector("#signup-btn")
var signup = document.querySelector("#Signup")
var lb = document.querySelector("#login-btn")

sb.addEventListener("click", function(){
   login.classList.add("login-form");
    signup.classList.remove("signup-form");
})

lb.addEventListener("click", function(){
    login.classList.remove("login-form");
     signup.classList.add("signup-form");
})
