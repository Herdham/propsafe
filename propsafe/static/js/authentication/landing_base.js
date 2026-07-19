const accordion_btn = document.querySelectorAll(".section_card h4")

if (accordion_btn) {
    accordion_btn.forEach(btn => {
        const parent = btn.closest(".section_card")
        const faqBtn = parent.querySelector(".section_card h4")
        const faqDetail = parent.querySelector(".section_card p")
    
        faqBtn.addEventListener("click", (e) => {
            if (faqDetail.classList.contains("show")) {
                faqDetail.classList.remove("show")
            }else{
                faqDetail.classList.add("show")
            }
        })
    })
}

const loginBtn = document.getElementById("loginBtn")
const loginPopup = document.querySelector(".login_popup")
const signup_btn = document.getElementById("signup_btn")
const login_btn = document.getElementById("login_btn")
const signupBtn = document.getElementById("signupBtn")
const getStartedBtn = document.getElementById("getStartedBtn")
const signupPopup = document.querySelector(".signup_popup")

if (loginBtn) {
    loginBtn.addEventListener("click", (e) => {
        if(loginPopup.classList.contains("show")){
            loginPopup.classList.remove("show")
            document.body.style.overflow = ""
        }else{
            loginPopup.classList.add("show")
            document.body.style.overflow = "hidden"
        }
    })
}

if (signup_btn) {
    signup_btn.addEventListener("click", (e) => {
        e.preventDefault()
        if(signupPopup.classList.contains("show")){
            signupPopup.classList.remove("show")
            document.body.style.overflow = ""
        }else{
            signupPopup.classList.add("show")
            loginPopup.classList.remove("show")
            document.body.style.overflow = "hidden"
        }
    })
}

if (login_btn) {
    login_btn.addEventListener("click", (e) => {
        e.preventDefault()
        if (loginPopup.classList.contains("show")) {
            loginPopup.classList.remove("show")
            document.body.style.overflow = ""
        } else {
            loginPopup.classList.add("show")
            signupPopup.classList.remove("show")
            document.body.style.overflow = "hidden"
        }
    })
}


if (signupBtn) {
    signupBtn.addEventListener("click", (e) => {
        if(signupPopup.classList.contains("show")){
            signupPopup.classList.remove("show")
            document.body.style.overflow = ""
        }else{
            signupPopup.classList.add("show")
            document.body.style.overflow = "hidden"
        }
    })
}

if (getStartedBtn) {
    getStartedBtn.addEventListener("click", (e) => {
        if(signupPopup.classList.contains("show")){
            signupPopup.classList.remove("show")
            document.body.style.overflow = ""
        }else{
            signupPopup.classList.add("show")
            document.body.style.overflow = "hidden"
        }
    })
}

const loginClose = document.querySelector("#loginclosebtn svg")
if (loginClose) {
    loginClose.addEventListener("click", (e) => {
        if(loginPopup.classList.contains("show")){
            loginPopup.classList.remove("show")
            document.body.style.overflow = ""
        }else{
            loginPopup.classList.add("show")
            document.body.style.overflow = "hidden"
        }
    })
}


const signupClose = document.querySelector("#signupclosebtn svg")
if (signupClose) {
    signupClose.addEventListener("click", (e) => {
        if(signupPopup.classList.contains("show")){
            signupPopup.classList.remove("show")
            document.body.style.overflow = ""
        }else{
            signupPopup.classList.add("show")
            document.body.style.overflow = "hidden"
        }
    })
}

// const signupForm = document.getElementById("signupForm")
// signupForm.addEventListener("submit", (e) => {
//     e.preventDefault()
//     const form = new FormData(signupForm)
    
//     fetch("", {
//         method: "POST",
//         body: form,
//         headers: {
//             "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
//         }
//     })
//     .then(res => res.json())
//     .then(body => {
//         const email_error = document.getElementById("emailerror")
//         const username_error = document.getElementById("usernameerror")
//         if (body.form.email) {
//             email_error.style.display = "block"
//             email_error.innerText = body.form.email[0].message
//         }
//         if (body.form.username) {
//             username_error.style.display = "block"
//             username_error.innerText = body.form.username[0].message
//         }
//         alert(body.success)
//     })
//     signupForm.reset()
// })


const login_checkbox = document.querySelector(".login_checkbox #checkbox")
const login_password = document.getElementById("login_password")
if (login_checkbox) { 
    login_checkbox.addEventListener("click", (e) => {
        if (login_checkbox.checked) {
            login_password.type = "text"
        }else{
            login_password.type = "password"
        }
    })
}

const signup_checkbox = document.querySelector(".signup_checkbox #checkbox")
const signup_password1 = document.getElementById("signup_password1")
const signup_password2 = document.getElementById("signup_password2")

if (signup_checkbox) { 
    signup_checkbox.addEventListener("click", (e) => {
        if (signup_checkbox.checked) {
            signup_password1.type = "text"
            signup_password2.type = "text"
        }else{
            signup_password1.type = "password"
            signup_password2.type = "password"
        }
    })
}