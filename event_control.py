from pygame import event, QUIT, MOUSEBUTTONDOWN
import constants.globals


def event_control():
    for _event in event.get():
        if _event.type == QUIT:
            constants.globals.run = False
            constants.globals.runbattle = False

        if _event.type == MOUSEBUTTONDOWN:
            constants.globals.clicked = True

        else:
            constants.globals.clicked = False