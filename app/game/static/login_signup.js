function LoginScreen() {
    document.getElementById("loginOrSignupHolder").innerHTML = `
    <div class="card d-none d-sm-flex text-center align-self-center position-fixed top-50 start-50 translate-middle" style="width: 20rem; height: 20rem;">
        <a class="btn btn-primary position-absolute text-center p-0" style="right: 0; width: 2rem; height: 2rem;" onclick="Destroy()" role="button">
            <img src="/TdA _ Ikonky/SVG/X/X_bile.svg") style="width: 75%; height: 75%;">
        </a>
        <div class="card-body">
            <h1 class="card-title">Log-in</h1>
            <form class="row g-3">
                <div class="col-md-4" style="width: 100%;">
                    <label for="Email" class="form-label">E-mail</label>
                    <input type="email" class="form-control" id="Email" placeholder="valid@address.cz" required>
                </div>
                <div class="col-md-4" style="width: 100%;">
                    <label for="Password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="Password" placeholder="UwU" required>
                </div>
                <div class="col-12">
                    <button class="btn btn-primary" onclick="if(document.getElementById('Email').value != '' && document.getElementById('Password').value != ''){SendData(document.getElementById('Email').value, document.getElementById('Password').value)} else {alert('Das not right. Sumtin is missin')}" type="button">Log-in</button>
                </div>
            </form>
        </div>
    </div>
    <div class="card d-sm-none text-center align-self-center position-fixed top-50 start-50 translate-middle" style="width: 100%; height: 20rem;">
        <a class="btn btn-primary position-absolute text-center p-0" style="right: 0; width: 2rem; height: 2rem;" onclick="Destroy()" role="button">
            <img src="/TdA _ Ikonky/SVG/X/X_bile.svg") style="width: 75%; height: 75%;">
        </a>
        <div class="card-body">
            <h1 class="card-title">Log-in</h1>
            <form class="row g-3">
                <div class="col-md-4" style="width: 100%;">
                    <label for="Email2" class="form-label">E-mail</label>
                    <input type="email" class="form-control" id="Email2" placeholder="valid@address.cz" required>
                </div>
                <div class="col-md-4" style="width: 100%;">
                    <label for="Password2" class="form-label">Password</label>
                    <input type="password" class="form-control" id="Password2" placeholder="UwU" required>
                </div>
                <div class="col-12">
                    <button class="btn btn-primary" onclick="if(document.getElementById('Email2').value != '' && document.getElementById('Password2').value != ''){SendData(document.getElementById('Email2').value, document.getElementById('Password2').value)} else {alert('Das not right. Sumtin is missin')}" type="button">Log-in</button>
                </div>
            </form>
        </div>
    </div>
    `
}

function Destroy() {
    document.getElementById("loginOrSignupHolder").innerHTML = ''
}

function SendData(mail, pass) {
    localStorage.setItem("E-Mail", mail)
    localStorage.setItem("Password", pass)
}