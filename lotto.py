#lotto.py by Ensi Martini
import pygame
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 1024)

class Coin(pygame.sprite.Sprite):

    def __init__(self):
        '''This class creates a Coin object, which is to replace the cursor'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image. load('resources/gold.png').convert_alpha()
        self.rect = self.image.get_rect()

class Letter(pygame.sprite.Sprite):

    def __init__(self, char, pic, position):
        '''This class creates a Letter object, with a character value, picture, and position. The object's rect is aligned to position'''
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image. load('resources/{}.png'.format(pic)).convert()
        self.image.set_colorkey((255, 255, 254))
        self.picture = pic

        self.rect = self.image.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]

        self.character = char
        self.pos = position
        self.scratched = False #This will be turned true when the tile is fully scratched, to optimize the right-clcik feature


    def is_scratched(self):
        '''L.is_scratched() --> bool
        Returns True if a letter is over 60% (1500/2500) scratched, False otherwise'''

        counter = 0

        for y in range (50):
            for x in range (50):
                if self.image.get_at((x, y)) == (255, 255, 254, 255):
                    counter += 1

        if counter >= 1500:
            return True
        return False


class Word(list):

    def __init__(self, letters = []):
        '''Creates a Word class, with a list of Letter objects'''
        list.__init__(self)

        for letter in letters:
            self.list.append(letter)

    def scratched(self):
        '''W.scratched() --> bool
        Returns True if all Letters in this list are scratched, False otherwise'''
        boolean = True

        for letter in self:
            if letter.is_scratched() == False:
                boolean = False

        return boolean

class Button(pygame.sprite.Sprite):

    def __init__(self, pic,  position, ogg):
        '''A class that models a clickable button, with a picture, position, and sound property. The object's rect is aligned to position'''
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image. load('resources/{}.png'.format(pic)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]

        self.sound = pygame.mixer.Sound('resources/{}.ogg'.format(ogg))

puzzle_1 = [['0', '0', '0', 'b', '0', '0', '0', '0', '0', '0'],\
          ['0', 'g', '0', 'a', '0', '0', '0', '0', 'b', '0'],\
          ['0', 'u', '0', 'n', '0', '0', 'g', 'r', 'i', 'p'],\
          ['g', 'a', 'n', 'g', '0', 'h', '0', '0', 'b', '0'],\
          ['0', 'r', '0', 'l', '0', 'o', '0', '0', 'l', '0'],\
          ['s', 'a', 't', 'e', 'l', 'l', 'i', 't', 'e', '0'],\
          ['0', 'n', '0', 's', '0', 'y', '0', 'r', '0', '0'],\
          ['0', 't', '0', '0', '0', '0', '0', 'a', '0', '0'],\
          ['0', 'e', '0', 'm', 'i', 'n', 'i', 'm', 'u', 'm'],\
          ['0', 'e', '0', '0', '0', '0', '0', '0', '0', '0']]

puzzle_2 = [['0', '0', '0', '0', '0', 'h', 'u', 'l', 'k', '0'],\
          ['0', '0', '0', '0', '0', '0', '0', '0', 'n', '0'],\
          ['w', '0', 'v', 'e', 'r', 't', 'i', 'g', 'o', '0'],\
          ['a', '0', '0', '0', '0', 'w', '0', '0', 'c', '0'],\
          ['n', '0', '0', '0', 'r', 'i', 'o', '0', 'k', '0'],\
          ['t', '0', 'a', '0', '0', 'n', '0', '0', 'o', '0'],\
          ['e', 'c', 'l', 'i', 'p', 's', 'e', '0', 'u', '0'],\
          ['d', '0', 'i', '0', '0', '0', '0', '0', 't', '0'],\
          ['0', 'b', 'e', 'a', 'c', 'h', '0', '0', '0', '0'],\
          ['0', '0', 'n', '0', '0', '0', '0', '0', '0', '0']]

