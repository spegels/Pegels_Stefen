song1 = "Na"
song2 = "Hey"
song3 = "Goodbye!"
times1 = 4
times2 = 3
times3 = 1
output = " "
def lyricPrint(song, times):
    for i in range(len(song), times):
        output = " " + str(i) + " "
        print(output)

lyricPrint(song1,times1)
lyricPrint(song1,times1)
lyricPrint(song2,times2)
lyricPrint(song3,times3)
