#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import event, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import constants.globals


class GameEventControl:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def handle_click(self, game_event):
        for subscriber in self.subscribers:
            # TODO: crear una interfaz llamada "clickable", en lugar de chequear todos los elementos
            if 'click' in subscriber.events:
                click_callback = subscriber.events['click']
                if not subscriber.hidden and subscriber.rect.collidepoint(game_event.pos):
                    click_callback(game_event, subscriber)


event_controller = GameEventControl()


def event_control():
    for game_event in event.get():
        if game_event.type == QUIT:
            constants.globals.run_game = False
            constants.globals.run_stage = False

        if game_event.type == MOUSEBUTTONDOWN:
            event_controller.handle_click(game_event)
            constants.globals.clicked = True

        if game_event.type == MOUSEBUTTONUP:
            constants.globals.clicked = False