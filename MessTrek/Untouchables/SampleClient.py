from MessTrek.Untouchables.webgadget import WebGadget
from MessTrek.Game.klingon import Klingon
from MessTrek.Game.game import Game

if __name__ == '__main__':
    print("Simple Star Trek")
    wg = WebGadget("phaser", "1000", Klingon())
    game = Game()
    game.fire_weapon(wg)
