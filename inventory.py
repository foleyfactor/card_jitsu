from collections import defaultdict
from element import Element
from random import randint

class Inventory(object):
    def __init__(self):
        self.by_element = defaultdict(list)
        self.by_color = defaultdict(list)
    
    def add(self, card):
        element = card.element
        color = card.color
        if color in self.by_element[element]:
            return
        self.by_element[element].append(color)
        self.by_color[color].append(element)
    
    def remove_one_element(self, element):
        colors = self.by_element[element] 
        if len(colors) == 0:
            return
        i = randint(0, len(colors)-1)
        color = colors[i]
        by_color_index = self.by_color[color].index(element)
        del(self.by_color[color][by_color_index])
        del(colors[i])
    
    def remove_one_color(self, color):
        elements = self.by_color[color]
        if len(elements) == 0:
            return
        i = randint(0, len(elements)-1)
        element = elements[i]
        by_element_index = self.by_element[element].index(color)
        del(self.by_element[element][by_element_index])
        del(elements[i])
    
    def remove_all_color(self, color):
        self.by_color[color] = []
        for element in self.by_element:
            self.by_element[element] = [c for c in self.by_element[element] if c != color]

    def has_won(self):
        same_element_win = max([len(self.by_element[x]) for x in self.by_element]) == 3
        if same_element_win:
            return True

        for fire_color in self.by_element[Element.FIRE]:
            for water_color in self.by_element[Element.WATER]:
                for snow_color in self.by_element[Element.SNOW]:
                    if fire_color != water_color and water_color != snow_color and fire_color != snow_color:
                        return True
        
        return False
    
    def display(self):
        for element in self.by_element:
            for col in self.by_element[element]:
                print("{} {}".format(col.name, element.name))
