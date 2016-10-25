

song1 = "Na"
song2 = "Hey"
song3 = "Goodbye!"
times1 = 4
times2 = 3
times3 = 1


def lyricPrint(song, times):
    output = ""
    for i in range(0, times):
        output =output + song + " "
    print(output)


lyricPrint(song1,times1)
lyricPrint(song1,times1)
lyricPrint(song2,times2)
lyricPrint(song3,times3)
