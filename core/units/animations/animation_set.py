#!/usr/bin/env python

from pygame import time, image, transform


class AnimationSet:
    def __init__(self, x, y, unit_name, animation_set):
        # Unit Information: Coordinates x,y & Unit Name
        self.x = x
        self.y = y
        self.unit_name = unit_name

        # Init Animation Set List: [Action][Frame Index]
        self.animation_list = []

        # Load Animation onto animation_list
        for animation_resource in animation_set:
            # Load: Unit Animations using Path to Resources
            self.animation_list.append(self.load(self.unit_name, animation_resource.type, animation_resource.frames))

        # Init Default Frames
        self.frame_index = 0
        self.action = 0  # 0: Idle, 1: Attack, 2: Hurt, 3:Death, 4:Block, 5: Miss
        self.image = self.animation_list[self.action][self.frame_index]

        self.update_time = time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    @staticmethod
    def load(name, animation, sequence_length):
        # Load: Unit Animation Sequence from Path
        animation_sequence = []
        for index in range(sequence_length):
            img = image.load(f"resources/{name}/{animation}/{index}.png")
            img = transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            animation_sequence.append(img)
        return animation_sequence

    def update(self):
        # Animation Cooldown Interval
        animation_cooldown = 100

        # Update image
        self.image = self.animation_list[self.action][self.frame_index]

        # Check if enough time has passed since the last update
        if time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = time.get_ticks()
            self.frame_index += 1

        # Reset Animations to Idle unless Death happens
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 1:
                self.frame_index = 9
            else:
                self.idle_animation()

    def reset_frame_index(self):
        self.frame_index = 0
        self.update_time = time.get_ticks()

    def idle_animation(self):
        # Activates: Idle Animation
        self.action = 0
        self.reset_frame_index()

    def draw(self, screen):
        # Place Animation on the Screen
        screen.blit(self.image, self.rect)
