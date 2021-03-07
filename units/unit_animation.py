from pygame import time, image, transform


class UnitAnimation:
    def __init__(self, x, y, unit_name):
        # Unit Information: Coordinates x,y & Unit Name
        self.x = x
        self.y = y
        self.unit_name = unit_name

        # Init Animation Set List: [Action][Frame Index]
        self.animation_list = []

        # Load: Unit Animations using Path to Resources
        self.animation_list.append(self.load_animation(self.unit_name, 'Idle', 8))
        self.animation_list.append(self.load_animation(self.unit_name, 'Attack', 8))
        self.animation_list.append(self.load_animation(self.unit_name, 'Hurt', 3))
        self.animation_list.append(self.load_animation(self.unit_name, 'Death', 10))
        self.animation_list.append(self.load_animation(self.unit_name, 'Block', 5))

        # Init Default Frames
        self.frame_index = 0
        self.action = 0  # 0: Idle, 1: Attack, 2: Hurt, 3:Death, 4:Block
        self.image = self.animation_list[self.action][self.frame_index]

        self.update_time = time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    @staticmethod
    def load_animation(name, animation, sequence_length):
        # Load: Unit Animation Sequence from Path
        tmp = []
        for index in range(sequence_length):
            img = image.load(f"resources/{name}/{animation}/{index}.png")
            img = transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            tmp.append(img)
        return tmp

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = time.get_ticks()
            self.frame_index += 1
        # reset animation to the start when run out
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = 9
            else:
                self.idle_animation()

    def caster_attack_animation(self):
        # Activates: Caster Attack Animation
        pass

    def ranged_attack_animation(self):
        # Activates: Ranged Attack Animation
        pass

    def melee_attack_animation(self):
        # Activates: Melee Attack Animation

        self.action = 1
        self.frame_index = 0
        self.update_time = time.get_ticks()

    def idle_animation(self):
        # Activates: Idle Animation
        self.action = 0
        self.frame_index = 0
        self.update_time = time.get_ticks()

    def hurt_animation(self):
        # Activates: Hurt Animation
        self.action = 2
        self.frame_index = 0
        self.update_time = time.get_ticks()

    def block_animation(self):
        # Activates: Block Animation
        self.action = 4
        self.frame_index = 0
        self.update_time = time.get_ticks()

    def death_animation(self):
        # Activates: Death Animation
        self.action = 3
        self.frame_index = 0
        self.update_time = time.get_ticks()

    def dodge_animation(self):
        # Activates: Miss Animation
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
