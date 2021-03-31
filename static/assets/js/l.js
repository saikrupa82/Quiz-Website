const login = document.querySelector("#Login")
const signup = document.querySelector("#Signup")
const forgot = document.querySelector("#ForgotPassword")
const verify = document.querySelector("#Verification")
const newpass = document.querySelector("#newpass")
const success = document.querySelector("#success")

let sb = document.querySelector("#signup-btn")
let lb = document.querySelectorAll(".login-btn")
let fb = document.querySelector("#forgot-btn")
let rb = document.querySelector("#reset-btn")
let vb = document.querySelector("#verify-btn")
let db = document.querySelector("#done-btn")
let sections = [login, signup, forgot, verify, newpass, success]

const section_change = (button, 
                        sections,  
                        needed, 
                        classname 
                        ) => {
                        button.addEventListener("click", function(){
                            sections.forEach(element => {
                                if (element === needed){
                                    element.classList.remove(classname);
                                }
                                else{
                                    element.classList.add(classname);
                                }                                    
                            });
                        })
}

section_change(sb, sections, signup, "display_none");
section_change(lb[0], sections, login, "display_none");
section_change(fb, sections, forgot, "display_none");
section_change(rb, sections, verify, "display_none");
section_change(lb[1], sections, login, "display_none");
section_change(vb, sections, newpass, "display_none");


db.addEventListener("click", function(){
    success.classList.remove('display_none');
})

lb[2].addEventListener("click", function(){
    success.classList.add("display_none");
    newpass.classList.add("display_none");
    login.classList.remove("display_none");

});
