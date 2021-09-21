import win32gui
import win32con
import win32api
import pygame


def update_window_settings():
    hwnd = pygame.display.get_wm_info()['window']

    #  Styles: https://github.com/SublimeText/Pywin32/blob/master/lib/x32/win32/lib/win32con.py
    #  https://stackoverflow.com/questions/2398746/removing-window-border
    # I couldn't get NOFRAME to work but it was because of a silly mistake. Now I don't need this anymore.
    #style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    #style += (win32con.WS_CAPTION | win32con.WS_THICKFRAME | win32con.WS_MINIMIZEBOX | win32con.WS_MAXIMIZEBOX)
    #win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    ex_style += (win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)

    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)
    # https://stackoverflow.com/questions/3926655/how-to-keep-a-python-window-on-top-of-all-others-python-3-1
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def make_text(text):
    font_object = pygame.font.SysFont("Calibri", 50)
    return font_object.render(text, True, pygame.Color("white"))

class Game:
    def __init__(self):
        screen_info = pygame.display.Info()
        self.width, self.height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.HIDDEN)
        self.screen.set_alpha(None)
        self.screen.fill("black")

        pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)

        # Run update_window_settings just before the game loop or after the display is done being set.
        # Silly mistake here - So every time you change the display mode(pygame.display.set_mode()), you have to call update_window_settings again.
        update_window_settings()

    def run(self):
        while True:
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type in [pygame.QUIT] or event.type in [pygame.KEYDOWN] and event.key in [pygame.K_ESCAPE]:
                    pygame.quit()
                    raise SystemExit

            text = make_text("Look Ma, floating text!")
            self.screen.blit(text, (self.width/2-text.get_width()/2,self.height/2-text.get_height()/2))
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    game = Game()
    game.run()




