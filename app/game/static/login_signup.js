function LoginScreen() {
    document.getElementById("loginOrSignupHolder").style.display = "block"
}

function Destroy() {
    document.getElementById("loginOrSignupHolder").style.display = "none"
}

function login_user(mail, pass) {
    localStorage.setItem("email", mail)
    localStorage.setItem("password", pass)
    window.location.replace("/game")
}

function signout_user() {
    localStorage.removeItem("email")
    localStorage.removeItem("password")
    window.location.replace("/")
}