puzzle_3 = [['0', '0', '0', '0', '0', '0', '0', '0', 'p', '0'],\
          ['0', '0', '0', '0', 'a', '0', 'c', 'l', 'u', 'e'],\
          ['w', 'o', 'u', 'n', 'd', '0', 'r', '0', 's', '0'],\
          ['o', '0', '0', '0', 'v', '0', 'o', '0', 'h', '0'],\
          ['r', '0', '0', '0', 'e', '0', 's', '0', '0', '0'],\
          ['r', '0', 'f', 'i', 'n', 'i', 's', 'h', '0', 'c'],\
          ['y', '0', '0', '0', 't', '0', 'w', '0', '0', 'r'],\
          ['0', 'm', 'e', 'n', 'u', '0', 'o', '0', '0', 'a'],\
          ['0', '0', '0', '0', 'r', '0', 'r', '0', '0', 'c'],\
          ['g', 'r', 'a', 'v', 'e', '0', 'd', 'o', 'c', 'k']]

puzzle_4 = [['0', 'r', 'e', 's', 'i', 'd', 'e', 'n', 'c', 'e'],\
          ['0', '0', '0', 'e', '0', '0', '0', '0', '0', '0'],\
          ['0', '0', '0', 'n', '0', 'r', '0', '0', 'd', '0'],\
          ['0', 'e', 'a', 's', 't', 'e', 'r', '0', 'i', '0'],\
          ['s', '0', '0', 'a', '0', 'p', '0', '0', 'v', '0'],\
          ['p', 'o', 'r', 't', 'f', 'o', 'l', 'i', 'o', '0'],\
          ['r', '0', '0', 'i', '0', 'r', '0', '0', 'r', '0'],\
          ['e', '0', '0', 'o', '0', 't', 'r', 'a', 'c', 'k'],\
          ['a', '0', '0', 'n', '0', 'e', '0', '0', 'e', '0'],\
          ['d', '0', '0', '0', 't', 'r', 'a', 'y', '0', '0']]

puzzle_5 = [['t', '0', 'd', '0', '0', 'f', 'e', 'n', 'c', 'e'],\
          ['r', '0', 'i', '0', 'b', '0', 'x', '0', '0', '0'],\
          ['i', '0', 'c', '0', 'u', '0', 'p', 'o', 'n', 'd'],\
          ['u', '0', 't', '0', 't', '0', 'l', '0', '0', '0'],\
          ['m', '0', 'i', '0', 't', '0', 'o', '0', 'b', '0'],\
          ['p', 'r', 'o', 'c', 'e', 's', 's', 'o', 'r', '0'],\
          ['h', '0', 'n', '0', 'r', '0', 'i', '0', 'a', '0'],\
          ['0', '0', 'a', '0', '0', '0', 'o', '0', 'n', '0'],\
          ['h', 'o', 'r', 'i', 'z', 'o', 'n', '0', 'd', '0'],\
          ['0', '0', 'y', '0', '0', '0', '0', '0', '0', '0']]

puzzle_6 = [['i', '0', 't', 'e', 'e', 'n', 'a', 'g', 'e', 'r'],\
          ['n', '0', '0', '0', 'n', '0', '0', '0', '0', 'o'],\
          ['n', '0', '0', '0', 'g', '0', '0', '0', '0', 'o'],\
          ['o', '0', '0', 'p', 'a', 'n', 'i', 'c', '0', 't'],\
          ['v', '0', '0', '0', 'g', '0', '0', '0', 'b', '0'],\
          ['a', '0', '0', 'd', 'e', 'c', 'k', '0', 'r', '0'],\
          ['t', '0', '0', '0', 'm', '0', '0', '0', 'o', '0'],\
          ['i', 'n', 'g', 'r', 'e', 'd', 'i', 'e', 'n', 't'],\
          ['o', '0', '0', '0', 'n', '0', '0', '0', 'z', '0'],\
          ['n', 'i', 'g', 'h', 't', 'm', 'a', 'r', 'e', '0']]

