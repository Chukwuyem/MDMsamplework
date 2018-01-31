## written by Chukwuyem & Dharini

import Tkinter as Tk
import rhythm_player
import final_classes
import random
import __future__
import re
from Interval import *


short_desc = 'This is a description of Apollo\'s project. This is a small app/learning tool/game that teaches the user ' \
             'the \nfundamentals on the two major basic aspects of music: rhythm and scales. It is really cool. Choose either ' \
             'below.'

#main Tkinter window
window = Tk.Tk()
window.title("JUST Music")
window.geometry('{}x{}'.format(800, 400))
# window.resizable(width=False, height=False)

#title
title_label = Tk.Label(window, text='JUST Music', font=("Courier", 32, "bold"))
title_label.pack(fill='x')

#frames
home_frame = Tk.Frame(window, padx=10)
rhythm_frame = Tk.Frame(window)
scales_frame = Tk.Frame(window, pady=10, padx=5)
piano_frame = Tk.Frame(window)

#labelframe
intro_frame = Tk.LabelFrame(home_frame, text='Welcome to Just Music',font=("MS Sans", 24), padx=15, pady=15)

short_description = Tk.Label(intro_frame, text=short_desc)
short_description.pack(side='left')

intro_frame.grid(row=0, columnspan=12, padx=10, pady=(10, 25)) #.pack(fill='x')

#button to direct to parts of the app/project

def render_rhythm():
    home_frame.destroy()
    rhythm_frame.pack(fill='both', expand='yes')
    window.geometry('{}x{}'.format(800, 500))

def render_scales():
    home_frame.destroy()
    scales_frame.pack(fill='both')
    window.geometry('{}x{}'.format(800, 800))

def render_piano():
    home_frame.destroy()
    piano_frame.pack(fill='both')
    window.geometry('{}x{}'.format(1000, 800))



select_label = Tk.Label(home_frame, text="Select one of the following sections to begin", font=("MS Sans", 16))
select_label.grid(row=3, pady=(0, 10))

rhythm_button = Tk.Button(home_frame, text='Just Rhythm', bg = '#fefefe',activebackground= '#8589d5', width=20,
                          pady=5, command= render_rhythm)
rhythm_button.grid(row=4, pady=(0, 10)) #pack()
scales_button = Tk.Button(home_frame, text='Just Compose', bg = '#fefefe',activebackground= '#8589d5',width=20,
                          pady=5, command= render_scales)
scales_button.grid(row=5, pady=(0, 10)) #pack()
piano_button = Tk.Button(home_frame, text='Just Piano', bg= '#fefefe',activebackground='#8589d5', width=20,
                         pady=5, command=render_piano)
piano_button.grid(row=6, pady=(0, 10)) #pack()



#RHYTHM_SECTION###################################################################
# home_button= Tk.Button(rhythm_frame, text='Home', bg= '#fefefe',activebackground='#8589d5', width=20,
#                          pady=5, command=render_piano)
# home_button.grid(row=0, sticky='E')

rhythm_label = Tk.Label(rhythm_frame, text='JUST Rhythm', font=("Courier", 18))
rhythm_label.grid(row=0, columnspan=10)

sounds_frame = Tk.Frame(rhythm_frame)
sounds_frame.grid(row=1, column=0, columnspan=4)#.pack(fill='y',side='left')


sounds_label = Tk.Label(sounds_frame, text='List of Sounds', bg='#545454', fg='#fafafa', width=20)
sounds_label.pack()

for x in list(reversed([i for i in range(1,9)])): #range(1,5):
    label = str(x)
    file_n = 'bit'+label+'.wav'
    beat_bttn = Tk.Button(sounds_frame, width=20, relief='groove', bd=0, text='Beat '+label, command=lambda file_n=file_n: rhythm_player.player(file_n))
    beat_bttn.pack()

