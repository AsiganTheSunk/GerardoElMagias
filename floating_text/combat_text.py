from constants.basic_fonts import combat_text_font, critical_combat_text_font, cast_text_font
from floating_text.floating_text_effects import FloatingTextEffects


class CombatText(FloatingTextEffects):
    def __init__(self, x, y, text, text_color, animation_type):
        FloatingTextEffects.__init__(self, x, y, animation_type)

        self.text = text
        self.text_color = text_color

    def cast_text(self):
        self.image = cast_text_font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        return self.image

    def combat_text(self):
        self.image = combat_text_font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        return self.image

    def critical_combat_text(self):
        self.image = critical_combat_text_font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        return self.image
