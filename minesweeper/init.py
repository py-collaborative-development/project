import minesweeper.gui as gui
import minesweeper.constants as const


def initialize(size_x=const.HEIGHT, size_y=const.WIDTH,
               bomb_number=const.BOMBS):
    field = gui.FieldFrame(gui.root, cols=size_y, rows=size_x)
    gui.TopFrame(gui.root, cols=size_y, field_restart=field.restart)
    gui.root.mainloop()

if __name__ == '__main__':
    initialize()