puzzle_7 = [['c', '0', '0', '0', '0', '0', '0', 'd', '0', '0'],\
          ['h', '0', '0', 'w', '0', 'p', 'i', 'a', 'n', 'o'],\
          ['a', '0', '0', 'h', '0', '0', '0', 'w', '0', '0'],\
          ['m', 'u', 's', 'i', 'c', 'i', 'a', 'n', '0', 't'],\
          ['p', '0', '0', 't', '0', '0', '0', '0', '0', 'h'],\
          ['a', 'c', 'c', 'e', 'p', 't', 'a', 'n', 'c', 'e'],\
          ['g', '0', '0', '0', '0', '0', '0', '0', '0', 'r'],\
          ['n', 'u', 'r', 's', 'e', 'r', 'y', '0', '0', 'a'],\
          ['e', '0', '0', '0', '0', '0', '0', '0', '0', 'p'],\
          ['0', '0', '0', '0', '0', '0', 'n', 'a', 'v', 'y']]

puzzle_8 = [['t', 'u', 't', 'o', 'r', '0', '0', '0', 'w', '0'],\
          ['r', '0', '0', '0', '0', 'd', '0', '0', 'o', '0'],\
          ['a', 'r', 'c', 'h', 'b', 'i', 's', 'h', 'o', 'p'],\
          ['i', '0', 'a', '0', '0', 'a', '0', '0', 'l', '0'],\
          ['n', '0', 'b', 'o', 'o', 'm', '0', 't', '0', '0'],\
          ['e', '0', '0', '0', '0', 'o', '0', 'h', '0', '0'],\
          ['r', '0', 'b', 'l', 'a', 'n', 'k', 'e', 't', '0'],\
          ['0', '0', '0', '0', '0', 'd', '0', 's', '0', '0'],\
          ['0', '0', '0', '0', '0', '0', '0', 'i', '0', '0'],\
          ['0', '0', 'c', 'o', 'n', 't', 'e', 's', 't', '0']]

puzzle_9 = [['0', '0', '0', '0', '0', '0', 'm', '0', '0', '0'],\
          ['0', 'e', 's', 'c', 'a', 'p', 'e', '0', 'c', '0'],\
          ['0', '0', '0', 'e', '0', '0', 's', '0', 'u', '0'],\
          ['v', 'i', 'l', 'l', 'a', '0', 's', '0', 'p', '0'],\
          ['i', '0', '0', 'e', '0', '0', '0', '0', 'b', '0'],\
          ['r', '0', '0', 'b', 'u', 'l', 'k', '0', 'o', '0'],\
          ['u', '0', '0', 'r', '0', '0', '0', '0', 'a', '0'],\
          ['s', '0', 'h', 'a', 'r', 'd', 'w', 'a', 'r', 'e'],\
          ['0', '0', '0', 't', '0', '0', '0', '0', 'd', '0'],\
          ['0', '0', 'm', 'e', 'r', 'g', 'e', '0', '0', '0']]

puzzle_10 = [['0', '0', 'l', '0', '0', '0', 'd', '0', '0', '0'],\
          ['t', '0', 'i', 'n', 'c', 'r', 'e', 'a', 's', 'e'],\
          ['i', '0', 'a', '0', '0', '0', 'p', '0', 't', '0'],\
          ['s', '0', 'r', '0', '0', 'c', 'a', 'r', 'r', 'y'],\
          ['s', '0', '0', '0', '0', '0', 'r', '0', 'o', '0'],\
          ['u', 'n', 'd', 'e', 'r', 's', 't', 'a', 'n', 'd'],\
          ['e', '0', '0', '0', '0', '0', 'm', '0', 'g', '0'],\
          ['0', 'm', 'a', 'n', 'a', 'g', 'e', 'r', '0', '0'],\
          ['0', '0', '0', '0', '0', '0', 'n', '0', '0', '0'],\
          ['0', 'i', 'n', 'd', 'u', 's', 't', 'r', 'y', '0']]

