document.body.innerHTML += "<div id=\"xocontainer\" style=\"position: fixed; z-index: -99\"></div>"
let timeOutTime = 750
const myTimeout = setTimeout(coolEffect, timeOutTime);
function coolEffect() {
    let x = Math.round(Math.floor(Math.random() * window.screen.width)/32)*32-16;
    let y = Math.round(Math.floor(Math.random() * window.screen.height)/32)*32-16;
    if (timeOutTime == 750) {
        timeOutTime = 100
        document.getElementById("xocontainer").innerHTML += `
        <img
        draggable="false"
        src="/TdA _ Ikonky/SVG/X/X_modre.svg"
        class="img-fluid align-self-center xmark"
        style="position: fixed; top: ${y}px; left: ${x}px; height: 1.5rem; aspect-ratio: 1/ 1; width: 2.5em;"
        alt="X"
        />`
        try{ document.getElementsByClassName("xmark")[Math.floor(Math.random() * 5)+1].remove() } catch(e) {}
    } else {
        timeOutTime = 750
        document.getElementById("xocontainer").innerHTML += `
        <img
        draggable="false"
        src="/TdA _ Ikonky/SVG/O/O_cervene.svg"
        class="img-fluid align-self-center omark"
        style="position: fixed; top: ${y}px; left: ${x}px; height: 1.65rem; aspect-ratio: 1/ 1; width: 2.5em; z-index: -99"
        alt="O"
        />`
        try { document.getElementsByClassName("omark")[Math.floor(Math.random() * 5)+1].remove() } catch(e) {}
    }
    setTimeout(coolEffect, timeOutTime)
}