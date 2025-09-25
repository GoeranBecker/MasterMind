from enum import Enum
from itertools import chain

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    
    
class Hit(Enum):
    PERFECT = 1
    IMPERFECT = 2
    MISS = 3
    

PRINT_PAD = 2 + max([len(word) for word in chain([color.name for color in Color],
                                             [hit.name for hit in Hit])])


class Code(list[Color]):
    def __init__(self, colors:list[Color]):
        for color in colors: self.append(color)


    def __str__(self) -> str:
        result = ""
        for color in self:
            result += f"{color.name:^{PRINT_PAD}}|" 
        return result[:-2]
        

class Answer(list[Hit]):
    def __init__(self, hits:list[Hit]):
        for hit in hits: self.append(hit)
      

    def __str__(self) -> str:
        result = ""
        for hit in self:
            result += f"{hit.name:^{PRINT_PAD}}|" 
        return result[:-2]

   
class GameState:
    def __init__(self):
        self.number_of_pins:int = 4
        self.color_set:list[Color] = [Color.BLUE, Color.GREEN, Color.RED, Color.YELLOW] 
        self.code:Code = Code([Color(1), Color(2), Color(3), Color(4)])
        self.codemaker_is_human = False
        self.codebreaker_is_human = True
        
        self.number_of_rounds:int = 10
        self.rounds:list[Round] = []
        
    def play_round(self):
        # should be next_move() and decide next move based on gamestate
        guess = None
        if self.codebreaker_is_human:
            guess = self.get_guess()
        else:
            guess = self.calc_guess()
        
        answer = None
        if self.codemaker_is_human:
            answer = self.get_answer()
        else:
            answer = self.calc_answer(guess, self.code)
        
        self.rounds.append(Round(guess, answer))
        # check if guess is correct/ answer is all pins perfect
        
            
    def calc_guess(self) -> Code: 
        pass
    
    def get_guess(self) -> Code:
        cur_code = []
        for i in range(self.number_of_pins):
            cur_code.append(Color(int(input("enter color: "))))
        return Code(cur_code)
            
    
    def get_answer(self) -> list[Hit]:
        pass
    
    def calc_answer(self, guess:Code, code:Code) -> list[Hit]:
        hits = []
        c = code.copy()
        for i in range(self.number_of_pins):
            if guess[i] == code[i]:
                hits.append(Hit.PERFECT)
        imperfect_hits = 0
        for pin in guess:
            if pin in c:
                imperfect_hits += 1
                c.remove(pin)
        for i in range(imperfect_hits-len(hits)):
            hits.append(Hit.IMPERFECT)
        for i in range(self.number_of_pins-len(hits)):
            hits.append(Hit.MISS)

        return Answer(hits)
            

class Round:
    def __init__(self, guess:Code, answer:Answer):
        self.guess = guess 
        self.answer = answer 


def init_game() -> GameState:
    pass

g = GameState()
g.play_round()
guess = g.rounds[0].guess
print("code  :", g.code)
print("guess :", guess)
print("answer:", g.rounds[0].answer)
print(g.code == guess)      