#patterns
def single_pattern_player(init_beat_str):
    #get input string
    if init_beat_str == '':
        init_beat_str = raw_input('Enter string: ')

    print init_beat_str

    #get unique set of input string
    each_beat_set = set()
    for x in init_beat_str.split(','):
        each_beat_set.add(x)

    #get corresponding beat for each element in set
    each_beat_set_dict = dict()

    num_l = list([x for x in range(1, 8+1)])
    for x in each_beat_set:
        num = random.choice(num_l)
        num_l.remove(num)
        file_str = 'bit'+str(num)+'.wav'
        each_beat_set_dict[x] = file_str


    #play input string

    for x in init_beat_str.split(','):
        rhythm_player.player(each_beat_set_dict[x])
        time.sleep(float(tempo_var.get())/100)

    print float(tempo_var.get())
    x = 15
    while lp_var.get() == 1 and x > 0:
        for x in init_beat_str.split(','):
            rhythm_player.player(each_beat_set_dict[x])
            #time.sleep(tempo_slider.get())
        x -= 1

def play_ptrn_bttn_functn(): #function to play pattern with randomly selected beats
    single_pattern_player(ptrn.get())


#pattern input
r_input_frame = Tk.Frame(rhythm_frame, padx=35, pady=20)
r_input_frame.grid(row=1, column=4, columnspan=5)#.pack(fill='both', side='top', padx=25, pady=20)

ptrn_input_label = Tk.Label(r_input_frame, text='Rhythm Pattern Input')
ptrn_input_label.grid(row=15, columnspan=7, column=2) #ptrn_input_label.pack(fill='x')
ptrn = Tk.StringVar()
ptrn_input = Tk.Entry(r_input_frame, textvariable=ptrn, width=50)
ptrn_input.grid(columnspan=7, column=2) #.pack()
#loop button
lp_var = Tk.IntVar()
loop_bttn = Tk.Checkbutton(r_input_frame, text="Loop", pady=20, variable=lp_var)
loop_bttn.grid(rowspan=3, columnspan=7, column=2)
tempo_var = Tk.StringVar()
tempo_slider = Tk.Scale(r_input_frame, from_=0, to=10, resolution=0.5, variable=tempo_var, relief='flat', label='Tempo',
                        length=200, orient='horizontal')
tempo_slider.grid(rowspan=5, columnspan=7, column=2)

#play pattern button
play_bttn = Tk.Button(r_input_frame, bd=1,bg = '#fefefe', activebackground= '#8589d5', text='Play Pattern', command= play_ptrn_bttn_functn)
play_bttn.grid(rowspan=5, columnspan=7, column=2, pady=20) #.pack(side='top')

###################################################################

#PIANO SECTION#####################################################################
NoteToIntervalNumber = {'Gb':-6, 'Db':-5, 'Ab':-4, 'Eb':-3, 'Bb':-2, 'F':-1, 'C':0, 'G':1, 'D':2, 'A':3, 'E':4, 'B':5, 'F#':6, 'C#':7,
                        'G#':8, 'D#':9, 'A#':10}

def key_plyr(key, scale, octave):
    #do something
    if str(scale) == "Pythagorean Dodecaphonic":
        dodec_key = final_classes.dodecaphonic_series( NoteToIntervalNumber[str(key)], 528)
        frequency = dodec_key.finalFrequency
        if octave >= 0:
            frequency *= (octave + 1)
        else:
            frequency *= ((1.0/abs(octave))/2.0)
        freq_var.set(frequency)
        final_classes.chunker(frequency)
    elif str(scale) == "Meantone":
        meantone_key = final_classes.meantoneSeries(NoteToIntervalNumber[str(key)], 528)
        frequency = meantone_key.meantoneFrequency
        if octave >= 0:
            frequency *= (octave + 1)
        else:
            frequency *= ((1.0/abs(octave))/2.0)
        freq_var.set(frequency)
        final_classes.chunker(frequency)
    elif str(scale) == "Ptolemy":
        pto_factor = final_classes.ptolemy[str(key)]
        frequency = 528 * ( float(pto_factor[0]) / float(pto_factor[1]) )
        if octave >= 0:
            frequency *= (octave + 1)
        else:
            frequency *= ((1.0/abs(octave))/2.0)
        freq_var.set(frequency)
        final_classes.chunker(frequency)

