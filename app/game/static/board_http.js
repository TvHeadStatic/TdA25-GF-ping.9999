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
let gameOver = `
<h1 class="card-title" id="wintext1">Opponent left</h1>
<p class="text-center">:/</p>
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

socket.on('connect', () => {
    socket.emit("join_game", { "gameuuid": uuid , "playeruuid": userData["uuid"]})
    console.log('a user connected')
})

socket.on("join_gamed", (json) => {
    hturn = json["result"]
    console.log(":3")
})

socket.on("leave_game", (json) => {
    if (players["X"] != json["uuid"] && players["O"] != json["uuid"]) { return }
    console.log(":(")
    document.getElementById("wincont").innerHTML = gameOver
    document.getElementById("wincont2").innerHTML = gameOver
    document.getElementById("winScreenHolder").style.display = "block"
    fetch(`/api/gateway/${uuid}`, {
        method: "delete",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem("token")}`
        }
    })
    .then( (response) => {
        socket.emit("update_game", { "coord": currentPos, "id": uuid })
        currentPos = [69, 69]
        return
    })
    console.log(":(")
})

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
        if (winner > 0) {
            document.getElementById("wincont").innerHTML = winX
            document.getElementById("wincont2").innerHTML = winX
        } else {
            document.getElementById("wincont").innerHTML = winO
            document.getElementById("wincont2").innerHTML = winO
        }
        document.getElementById("winScreenHolder").style.display = "block"
        fetch(`/api/gateway/${uuid}`, {
            method: "delete",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("token")}`
            }
        })
        .then( (response) => {
            socket.emit("update_game", { "coord": currentPos, "id": uuid })
            currentPos = [69, 69]
            return
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
        socket.emit("update_game", { "coord": currentPos, "id": uuid })
        currentPos = [69, 69]
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