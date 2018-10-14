import time
from copy import deepcopy


puzzle = [
  "001000000",
  "307605109",
  "050010080",
  "070403010",
  "009000500",
  "010908070",
  "040020060",
  "108506307",
  "000000000"
]

def main():
    start = time.time()

    global puzzle
    for idx, line in enumerate(puzzle):
        puzzle[idx] = list(line)

    solvePuzzle()
    printBoard()
    end = time.time()
    print("\n Finnished in " + str(end - start) + "seconds")


def solvePuzzle():
    global puzzle

    # Prøver først å løse sudokuen ved å fylle ut alle tall med plotNumbers(). Hvis dette ikke fungerer så lagrer vi en
    # "deepcopy" av sudokubrettet, slik at vi kan reversere tilbake brettets tilstand og "gjette" med en ny løsning.
    # Siden vi bruker set når vi konstruerer mulige tall (og dermed får tilfeldig rekkefølge) så vil alle mulige
    # løsninger eventuelt bli prøvd ut.
    #
    #               https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking
    #


    plotNumbers()
    if puzzleSolved():
        return True

    i, j = 0, 0
    for rowIdx, row in enumerate(puzzle):
        for colIdx, col in enumerate(row):
            if col == "0":
                i, j = rowIdx, colIdx

    legalnumbers = getPotentialSolutions(i, j)
    for value in legalnumbers:
        snapshot = deepcopy(puzzle)
        puzzle[i][j] = value
        result = solvePuzzle() #...vil bli true hvis det fungerte i første omgang
        if result == True:
            return True
        else: #...i tilfelle det ikke fungerte..
            puzzle = deepcopy(snapshot) #.. så reverserer vi brettets tilstand og prøver igjen!

    return False

def plotNumbers():
    global puzzle

    # Plotter inn tall i hver eneste ledige celle i sudokuen helt til den ikke lenger klarer å gjøre noen forandringer
    # ved hjelp av getPotentialSolutions() og en loop.

    while True:
        unableToMakeChanges = True
        for i in range(0, 9):
            for j in range(0, 9):
                legalnumbers = getPotentialSolutions(i, j)
                if not legalnumbers:
                    continue
                if len(legalnumbers) == 1:
                    puzzle[i][j] = legalnumbers[0]
                    unableToMakeChanges = False

        if unableToMakeChanges:
            return


def getPotentialSolutions(i, j):
    global puzzle

    # Finner ut hvilke tall som kan plasseres inn i et gitt "koordinat" (i og j) i sudokuen ved å skape et set med tall
    # fra 1-9, og deretter sammenligne det opp mot hva som allerede finnes inn i cellene, radene og 3x3 matrisene som
    # er aktuelle for den gitte cellen.

    # Sjekk om det gitte koordinatet allerede har blitt fyllt ut
    if puzzle[i][j] != "0":
        return False

    # Konstruer et set med tall fra 1 til 9 i tilfeldig rekkefølge. Ved å bruke set istedenfor liste eller objekt
    # kan vi bruke set operasjoner når vi sammenligner settet med hva som allerede finnes på sudokubrettet.
    legalnumbers = {str(n) for n in range(1, 10)}

    # Sjekk alle tallene i radene.
    for val in puzzle[i]:
        legalnumbers -= set(val)

    # Sjekk alle tallene i kolloner.
    for idx in range(0, 9):
        legalnumbers -= set(puzzle[idx][j])

    rowStart = (i // 3) * 3     # Brukes for å "kutte ut" 3x3 grids.
    colStart = (j // 3) * 3     # Brukes for å "kutte ut" 3x3 grids.

    # Sjekk alle tallene i 3x3 matrisene
    grid = puzzle[rowStart:rowStart + 3]
    for idx, row in enumerate(grid):
        grid[idx] = row[colStart:colStart + 3]

    for row in grid:
        for col in row:
            legalnumbers -= set(col)

    return list(legalnumbers)

def printBoard():
    # Printer ut sudokuen vår på en fin måte.
    global puzzle
    for row in puzzle:
        for col in row:
            print(col, end="")
        print("")

def puzzleSolved():
    # Gir oss en boolsk verdi som betegner hvorvidt sudokuen er løst.
    for row in puzzle:
        for col in row:
            if (col == "0"):
                return False
    return True

main()