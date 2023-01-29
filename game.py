class Player:
    number = []
    def __init__(self) -> None:
        self.number = [1, 1]
    def add(self, other, selfpos, otherpos):
        if selfpos > len(self.number) or otherpos > len(other.number):
            raise IndexError
        else:
            self.number[selfpos] = (self.number[selfpos] + other.number[otherpos]) % 10
            if self.number[selfpos] == 0:
                del self.number[selfpos]
    def isEmpty(self):
        return len(self.number) == 0

def display(p1: Player, p2: Player) -> None:
    print('---- Current State ----')
    print('player 1: ' + str(p1.number))
    print('player 2: ' + str(p2.number))

def pvp() -> int:
    '''
    PVP game mode, return the winner (1 or 2).
    '''
    p1 = Player()
    p2 = Player()
    current_player = 0
    while not (p1.isEmpty() or p2.isEmpty()):
        display(p1, p2)
        s = input('Input (i, j) seperated with space, which means in player {}\'s turn, he add the j-th number of player {} to the i-th number of him: (index start with 0)'.format(current_player + 1, 2 - current_player))
        i, j = s.split(sep=' ')
        i = int(i)
        j = int(j)
        try:
            if current_player == 0:
                p1.add(p2, i, j)
            else:
                p2.add(p1, i, j)
            current_player = 1 - current_player
        except:
            print('Index error, please input again!')
            
    print('Player {} won!'.format(2 - current_player))
    return 1 - current_player
    

        


def main():
    pvp()

if __name__ == '__main__':
    main()