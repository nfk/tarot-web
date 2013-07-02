'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 25 oct. 2009
'''


class Carte:
    ''' card of tarot '''

    def __init__(self, name, value, point, color):
        self.id = 0;
        self.name = name
        self.value = int(value)
        self.point = float(point)
        self.color = color

    def __str__(self):
        ''' return string with card attributes'''
        return '%s(%d) %s - point = %.1f' % (self.name, self.value,
                                             self.color, self.point)
