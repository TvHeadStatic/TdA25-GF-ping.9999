let xImage = `<img draggable="false" src="/TdA%20_%20Ikonky/SVG/X/X_modre.svg" class="img-fluid align-self-center" alt="X" style="height: 1.5rem">`
let oImage = `<img draggable="false" src="/TdA%20_%20Ikonky/SVG/O/O_cervene.svg" class="img-fluid align-self-center" alt="O" style="height: 1.65rem">`
function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
        return pair[1];
        }
    } 
}

if (getQueryVariable("edit") == 1) {
    document.getElementById("guidetext").innerHTML += " | [Right Click] - Remove (edit mode)"
    document.getElementById("submits").innerHTML += "<button type=\"button\" class=\"btn btn-warning\" onClick=\"http_delete()\">Delete</button>"
}

function evaluate_turn() {
    let turn = 0
    for (let yy = 0; yy < currentBoard.length; yy++) {
        for (let xx = 0; xx < currentBoard[yy].length; xx++){
            if (currentBoard[yy][xx] == "X") turn += 1
            if (currentBoard[yy][xx] == "O") turn -= 1
        }
    }
    return turn
}

function check_winstates(i, j) {
    let average = 0
    let priorAverage = 0

    if (j <= 15-5) {
        for (let x = 0; x < 5; x++) {
            average += Number(currentBoard[i][j + x] == "X") - Number(currentBoard[i][j + x] == "O")
        }
    }
    if (Math.abs(priorAverage) < Math.abs(average)) {priorAverage = average}
    average = 0

    if (i <= 5) {
        for (let x = 0; x < 5; x++) {
            average += Number(currentBoard[i + x][j] == "X") - Number(currentBoard[i + x][j] == "O")
        } 
    }
    if (Math.abs(priorAverage) < Math.abs(average)) {priorAverage = average}
    average = 0

    if (i <= 15-5 && j >= 5) {
        for (let x = 0; x < 5; x++) {
            average += Number(currentBoard[i + x][j - x] == "X") - Number(currentBoard[i + x][j - x] == "O")
        }
    }
    if (Math.abs(priorAverage) < Math.abs(average)) {priorAverage = average}
    average = 0

    if (i <= 15-5 && j <= 15-5) {
        for (let x = 0; x < 5; x++) {
            average += Number(currentBoard[i + x][j + x] == "X") - Number(currentBoard[i + x][j + x] == "O")
        }
    }
    if (Math.abs(priorAverage) < Math.abs(average)) {priorAverage = average}
    return priorAverage
}

function board_edit(x, y) {
    if (currentBoard[y][x] != "" && currentBoard[currentPos[1]][currentPos[0]] != "") {
        console.log("nuh uh")
        return
    }
    if (hturn == false) { return }
    hturn = !hturn
    console.log(hturn)
    http_put()
    let currentCoord = `button${currentPos[0]}x${currentPos[1]}`
    if (getQueryVariable("edit") != 1 && currentPos[0] != 69) {
        currentBoard[currentPos[1]][currentPos[0]] = ""
        document.getElementById(currentCoord).innerHTML = ""
    }
    currentPos = [x, y]
    let turn = evaluate_turn()
    if (turn > 0) {
        document.getElementById(`button${x}x${y}`).innerHTML = oImage
        currentBoard[y][x] = "O"
    } else {
        document.getElementById(`button${x}x${y}`).innerHTML = xImage
        currentBoard[y][x] = "X"
    }
    let winner
    for (let i = 0; i < 15; i++) {
        for (let j = 0; j < 15; j++) {
            winner = check_winstates(i, j)
            if (Math.abs(winner) > 4) { break }
        }
        if (Math.abs(winner) > 4) { break }
    }
    console.log(winner)
    if (Math.abs(winner) < 5 && !exists(currentBoard, " ")) {
        document.getElementById("wincont").innerHTML = winDraw
        document.getElementById("wincont2").innerHTML = winDraw
        socket.emit("end_game", {"winner": "Duck", "x": players["X"], "o": players["O"]})
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
    else if (Math.abs(winner) > 4) {
        if (winner > 0) {
            document.getElementById("wincont").innerHTML = winX
            document.getElementById("wincont2").innerHTML = winX
            socket.emit("end_game", {"winner": "x", "x": players["X"], "o": players["O"]})
            console.log("moans")
        } else {
            document.getElementById("wincont").innerHTML = winO
            document.getElementById("wincont2").innerHTML = winO
            socket.emit("end_game", {"winner": "o", "x": players["X"], "o": players["O"]}) 
            console.log("moanz")
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
}

function board_edit_bypass(x, y) {
    if (currentBoard[y][x] != "" && currentBoard[currentPos[1]][currentPos[0]] != "") {
        console.log("nuh uh")
        return
    }
    let currentCoord = `button${currentPos[0]}x${currentPos[1]}`
    if (getQueryVariable("edit") != 1 && currentPos[0] != 69) {
        currentBoard[currentPos[1]][currentPos[0]] = ""
        document.getElementById(currentCoord).innerHTML = ""
    }
    currentPos = [x, y]
    let turn = evaluate_turn()
    if (turn > 0) {
        document.getElementById(`button${x}x${y}`).innerHTML = oImage
        currentBoard[y][x] = "O"
    } else {
        document.getElementById(`button${x}x${y}`).innerHTML = xImage
        currentBoard[y][x] = "X"
    }
}

socket.on("update_turn", (json) => {
    hturn = !hturn
    console.log(hturn)
})

socket.on("update_me", (json) => {
    if (json["id"] != uuid) { return }
    var audio = new Audio('/351518.wav')
    audio.play()
    $(':button').prop('disabled', false)
    document.getElementById("loadingscreen").style.display = "none"
    let gta6 = "[Left Click] - Place"
    if (hturn) {
        document.getElementById("guidetext").innerHTML = "Your Turn Now!<br>" + gta6
    } else {
        document.getElementById("guidetext").innerHTML = "Opponent's Turn Now!<br>" + gta6
    }
    board_edit_bypass(json["coord"][0], json["coord"][1])
    currentPos = [69, 69]
    let winner
    for (let i = 0; i < 15; i++) {
        for (let j = 0; j < 15; j++) {
            winner = check_winstates(i, j)
            if (Math.abs(winner) > 4) { break }
        }
        if (Math.abs(winner) > 4) { break }
    }
    console.log(winner)
    if (Math.abs(winner) < 5 && !exists(currentBoard, " ")) {
        document.getElementById("wincont").innerHTML = winDraw
        document.getElementById("wincont2").innerHTML = winDraw
        document.getElementById("winScreenHolder").style.display = "block"
        return
    }
    else if (Math.abs(winner) > 4) {
        if (winner > 0) {
            document.getElementById("wincont").innerHTML = winX
            document.getElementById("wincont2").innerHTML = winX
        } else {
            document.getElementById("wincont").innerHTML = winO
            document.getElementById("wincont2").innerHTML = winO
        }
        document.getElementById("winScreenHolder").style.display = "block"
        return
    }
})

function board_delete(x, y) {
    if (getQueryVariable("edit") != 1) return
    document.getElementById(`button${x}x${y}`).innerHTML = ""
    currentBoard[y][x] = ""
    if (currentPos[0] == x && currentPos[1] == y) {
        currentPos = [69, 69]
    }
}