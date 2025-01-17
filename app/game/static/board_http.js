let winX = `
<h1 class="card-title" id="wintext1">X Won!</h1>
<img
    draggable="false"
    src="/TdA%20_%20Ikonky/SVG/X/X_modre.svg"
    class="img-fluid align-self-center"
    alt="X"
    style="height: 4rem"
/>
<p class="text-center">
    <br>
    <a
        name=""
        id=""
        class="btn btn-primary"
        href="/game"
        role="button"
        ><- Go Back</a
    >
</p>`
let winO = `
<h1 class="card-title" id="wintext1">O Won!</h1>
<img
    draggable="false"
    src="/TdA%20_%20Ikonky/SVG/O/O_cervene.svg"
    class="img-fluid align-self-center"
    alt="X"
    style="height: 4rem"
/>
<p class="text-center">
    <br>
    <a
        name=""
        id=""
        class="btn btn-primary"
        href="/game"
        role="button"
        ><- Go Back</a
    >
</p>`
function http_delete() {
    console.log(uuid)
    fetch(`/api/gateway/${uuid}`, {
        method: "delete",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        }
    })
    .then( (response) => {
        window.location.replace("/game")
    })
}

function http_put() {
    let winner
    for (let i = 0; i < 15; i++) {
        for (let j = 0; j < 15; j++) {
            winner = check_winstates(i, j)
            if (Math.abs(winner) > 4) { break }
        }
        if (Math.abs(winner) > 4) { break }
    }
    console.log(winner)
    if (Math.abs(winner) > 4) {
        fetch(`/api/gateway/${uuid}`, {
            method: "delete",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("token")}`
            }
        })
        .then( (response) => {
            if (winner > 0) {
                document.getElementById("wincont").innerHTML = winX
                document.getElementById("wincont2").innerHTML = winX
            } else {
                document.getElementById("wincont").innerHTML = winO
                document.getElementById("wincont2").innerHTML = winO
            }
            document.getElementById("submitbtn").disabled = true
            document.getElementById("backbtn").disabled = true
            document.getElementById("winScreenHolder").style.display = "block"
        })
        return
    }
    fetch(`/api/gateway/${uuid}`, {
        method: "put",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        },
        body: JSON.stringify({
            'name': gname,
            'difficulty': diff,
            'board': currentBoard
        })
    })
    .then( (response) => {
        if (getQueryVariable("edit") == 1) {
            window.location.replace(`/game/${uuid}?edit=1`)
        }
        window.location.replace(`/game/${uuid}`)
        return
    })
}

function http_post() {
    if (document.getElementById("titleofgame").value == "" || document.getElementById("titleofgame").value == " ") {
        document.getElementById("badcodebad").innerHTML = "Name is empty"
        return
    }
    fetch(`/api/gateway`, {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        },
        body: JSON.stringify({
            'name': document.getElementById("titleofgame").value,
            'difficulty': document.getElementById("difficulty").value,
            'board': currentBoard
        })
    })
    .then(r =>  r.json().then(data => ({status: r.status, body: data})))
    .then( (response) => {
        if (response.status != 201) {
            document.getElementById("badcodebad").innerHTML = response.body["reason"]
        } else {
            window.location.replace(`/game/${response.body["uuid"]}`)
        }
    })
}