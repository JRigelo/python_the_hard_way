# coding=utf-8
# exercise 40
# Modules, Classes, and Objects

class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def song_length(self):
        print len(self.lyrics)

happy_bday = song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = song(["They rally around tha family",
                        "With pockets full of shells"])

my_special_song = song(["Se você pensa que cachaça é agua",
                        "Cachaça nao é agua nao"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_special_song.sing_me_a_song()

my_special_song.song_length()
