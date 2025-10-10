type RGB = string;

type Guess = Array<RGB>;

const mockState: Guess = [
    "rgb(250, 90, 0)",
    "rgb(90, 250, 90)",
    "rgb(90, 90, 250)",
    "transparent"
];

function renderColors(state: Guess) {
    const guessElem = document.getElementById("guess0");
    Array.from(guessElem.children)
    .filter(child => {
        return child.classList.contains("pin");
    })
    .forEach((pin, index) => {
        console.log(pin);
        console.log(index);
        (pin as HTMLElement).style.backgroundColor = state[index];
    })
}

renderColors(mockState);