import { Code, Colors } from "../types.js";
import { getColorValue } from "../themes.js"

const mockState: Code = [
  Colors.RED,
  Colors.GREEN,
  null,
  Colors.BLUE
]

function renderColors(state: Code) {
    const guessElem = document.getElementById("guess0");
    Array.from(guessElem.children)
    .filter(child => {
        return child.classList.contains("pin");
    })
    .forEach((pin, index) => {
        (pin as HTMLElement).style.backgroundColor = getColorValue(state[index]);
    })
}

renderColors(mockState);
