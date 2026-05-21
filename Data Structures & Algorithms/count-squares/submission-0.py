class CountSquares:

    def __init__(self):
        # Store counts of each point: {(x, y): count}
        self.ptsCount = defaultdict(int)
        self.pts = [] #  a list of all added points (including duplicates)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptsCount[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py-y)!=abs(px-x)) or x==px or y==py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
            
        return res
