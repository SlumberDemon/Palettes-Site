let colorCards = document.getElementsByClassName("color-card");
let downloadB = document.getElementById("download");
let apiB = document.getElementById("api");
let srcB = document.getElementById("src");

// Color Card

document.addEventListener("DOMContentLoaded", () => {
    for (let card of colorCards) {
        card.style.background=card.id;
    }
})

for (let card of colorCards) {
    card.addEventListener("click", () => {
        navigator.clipboard.writeText(card.id);
        card.innerHTML = "Copied";
        setTimeout(() => {
            card.innerHTML = card.id
        }, 250)
    })
}

function GenerateHex(){
    chars = '0123456789abcdef'
    var c1 = ""
    for(i = 0;i < 6;i++){
        c1 = c1 + chars[Math.floor(Math.random()*16)]
    }
    return '#'+c1
}
function RefreshPalette(){
    palette = document.getElementById("PrimaryPalette").getElementsByTagName('div')
    for (let i = 0;i<palette.length;i++){
        elem = palette[i]
        ColorHex = GenerateHex()
        elem.id = ColorHex
        elem.style.background = ColorHex
        elem.innerHTML = ColorHex
    }
}

// Buttons

downloadB.addEventListener("click", () => {
    window.location.href = `/`
})

apiB.addEventListener("click", () => {
    window.location.href = `/docs`
})

srcB.addEventListener("click", () => {
    window.location.href = `/github`
})
