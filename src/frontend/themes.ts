import { Colors } from "./types.js"

type Theme = Record<Colors, string> 

const defaultTheme: Theme = {
  [Colors.RED]:  "rgb(230, 50, 10)",
  [Colors.GREEN]: "rgb(90, 250, 90)",
  [Colors.BLUE]: "rgb(90, 90, 250)",
  [Colors.YELLOW]: "rgb(237, 231, 62)"
}

let currentTheme: Theme = defaultTheme

function getColorValue(color: Colors): string {
  if (color == null) { return "transparent" }
  return currentTheme[color]
}

export { getColorValue }
