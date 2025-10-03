# Master Mind

## Terminologie

- The two players are called Codemaker and Codebreaker.
- game:
    - game ends after x rounds or when guess is eqaul to code
- round:
    is a single guess with its respective response 
- code
    - a given color combination of pins which needs to be cracked
- guess:
    - a given color combination by the Codebreaker
- answer:
    - marks the perfect and imperfect pins of a guess

- perfect:
    - a pin with the right color in the right place
- imperfect:
    - a pin with the right color but in the wrong place
- pin:
    - a single pin inside of a code
- slot
    - the slot into which a pin can be placed in
- color
    - each pin has a color




## Was wir machen wollen

- Variable Menge an:
    - Farben
    - Slots
    - Anzahl an Runden
- Constraints fuer die moeglichen unterschiedlichen Kombinationen
- (Zusatz-Regeln wie z.B. Position der Antwort-Pins)
- Solver

- Single und Multiplayer, weil Multiplayer lernen ist witzig

## Komponenten

### Frontend

#### GUI
- as a flow we want to have:
   - -> menu -> game

- dynamically loading each guess as well as its response
- stick with vanilla css

### Backend

- For the backend we use python and flask
- sqlite as database

#### Spiel-Logik

### Codemaker

- Erstellt zu Beginn des Spiels einen Code
- Prueft nach jeder Runde, ob und wie viele der pins im guess korrekt sind
- wins if the codebreaker is not able to guess the code in x rounds

### Codebreaker

- creates a guess each round to try to crack the code
- wins if the guess is correct (i.E. equal to the code)

#### Multiplayer

- Codemaker darf Fehler machen beim auswerten (Maybe toggle)



### kp digga
    server: POST /update-gamestate
            Request-payload: GameState
                -handler: prüfe ob gamestate ok -> ja: neuer Gamestate an alle beteiligten clients
                                                    nein: error an sender

            Response-payload: GameState
    
    oder

    server: POST /update-answer
        Request-payload: Answer
            -handler: prüfe ob gamestate update valide -> ja: neuer Gamestate an alle beteiligten clients
                                                            nein: error an sender

        Response-payload: GameState
    
     POST /update-guess
        Request-payload: Guess
            -handler: prüfe ob gamestate ok -> ja: neuer Gamestate an alle beteiligten clients
                                                nein: error an sender

        Response-payload: GameState


