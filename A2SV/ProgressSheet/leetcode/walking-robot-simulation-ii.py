class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = (0, 0)
        self.face = (1, 0)
        self.perimeter = 2*(self.width + self.height - 2)
        self.faceDirection = {
            (1, 0) : (0, 1),
            (0, 1) : (-1, 0),
            (-1, 0) : (0, -1),
            (0, -1) : (1, 0),
        }

    def step(self, num: int) -> None:
        tot = num // self.perimeter
        num -= (tot-1)*self.perimeter

        while num > 0:
            moveX, moveY = self.face[0], self.face[1]
            newX, newY = self.pos
            newX, newY = newX + moveX, newY + moveY
            
            if newX >= self.width or newX < 0:
                self.face = self.faceDirection[self.face]
                continue
            
            if newY >= self.height or newY < 0:
                self.face = self.faceDirection[self.face]
                continue
            
            self.pos = newX, newY
            num -= 1

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        if self.face == (0, 1):
            return "North"
        if self.face == (0, -1):
            return "South"
        if self.face == (1, 0):
            return "East"
        if self.face == (-1, 0):
            return "West"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()