piano_label = Tk.Label(piano_frame, text='JUST Piano', font=("Courier", 18))
piano_label.grid(row=0, columnspan=10)
#frame for settings
sttngs_frame = Tk.Frame(piano_frame, pady=40, padx=20)
#sttngs_frame.pack(fill='x', side='top')
sttngs_frame.grid(row=1)

freq_frame = Tk.LabelFrame(sttngs_frame, text='Frequency',font=("MS Sans", 12))
freq_frame.grid(row=1, column=0)
freq_var = Tk.StringVar()
freq_label = Tk.Label(freq_frame, textvariable= freq_var)
freq_label.grid()

scale_var = Tk.StringVar()
scale_var.set("Pythagorean Dodecaphonic")

scales_option_menu = Tk.OptionMenu(sttngs_frame, scale_var, "Pythagorean Dodecaphonic", "Ptolemy", "Meantone", "Even-Tempered")
scales_option_menu.grid(row=0, column=4, columnspan=2, padx=(25, 0))

octave_slctr = Tk.Scale(sttngs_frame, from_=-2, to=2, label='Octave', length=200, orient='horizontal')
octave_slctr.grid(row=0, column=0, padx=(20, 0), pady=(0, 20))


keys_frame = Tk.Frame(piano_frame, padx=5)
#keys_frame.pack(fill='x', side='top')
keys_frame.grid(row=2, padx=30)

keys_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

for key in keys_list:
    key_button = Tk.Button(keys_frame, bg='#ffffff', activebackground='#ffffff', text=key, height=25, width=6,
                           command= lambda key=key: key_plyr(key, scale_var.get(), int(octave_slctr.get())))
    #key_button.grid(row=5, columnspan=2)
    key_button.pack(side='left')


###################################################################

#SCALES_SECTION#####################################################################

letter_13 = ["C","C#","D","D#","E","F","F#","G","G#","A","Bb","B","__"]
notesize = ['1/8','1/4','1/2','1']
notesbtn = []
notesizebtn = []
base = 261.63
notesz = .25

sheet = Tk.Text(scales_frame, width = 50, height = 30,fg = 'red')

tempobox = Tk.Entry(scales_frame,width=4)
tempobox.insert(Tk.INSERT,"120")

var1 = Tk.StringVar()
var1.set('4/4')
drop = Tk.OptionMenu(scales_frame,var1,'2/2','2/4','3/4','4/4','3/8','6/8','9/8','12/8')

var2 = Tk.StringVar()
var2.set('Even Tempered')
tuning = Tk.OptionMenu(scales_frame,var2,'Even Tempered','Pythagorean Tuning','Just Tuning')

var3 = Tk.StringVar()
var3.set('Violin')
instrument = Tk.OptionMenu(scales_frame,var3,'Violin','Guitar','Tanpura')

def playbtncallback():
    global var1
    timesignature = []
    notes = []
    freqnotes = []
    notesizes = []
    s = re.compile('[/]+')
    timesignature = s.split(var1.get())
    txt = sheet.get("1.0",Tk.END)
    r = re.compile('[ \t\n.0-9|+-]+')
    notes = r.split(txt)
    t = re.compile('[ \t\nA-Za-z#__|+-]+')
    notesizes = t.split(txt)
    u = re.compile('[\t\n.0-9A-Za-z#__]+')
    octaves = u.split(txt)
    noteszs = []
    for i in range(len(octaves)):
        print i
        print octaves[i]
    for i in range(1,len(notesizes)-1):
        noteszs.append(float(notesizes[i]))

    tempo = tempobox.get()
    tuningvalue = var2.get()
    instrumentvalue = var3.get()

    T = EvenTempered(base)
    if(tuningvalue == 'Pythagorean Tuning'):
        T = PythagoreanScale(base)
    if(tuningvalue == 'Just Tuning'):
        T = HarmonicSeries(base)

    instrument_filename = 'Tunes/Violin.wav'
    source_freq = 829.344
    if(instrumentvalue == 'Guitar'):
        instrument_filename = 'Tunes/guitar.wav'
        source_freq = 371.223
    elif(instrumentvalue == 'Tanpura'):
        instrument_filename = 'Tunes/tambura.wav'
        source_freq = 687.496



    o = 0
    for i in range(1,len(notes)):
        if(notes[i] != '__'):
            print notes[i]
            interval = T.get_interval_number_from_letter(notes[i])
            if(octaves[o].count('+') > 0):
                #print octaves[i].count('+')
                freqnotes.append(pow(2,octaves[o].count('+')) * T.get_frequency(interval))

            else:
                freqnotes.append(pow(2,-octaves[o].count('-')) * T.get_frequency(interval))

        else:
            freqnotes.append(0)
        o = o + 1
    play_recorded(freqnotes,tempo,timesignature[0],1.0/float(timesignature[1]),noteszs,instrument_filename,source_freq)

