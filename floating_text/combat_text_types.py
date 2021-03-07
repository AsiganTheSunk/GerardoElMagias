from constants.basic_fonts import combat_text_font, critical_combat_text_font, cast_text_font
from floating_text.floating_text_effects import FloatingTextEffects


class CombatTextTypes(FloatingTextEffects):
    def __init__(self, x, y, animation_type):
        FloatingTextEffects.__init__(self, x, y, animation_type)
        self.image = None

    def cast_text(self, text, text_color):
        self.image = cast_text_font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def combat_text(self, text, text_color):
        self.image = combat_text_font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def critical_combat_text(self, text, text_color):
        self.image = critical_combat_text_font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
