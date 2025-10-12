enum Colors {
  RED,
  BLUE,
  GREEN,
  YELLOW
}

enum Hit {
  PERFECT,
  IMPERFECT,
  MISS
}

type Code = Array<Colors>
type Answer = Array<Hit>

type Round = {
  guess: Code,
  answer: Answer
}

type GameState = {
  number_of_pins: number,
  color_set: Array<Colors>,
  code: Code,
  codemaker_is_human: boolean,
  codebreaker_is_human: boolean,
  number_of_rounds: number,
  rounds: Array<Round>
}

export { Colors, Code, Answer, Round, GameState }
