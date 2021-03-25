from interface.basic_components.ui_element import UIElement

class UILayout(UIElement):
    def __init__(self):
        super().__init__()
        self.elements = []

    def add_ui_element(self, element):
        self.elements.append(element)