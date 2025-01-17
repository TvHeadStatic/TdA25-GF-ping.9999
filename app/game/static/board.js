let xImage = `<img draggable="false" src="/TdA%20_%20Ikonky/SVG/X/X_modre.svg" class="img-fluid align-self-center" alt="X" style="height: 1.5rem">`
let oImage = `<img draggable="false" src="/TdA%20_%20Ikonky/SVG/O/O_cervene.svg" class="img-fluid align-self-center" alt="O" style="height: 1.65rem">`
let currentPos = [69, 69]
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
    if (getQueryVariable("edit") != 1 && currentPos[0] != 69) {
        currentBoard[currentPos[1]][currentPos[0]] = ""
        document.getElementById(`button${currentPos[0]}x${currentPos[1]}`).innerHTML = ""
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

function board_delete(x, y) {
    if (getQueryVariable("edit") != 1) return
    document.getElementById(`button${x}x${y}`).innerHTML = ""
    currentBoard[y][x] = ""
    if (currentPos[0] == x && currentPos[1] == y) {
        currentPos = [69, 69]
    }
}