puzzle_11 = [['p', '0', '0', '0', 's', 'h', 'a', 'c', 'k', '0'],\
          ['o', '0', 'i', '0', '0', '0', '0', 'h', '0', 'p'],\
          ['w', 'a', 'n', 't', '0', 'p', 'l', 'a', 'c', 'e'],\
          ['e', '0', 't', '0', '0', '0', '0', 'r', '0', 'l'],\
          ['r', '0', 'e', '0', '0', '0', '0', 'g', '0', 'i'],\
          ['0', 'p', 'r', 'o', 'd', 'u', 'c', 'e', '0', 'c'],\
          ['0', '0', 'e', '0', '0', '0', '0', '0', '0', 'a'],\
          ['b', 'u', 's', 'i', 'n', 'e', 's', 's', '0', 'n'],\
          ['0', '0', 't', '0', '0', '0', '0', 'e', '0', '0'],\
          ['0', '0', '0', 'c', 'o', 'u', 'n', 't', 'r', 'y']]

puzzle_12 = [['0', '0', '0', 'r', 'i', 'c', 'e', '0', '0', '0'],\
          ['0', '0', '0', '0', '0', 'o', '0', 'm', '0', '0'],\
          ['0', 'r', 'e', 'm', 'e', 'm', 'b', 'e', 'r', '0'],\
          ['s', '0', '0', '0', '0', 'm', '0', 'm', '0', '0'],\
          ['u', '0', '0', 'l', '0', 'u', '0', 'b', '0', 's'],\
          ['g', 'o', 'v', 'e', 'r', 'n', 'm', 'e', 'n', 't'],\
          ['g', '0', '0', 'a', '0', 'i', '0', 'r', '0', 'u'],\
          ['e', '0', '0', 'n', '0', 't', '0', '0', '0', 'd'],\
          ['s', '0', '0', '0', '0', 'y', '0', 't', 'r', 'y'],\
          ['t', 'h', 'i', 'n', 'k', '0', '0', '0', '0', '0']]

puzzle_13 = [['m', 'i', 's', 's', 'i', 'l', 'e', '0', '0', 'o'],\
          ['0', '0', 'k', '0', '0', '0', '0', 'c', '0', 'x'],\
          ['0', 'd', 'i', 'r', 'e', 'c', 't', 'o', 'r', 'y'],\
          ['u', '0', 'r', '0', '0', 'o', '0', 'm', '0', 'g'],\
          ['n', '0', 't', '0', '0', 'p', '0', 'p', '0', 'e'],\
          ['i', '0', '0', '0', '0', 'p', '0', 'e', '0', 'n'],\
          ['f', '0', '0', 't', 'h', 'e', 'f', 't', '0', '0'],\
          ['o', '0', 'm', '0', '0', 'r', '0', 'e', '0', '0'],\
          ['r', '0', 'u', '0', '0', '0', '0', 'n', '0', '0'],\
          ['m', 'i', 'd', 'n', 'i', 'g', 'h', 't', '0', '0']]

puzzle_14 = [['0', 's', 'c', 'u', 'l', 'p', 't', 'o', 'r', '0'],\
          ['0', 'a', '0', '0', '0', 'r', '0', '0', '0', '0'],\
          ['i', 'n', 'k', '0', '0', 'e', '0', '0', 's', '0'],\
          ['0', 'd', '0', '0', '0', 'g', '0', '0', 't', '0'],\
          ['0', 'w', '0', '0', '0', 'n', '0', '0', 'r', '0'],\
          ['d', 'i', 'a', 'g', 'r', 'a', 'm', '0', 'o', '0'],\
          ['0', 'c', '0', '0', '0', 'n', '0', '0', 'k', '0'],\
          ['0', 'h', '0', 'r', 'e', 'c', 'i', 'p', 'e', '0'],\
          ['0', '0', '0', 'o', '0', 'y', '0', 'a', '0', '0'],\
          ['b', 'l', 'a', 'd', 'e', '0', '0', 't', '0', '0']]

puzzle_15 = [['p', 'o', 'e', 't', '0', '0', '0', '0', 'p', '0'],\
          ['0', '0', '0', 'h', '0', 'w', '0', '0', 'a', '0'],\
          ['0', 'f', 'u', 'r', 'n', 'i', 't', 'u', 'r', 'e'],\
          ['0', '0', '0', 'o', '0', 't', '0', '0', 'a', '0'],\
          ['c', '0', '0', 'a', 'u', 'n', 't', '0', 'g', '0'],\
          ['a', '0', '0', 't', '0', 'e', '0', '0', 'r', '0'],\
          ['r', '0', 'j', '0', '0', 's', '0', '0', 'a', '0'],\
          ['p', 'r', 'o', 'm', 'i', 's', 'e', '0', 'p', '0'],\
          ['e', '0', 'k', '0', '0', '0', '0', '0', 'h', '0'],\
          ['t', 'i', 'e', '0', '0', '0', '0', '0', '0', '0']]