sum_notesize = 0.0
def btncallback(i):
    global sheet
    global notesz
    global sum_notesize
    timesignature = []
    s = re.compile('[/]+')
    timesignature = s.split(var1.get())

    sum_notesize = notesz + sum_notesize
    if (sum_notesize > float(timesignature[0]) * 1.0/float(timesignature[1])):
        sum_notesize = sum_notesize - notesz
        return
    elif (sum_notesize == float(timesignature[0]) * 1.0/float(timesignature[1])):
        sheet.insert(Tk.INSERT,"%3s%.3f   |"%(i,notesz))
        sum_notesize = 0
    else:
        sheet.insert(Tk.INSERT,"%3s%.3f   "%(i,notesz))

def notesizebtncallback(i):
    global notesz
    notesz = eval(compile(i, '<string>', 'eval', __future__.division.compiler_flag))

def measureendbtncallback():
    global sum_notesize
    timesignature = []
    s = re.compile('[/]+')
    timesignature = s.split(var1.get())
    remaining = float(timesignature[0]) * 1.0/float(timesignature[1]) - sum_notesize
    sum_notesize = 0
    sheet.insert(Tk.INSERT,"__%.3f|"%remaining)

def higheroctavebtncallback():
    sheet.insert(Tk.INSERT,"+")

def loweroctavebtncallback():
    sheet.insert(Tk.INSERT,"-")

def resetbtncallback():
    global sum_notesize
    sheet.delete('1.0',Tk.END)
    sum_notesize = 0.0

#Creating buttons
for i in range(12):
    notesbtn.append(Tk.Button(scales_frame,width = 6, text=letter_13[i],command = lambda x = letter_13[i]: btncallback(x)))
    notesbtn[-1].grid(row = i,column = 0)

for i in range(4):
    notesizebtn.append(Tk.Button(scales_frame,width = 6, text=notesize[i],command = lambda x = notesize[i]: notesizebtncallback(x)))
    notesizebtn[-1].grid(row = 13 + i,column = 0)

playbtn = Tk.Button(scales_frame,width = 6, text= "Play",command = playbtncallback)
measureendbtn = Tk.Button(scales_frame,width = 6, text= "|",command = measureendbtncallback)
higheroctavebtn = Tk.Button(scales_frame,width = 6, text= "+",command = higheroctavebtncallback)
loweroctavebtn = Tk.Button(scales_frame,width = 6, text= "-",command = loweroctavebtncallback)
resetbtn = Tk.Button(scales_frame,width = 6, text= "Reset",command = resetbtncallback)

#Create widget layout
playbtn.place(relx = .1, rely = 0)
measureendbtn.grid(row = 17,column = 0)
higheroctavebtn.grid(row = 18,column = 0)
loweroctavebtn.grid(row = 19,column = 0)
drop.place(relx = .25, rely = 0)
tuning.place(relx = .35, rely = 0)
instrument.place(relx = .55, rely = 0)
tempobox.place(relx = .2, rely = 0)
sheet.place(relx = 0.1,rely = 0.1)
resetbtn.place(relx = .1,rely = .05)


###################################################################


home_frame.pack(fill='both')


window.mainloop()



