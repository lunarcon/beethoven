import time
from threading import Thread
from msvcrt import getch
from synthesizer import Player, Synthesizer, Waveform
import numpy as np
from sys import stdout

def wave_damp(wave, damp):  return np.array([wave[i] * (1 - damp * i / len(wave)) for i in range(len(wave))])

notes = {
    'c': 16.3515,
    'd': 18.3540,
    'e': 20.6017,
    'f': 21.8267,
    'g': 24.4997,
    'a': 27.5,
    'b': 30.8677,
}

def nf(note):
    out=0
    if len(note) > 0:   out=notes[note[0]]
    if len(note) > 1:
        if note[1].isdigit():   out *= 2 ** int(note[1])
        if note[-1] == 'b': out *= 0.9438743126816935
        if note[-1] == '#': out *= 1.0594630943592953
    return out

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, osc2_waveform=Waveform.sine, osc2_volume=1.1, osc2_freq_transpose=0.5, use_osc2=True)
def play(note, duration=0.25):
    if note == None:
        time.sleep(duration)
        return
    if type(note) == str:
        player.play_wave(wave_damp(synthesizer.generate_constant_wave(nf(note), duration), 0.7))
    elif type(note) == list:
        player.play_wave(wave_damp(synthesizer.generate_chord([nf(n) for n in note], duration), 0.5))

F = 1
H = 0.5
Q = 0.25
E = 0.125
S = 0.0625

def set_timesig(numerator, denominator):
    global F, H, Q, E, S
    F = 4 * numerator / denominator
    H = F / 2
    Q = F / 4
    E = F / 8
    S = F / 16

set_timesig(3, 8)
fur_elise = [
    ('e5', E), ('d5#', E), ('e5', E), ('d5#', E), ('e5', E), ('b4', E), ('d5', E), ('c5', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E), ('c4', E), ('e4', E), ('a4', E),
    (['b4', 'e3'], Q), ('e4', E), ('g4#', E), ('e4', E), ('g4#', E), ('b4', E),
    (['c5', 'a3'], Q), ('e4', E), ('a4', E), ('e4', E),

    ('e5', E), ('d5#', E), ('e5', E), ('d5#', E), ('e5', E), ('b4', E), ('d5', E), ('c5', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E), ('c4', E), ('e4', E), ('a4', E),
    (['b4', 'e3'], Q), ('e4', E), ('g4#', E), ('e4', E), ('c5', E), ('b4', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E),

    (None, E), 

    ('e5', E), ('d5#', E), ('e5', E), ('d5#', E), ('e5', E), ('b4', E), ('d5', E), ('c5', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E), ('c4', E), ('e4', E), ('a4', E),
    (['b4', 'e3'], Q), ('e4', E), ('g4#', E), ('e4', E), ('g4#', E), ('b4', E),
    (['c5', 'a3'], Q), ('e4', E), ('a4', E), ('e4', E),

    ('e5', E), ('d5#', E), ('e5', E), ('d5#', E), ('e5', E), ('b4', E), ('d5', E), ('c5', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E), ('c4', E), ('e4', E), ('a4', E),
    (['b4', 'e3'], Q), ('e4', E), ('g4#', E), ('e4', E), ('c5', E), ('b4', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E),

    ('b4', E), ('c5', E), ('d5', E), (['e5', 'c4'], Q), ('g4', E), ('c5', E), ('g4', E), ('f5', E), ('e5', E),
    (['d5', 'g3'], Q), ('g4', E), ('b4', E), ('f4', E), ('e5', E), ('d5', E),
    (['c5', 'a3'], Q), ('e4', E), ('a4', E), ('e4', E), ('d5', E), ('c5', E),
    (['b4', 'e2'], Q), ('e3', E), ('e4', E), ('e4', E), ('e5', E), ('e4', E),

    ('e6', E), ('d5#', E), ('e5', E), ('d5#', E), ('e5', E), ('b4', E), ('d5', E), ('c5', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E), ('c4', E), ('e4', E), ('a4', E),
    (['b4', 'e3'], Q), ('e4', E), ('g4#', E), ('e4', E), ('g4#', E), ('b4', E),
    (['c5', 'a3'], Q), ('e4', E), ('a4', E), ('e4', E),

    ('e5', E), ('d5#', E), ('e5', E), ('d5#', E), ('e5', E), ('b4', E), ('d5', E), ('c5', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E), ('c4', E), ('e4', E), ('a4', E),
    (['b4', 'e3'], Q), ('e4', E), ('g4#', E), ('e4', E), ('c5', E), ('b4', E),
    (['a4', 'a3'], Q), ('e4', E), ('a4', E),

    (None, E)
]


VIOLET = (128, 0, 128)
RED = (255, 40, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
INDIGO = (75, 0, 130)

COLORS = {
    'c': VIOLET,
    'd': INDIGO,
    'e': BLUE,
    'f': GREEN,
    'g': YELLOW,
    'a': ORANGE,
    'b': RED
}

def ANSI_COlOR(color):  return '\033[38;2;{};{};{}m'.format(*color)

def note_to_color(note):
    if type(note) == str:
        basecolor = COLORS[note[0]]
        add=note[-1] if note[-1] in '0123456789' else note[-2]
        if add != note[0]:
            add = int(add) - 3
            add = add * 22
            basecolor = [max(min(255, x+add),0) for x in basecolor]
        return ANSI_COlOR(basecolor) + note + '\033[0m'
    elif type(note) == list:
        out = '['
        for n in note:
            out += note_to_color(n) + ', '
        return out + '\b\b]'
    else:
        return ANSI_COlOR(BLACK) + '  \033[0m,'

def main():
    for cur,note in enumerate(fur_elise):
        stdout.write('\033[K'*(not cur % 8))
        stdout.write(note_to_color(note[0]))
        stdout.write(', '*(cur%8 != 0) + ' '*10*(not cur%8) + '\r'*(not cur%8))
        stdout.flush()
        play(note[0], note[1])
    stdout.write('\033[K'); stdout.flush()

if __name__ == '__main__':
    main()