#All of these values are set here because they never change
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Crossword')

win = pygame.image. load('resources/win.png')
lose = pygame.image. load('resources/lose.png')

sounds = [pygame.mixer.Sound('resources/scratch1.ogg'), pygame.mixer.Sound('resources/scratch2.ogg'), pygame.mixer.Sound('resources/scratch3.ogg'), pygame.mixer.Sound('resources/scratch4.ogg'), pygame.mixer.Sound('resources/scratch5.ogg'), pygame.mixer.Sound('resources/scratch6.ogg'), pygame.mixer.Sound('resources/scratch7.ogg'), pygame.mixer.Sound('resources/scratch8.ogg'), pygame.mixer.Sound('resources/scratch9.ogg'), pygame.mixer.Sound('resources/scratch10.ogg'), pygame.mixer.Sound('resources/scratch11.ogg'), pygame.mixer.Sound('resources/scratch12.ogg'), pygame.mixer.Sound('resources/pop.ogg'), pygame.mixer.Sound('resources/lose.ogg'), pygame.mixer.music. load('resources/techno.mp3')]

disco_colors = [(252, 0, 0), (0, 252, 0), (0, 0, 252), (252, 128, 0), (252, 252, 0), (128, 0, 252), (252, 0, 128)]

coin = Coin()

done = Button('done',  (450, 0), 'click')
retry = Button('retry',  (200, 350), 'click')

restart = True
#This is used later for the vertical list parsing of the crossword
pos_dict = {0:0, 50:1, 100:2, 150:3, 200:4, 250:5, 300:6, 350:7, 400:8, 450:9}

