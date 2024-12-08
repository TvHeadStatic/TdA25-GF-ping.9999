function LoginScreen() {
    document.getElementById("loginOrSignupHolder").style.display = "block"
}

function Destroy() {
    document.getElementById("loginOrSignupHolder").style.display = "none"
}

function SendData(mail, pass) {
    localStorage.setItem("E-Mail", mail)
    localStorage.setItem("Password", pass)
    window.location.replace("/game")
}