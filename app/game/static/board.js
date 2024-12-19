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

if (getQueryVariable("edit") == 1) document.getElementById("guidetext").innerHTML += " | [Right Click] - Remove (edit mode)"

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

function board_edit(x, y) {
    if (currentBoard[y][x] != "") {
        console.log("nuh uh")
        return
    }
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
}