while restart:

    font = pygame.font.SysFont('oldenglishtext', 48)

    background = pygame.Surface((500, 700)).convert()
    background.fill((0, 0, 0))

    redblock = pygame.Surface((500, 200)).convert()
    redblock.fill((244, 68, 56))

    redblock.blit(font.render('Crossword', True, (63, 81, 181)), (144, 0))

    puzzle = [puzzle_1, puzzle_2, puzzle_3, puzzle_4, puzzle_5, puzzle_6, puzzle_7, puzzle_8, puzzle_9, puzzle_10, puzzle_11, puzzle_12, puzzle_13, puzzle_14, puzzle_15][randint(0, 14)]

    x_pos = 0
    y_pos = 200
    tiles = pygame.sprite.OrderedUpdates()

    #These will be lists of tiles and empty blocks, used later for checking wins
    vertical = [[], [], [], [], [], [], [], [], [], []]
    horizontal = [[], [], [], [], [], [], [], [], [], []]

    h_counter = 0

    for row in puzzle:
        for char in row:

            if char != '0':
                tile = Letter(char, char, (x_pos, y_pos))
                tiles.add(tile)
                #Gluing a 'scratched' version of the tile to the background
                background.blit(pygame.image.load('resources/' + char + '2.png').convert_alpha(), (x_pos, y_pos))

            else:
                tile = '0'
                background.blit(pygame.image. load('resources/0.png'), (x_pos, y_pos))

            vertical[pos_dict[x_pos]].append(tile)
            horizontal[h_counter].append(tile)

            x_pos += 50

        h_counter += 1
        x_pos = 0
        y_pos += 50

    words = []
    word = Word()

    #Parsing the vertical/horizontal lists for words
    for word_list in [vertical, horizontal]:
        for row in word_list:
            for tile in row:

                if tile != '0':
                    word.append(tile)

                #The second condition makes sure a word gets added even if it reaches the end of the row
                if tile == '0' or row.index(tile) == 9:
                    if len(word) > 1:
                        words.append(word)
                    word = Word()

    #These are the stars at the top
    matches = pygame.sprite.OrderedUpdates()
    letter_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    letters = []

    x_pos = 100
    y_pos = 50

    font = pygame.font.SysFont('arial', 24)
    font.set_bold(True)

    for star in range(1, 19):
        index = randint(0, len(letter_list) - 1)

        if star % 2 == 0:
            matches.add(Letter(letter_list[index], 'b_star', (x_pos, y_pos)))

        else:
            matches.add(Letter(letter_list[index], 'r_star', (x_pos, y_pos)))

        #Gluing the text version of the letter behind the star
        redblock.blit(font.render(letter_list[index].upper(), True, (63,81,181)), (x_pos + 18, y_pos + 12))
        letter_list.pop(index)
        x_pos += 50

        if star % 6 == 0:
            y_pos += 50
            x_pos = 100

    screen.blit(background, (0, 0))
    background.blit(redblock, (0,0))

    restart = False
    word_counter = 0
    font = pygame.font.SysFont('georgia', 55)
    falling = pygame.sprite.OrderedUpdates() #Used after winning for falling animation

    clock = pygame.time.Clock()
    keep_going = True
    pygame.mouse.set_visible(0)

    while keep_going:

        clock.tick(60)

        for ev in pygame.event.get():

            if ev.type == QUIT:
                keep_going = False

            elif ev.type == MOUSEMOTION:

                coin.rect.center = ev.pos

                if pygame.mouse.get_pressed()[0]: #Checking this before looping through the groups is more efficient than vice versa

                    #Going through all the match stars, and "scratching" all those in contact with the coin
                    for collide in pygame.sprite.spritecollide(coin, matches, False):

                        #Prevents unnecessary lines from being drawn, improving framerate
                        if collide.scratched == False:
                            pygame.draw.line(collide.image, (255, 255, 254), (randint(0,50), randint(0,50)), (randint(0,50), randint(0,50)), 6)
                            sounds[randint(0, 11)].play()

                        #Keeps track of which letter are valid to scratch
                        if collide.character not in letters and collide.is_scratched():
                            letters.append(collide.character)

                    #Same thing for the tiles
                    for collide in pygame.sprite.spritecollide(coin, tiles, False):

                        if collide.scratched == False:
                            if collide.character in letters:
                                pygame.draw.line(collide.image, (255, 255, 254), (randint(0,50), randint(0,50)), (randint(0,50), randint(0,50)), 6)
                                sounds[randint(0, 11)].play()

                #Holding down right click while moving the coin completly clears the tile
                if pygame.mouse.get_pressed()[2]:

                    blank = True

                    for collide in pygame.sprite.spritecollide(coin, matches, False):
                        if collide.scratched == False:

                            for y in range (50):
                                for x in range (50):

                                    if collide.image.get_at((x, y)) != (255, 255, 254, 255):
                                        blank = False
                                        collide.image.set_at((x, y), (255, 255, 254, 255))

                            collide.scratched = True

                        #Keeps track of which letter are valid to scratch
                        if collide.character not in letters and collide.is_scratched():
                            letters.append(collide.character)

                    #Only allows for the sound to be played once per tile clear
                    if blank == False:
                        sounds[12].play()

                    #Same thing for tiles, but only if that letter is in the matches
                    for collide in pygame.sprite.spritecollide(coin, tiles, False):

                        if collide.character in letters:
                            blank = True

                            if collide.scratched == False:
                                for y in range (50):
                                    for x in range (50):

                                        if collide.image.get_at((x, y)) != (255, 255, 254, 255):
                                            blank = False
                                            collide.image.set_at((x, y), (255, 255, 254, 255))

                                collide.scratched = True

                    if blank == False:
                        sounds[12].play()

            elif ev.type == MOUSEBUTTONUP:
                #Intended to stop scratching sounds when scratching stops, accounts for button presses
                if word_counter != None:
                    pygame.mixer.stop()

            elif ev.type == KEYDOWN and ev.key == K_SPACE:

                #Fully solve the puzzle for the player
                for sprite in matches.sprites():

                    if sprite.character not in letters:
                        letters.append(sprite.character)

                    if sprite.scratched == False:
                        for y in range(50):
                            for x in range(50):
                                sprite.image.set_at((x, y), (255, 255, 254, 255))

                    sprite.scratched = True

                sounds[12].play() #This is done here to seem in sync to the player with the action

                for sprite in tiles.sprites():
                    if sprite.scratched == False and sprite.character in letters:
                        for y in range(50):
                            for x in range(50):
                                sprite.image.set_at((x, y), (255, 255, 254, 255))

                        sprite.scratched = True

            elif ev.type == MOUSEBUTTONDOWN:

                if coin.rect.colliderect(done.rect):
                    done.sound.play()

                    #Also solving the puzzle, gives player true game result
                    for sprite in matches.sprites():

                        if sprite.character not in letters:
                            letters.append(sprite.character)

                        if sprite.scratched == False:
                            for y in range(50):
                                for x in range(50):
                                    sprite.image.set_at((x, y), (255, 255, 254, 255))

                            sprite.scratched = True

                    for sprite in tiles.sprites():
                        if sprite.scratched == False and sprite.character in letters:
                            for y in range(50):
                                for x in range(50):
                                    sprite.image.set_at((x, y), (255, 255, 254, 255))

                        sprite.scratched = True

                    for word in words:
                        if word.scratched():
                            word_counter += 1

                    if word_counter != None and word_counter > 0:
                        pygame.mixer.music.play(-1)

                    else:
                        word_counter = None #This lets the program know that we've finished playing but haven't won
                        sounds[13].play()



                if coin.rect.colliderect(retry.rect):

                    retry.sound.play()
                    restart = True
                    keep_going = False
                    #Stops the disco music, not button click
                    pygame.mixer.music.stop()

                for collide in pygame.sprite.spritecollide(coin, falling, False):
                    collide.kill()
                    sounds[12].play()
        screen.blit(background, (0, 0))

        if word_counter != None and word_counter > 0:
            #Creating a fade-out effect, compliments disco music
            color = background.get_at((0, 0))

            if color == (0, 0, 0):

                index = randint(0, 6)
                background.fill(disco_colors[index])

                #Preventing the same color from appearing twice in a row
                disco_colors.append(disco_colors[index])
                disco_colors.pop(index)

            else:
                #If no single RGB value is 0, darken the shade
                if color[0] >= 4:
                    color = (color[0] - 4, color[1], color[2])

                if color[1] >= 4:
                    color = (color[0], color[1] - 4, color[2])

                if color[2] >= 4:
                    color = (color[0], color[1], color[2] - 4)

                background.fill(color)

            pygame.mouse.set_visible(1)
            screen.blit(win, (0, 250))

            for letter in tiles:
                if randint(0, 1000) == 1: #Making the amount of letters falling scarce
                    #Adding a copy of an existing letter in the list
                    falling.add(Letter(letter.character, letter.picture, (randint(0, 450), -10)))

            for letter in falling:
                letter.rect.top += 1

                #Making sure the letters fade out as they reach the bottom
                if letter.rect.top % 2 == 0:
                    letter.image.set_alpha(letter.image.get_alpha() - 1)

                #Removing the letters that are falling under the screen from the list
                if letter.rect.top > 700:
                    falling.remove(letter)

            falling.update(screen, background)
            falling.draw(screen)

            if word_counter == 1:
                screen.blit(font.render('SCORE: 1 WORD', True, (255, 255, 255)), (48, 150))

            else:
                screen.blit(font.render('SCORE: {} WORDS'.format(word_counter), True, (255, 255, 255)), (15, 150))

            screen.blit(retry.image, retry.rect)

        elif word_counter == None:

            background.fill((122, 122, 122))
            screen.blit(lose, (0, 250))
            screen.blit(retry.image, retry.rect)
            pygame.mouse.set_visible(1)

        if word_counter == 0:
            #If the game is still going
            tiles.update(screen, background)
            tiles.draw(screen)

            matches.update(screen, background)
            matches.draw(screen)

            screen.blit(done.image, done.rect)
            screen.blit(coin.image, coin.rect)

        pygame.display.flip()
