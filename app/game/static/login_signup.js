function LoginScreen() {
    document.getElementById("loadingscreen").style.display = "flex"
    $(':button').prop('disabled', true)
    fetch("/api/v1/users/login", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
    },
        body: JSON.stringify({
            email: "",
            password: ""
        })
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        document.getElementById("loadingscreen").style.display = "none"
        $(':button').prop('disabled', false)
        if (response.body["response"] != "session already active, you're good to go") {
            document.getElementById("loginHolder").style.display = "block"
        } else {
            localStorage.setItem("token", response.body["token"])
            return window.location.replace("/game")
        }
    })
}

function SignupScreen() {
    document.getElementById("signupHolder").style.display = "block"
}

function Destroy() {
    document.getElementById("loginHolder").style.display = "none"
    document.getElementById("signupHolder").style.display = "none"
}

function login_user(mail, pass) {
    document.getElementById("loadingscreen").style.display = "flex"
    $(':button').prop('disabled', true)
    fetch("/api/v1/users/login", {
            method: "post",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
            body: JSON.stringify({
                email: String(mail),
                password: String(pass)
        })
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        if (response.status != 201) {
            document.getElementById("loadingscreen").style.display = "none"
            $(':button').prop('disabled', false)
            document.getElementsByClassName("loginwarn")[0].innerHTML = response.body["reason"]
            document.getElementsByClassName("loginwarn")[1].innerHTML = response.body["reason"]
            document.getElementsByClassName("loginwarn")[0].style.display = "block"
            document.getElementsByClassName("loginwarn")[1].style.display = "block"
        } else {
            localStorage.setItem("token", response.body["token"])
            window.location.replace("/game")
        }
    })
}

function signup_user(name, mail, pass) {
    document.getElementById("loadingscreen").style.display = "flex"
    $(':button').prop('disabled', true)
    fetch("/api/v1/users", {
            method: "post",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
        },
            body: JSON.stringify({
                username: String(name),
                email: String(mail),
                password: String(pass)
        })
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        document.getElementById("loadingscreen").style.display = "none"
        $(':button').prop('disabled', false)
        if (response.status != 201) {
            document.getElementsByClassName("signupwarn")[0].innerHTML = response.body["reason"]
            document.getElementsByClassName("signupwarn")[1].innerHTML = response.body["reason"]
            document.getElementsByClassName("signupwarn")[0].style.display = "block"
            document.getElementsByClassName("signupwarn")[1].style.display = "block"
        } else {
            localStorage.setItem("token", response.body["token"])
            window.location.replace("/game")
        }
    })
}

function signout_user() {
    document.getElementById("loadingscreen").style.display = "flex"
    $(':button').prop('disabled', true)
    fetch("/api/v1/users/signout", {
        method: "get",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        if (response.status == 201) {
            localStorage.removeItem("token")
            window.location.replace("/")
        }
    })
}