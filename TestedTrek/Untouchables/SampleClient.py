
from TestedTrek.Untouchables.webgadget import WebGadget
from TestedTrek.Game.klingon import Klingon
from TestedTrek.Game.game import Game

if __name__ == '__main__':
    print("Simple Star Trek")
    wg = WebGadget("phaser", "1000", Klingon())
    game = Game()
    game.FireWeapon(wg)


