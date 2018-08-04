
from trek.WebGadget import WebGadget
from trek.Klingon import Klingon
from trek.Game import Game

if __name__ == '__main__':
    print("Simple Star Trek")
    wg = WebGadget("phaser", "1000", Klingon())
    game = Game()
    game.FireWeapon(wg)


