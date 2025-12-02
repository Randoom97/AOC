from input import p1Pos, p2Pos

rollCount = 0

cache = {}
def round(player: bool, p1Score: int, p2Score: int, p1Pos: int, p2Pos: int):
    cacheIndex = str(player)+":"+str(p1Score)+":"+str(p2Score)+":"+str(p1Pos)+":"+str(p2Pos)
    if cacheIndex in cache:
        return cache[cacheIndex]
    p1WinCount = 0
    p2WinCount = 0
    if player:
        # player 1
        for roll1 in range(1, 4):
            for roll2 in range(1, 4):
                for roll3 in range(1, 4):
                    newP1Pos = (p1Pos + roll1 + roll2 + roll3 - 1) % 10 + 1
                    newP1Score = p1Score + newP1Pos
                    if newP1Score >= 21:
                        p1WinCount += 1
                        continue
                    (p1SubWins, p2SubWins) = round(False, newP1Score, p2Score, newP1Pos, p2Pos)
                    p1WinCount += p1SubWins
                    p2WinCount += p2SubWins
        cache[cacheIndex] = (p1WinCount, p2WinCount)
        return (p1WinCount, p2WinCount)
    else:
        # player 2
        for roll1 in range(1, 4):
            for roll2 in range(1, 4):
                for roll3 in range(1, 4):
                    newP2Pos = (p2Pos + roll1 + roll2 + roll3 - 1) % 10 + 1
                    newP2Score = p2Score + newP2Pos
                    if newP2Score >= 21:
                        p2WinCount += 1
                        continue
                    (p1SubWins, p2SubWins) = round(True, p1Score, newP2Score, p1Pos, newP2Pos)
                    p1WinCount += p1SubWins
                    p2WinCount += p2SubWins
        cache[cacheIndex] = (p1WinCount, p2WinCount)
        return (p1WinCount, p2WinCount)
        
(p1Wins, p2Wins) = round(True, 0, 0, p1Pos, p2Pos)
if p1Wins > p2Wins:
    print(p1Wins)
else:
    print(p2Wins)