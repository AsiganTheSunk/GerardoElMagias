#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import event, QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, USEREVENT, MOUSEMOTION, mouse
import constants.globals
from interface.ui_elements.ui_button import UIButton
from interface.ui_elements.ui_text_button import UITextButton

MOUSE_OVER = USEREVENT + 1


class GameEventControl:
    def __init__(self):
        self.subscribers = []
        self.conditions = []
        self.last_event = None
        self.custom_event_conditions = [
            (lambda subscriber:
             subscriber.rect.collidepoint(mouse.get_pos()), event.Event(MOUSE_OVER))
        ]

    def resolve_custom_event_conditions(self):
        for subscriber in self.subscribers:
            if isinstance(subscriber, UIButton):
                custom_event = [e for (c, e) in self.custom_event_conditions if c(subscriber)]
                if custom_event:
                    event.post(custom_event[0])

    # def add_event_condition(self, event_name, event_condition):
    #     self.conditions.append(
    #         (lambda subscriber: event_condition, event.Event(event_name)))

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def handle_click(self, game_event):
        for subscriber in self.subscribers:
            # TODO: crear una interfaz llamada "clickable", en lugar de chequear todos los elementos
            if 'click' in subscriber.events:
                click_callback = subscriber.events['click']
                if not subscriber.hidden and subscriber.rect.collidepoint(mouse.get_pos()):
                    click_callback(game_event, subscriber)

    def manage_events(self):
        self.resolve_custom_event_conditions()

        for game_event in event.get():
            if game_event.type == QUIT:
                constants.globals.run_game = False
                constants.globals.run_stage = False

            if game_event.type == MOUSEBUTTONDOWN:
                event_controller.handle_click(game_event)
                constants.globals.clicked = True

            # if game_event.type == MOUSE_OVER:
            #     event_controller.handle_mouse_over(game_event)

            if game_event.type == MOUSEBUTTONUP:
                constants.globals.clicked = False

            # Check for changes in events so mouse_over can be deactivated
            # event_controller.handle_mouse_over(game_event)


event_controller = GameEventControl()

#
#
# def event_control():
#     # generate events from conditions
#     # map(event.post, [e for (c, e) in event_conditions if c()])
#
#     for game_event in event.get():
#         if game_event.type == QUIT:
#             constants.globals.run_game = False
#             constants.globals.run_stage = False
#
#         if game_event.type == MOUSEBUTTONDOWN:
#             event_controller.handle_click(game_event)
#             constants.globals.clicked = True
#
#         if game_event.type == MOUSEMOTION:
#             event_controller.handle_mouse_over(game_event)
#
#         if game_event.type == MOUSEBUTTONUP:
#             constants.globals.clicked = False
