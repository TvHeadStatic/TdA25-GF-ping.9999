function LoginScreen() {
    if (localStorage.getItem("username") !== null) {
        return window.location.replace("/game")
    }
    document.getElementById("loginHolder").style.display = "block"
}

function SignupScreen() {
    document.getElementById("signupHolder").style.display = "block"
}

function Destroy() {
    document.getElementById("loginHolder").style.display = "none"
    document.getElementById("signupHolder").style.display = "none"
}

function login_user(mail, pass) {
    fetch("/api/users/login", {
            method: "post",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
            body: JSON.stringify({
                address: String(mail),
                password: String(pass)
        })
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        if (response.status != 201) {
            document.getElementsByClassName("loginwarn")[0].innerHTML = response.body["reason"]
            document.getElementsByClassName("loginwarn")[1].innerHTML = response.body["reason"]
            document.getElementsByClassName("loginwarn")[0].style.display = "block"
            document.getElementsByClassName("loginwarn")[1].style.display = "block"
        } else {
            localStorage.setItem("username", response.body["username"])
            localStorage.setItem("email", mail)
            localStorage.setItem("password", pass)
            window.location.replace("/game")
        }
    })
}

function signup_user(name, mail, pass) {
    fetch("/api/users/register", {
            method: "post",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
            body: JSON.stringify({
                username: String(name),
                address: String(mail),
                password: String(pass)
        })
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        if (response.status != 201) {
            document.getElementsByClassName("signupwarn")[0].innerHTML = response.body["reason"]
            document.getElementsByClassName("signupwarn")[1].innerHTML = response.body["reason"]
            document.getElementsByClassName("signupwarn")[0].style.display = "block"
            document.getElementsByClassName("signupwarn")[1].style.display = "block"
        } else {
            localStorage.setItem("username", response.body["username"])
            localStorage.setItem("email", mail)
            localStorage.setItem("password", pass)
            window.location.replace("/game")
        }
    })
}

function signout_user() {
    localStorage.removeItem("username")
    localStorage.removeItem("email")
    localStorage.removeItem("password")
    window.location.replace("/")
}