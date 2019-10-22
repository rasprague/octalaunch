import ui
import mido

autochannel = 10

g = {
    'liveOutPort': None,
    'liveInPort': None,
    'standaloneOutPort': None,
    'standaloneInPort': None,
    'midiOutPort': None,
    'midiInPort': None
}

def midiOutPort():
    return g['midiOutPort']
    
def standaloneOutPort():
    return g['standaloneOutPort']

def liveOutPort():
    return g['liveOutPort']

def setupMidiPorts():
    g['liveInPort'] = mido.open_input(u'Launchpad Pro Live Port', callback=midiInCallback)
    g['liveOutPort'] = mido.open_output(u'Launchpad Pro Live Port')
    g['standaloneInPort'] = mido.open_input(u'Launchpad Pro Standalone Port', callback=midiInCallback)
    g['standaloneOutPort'] = mido.open_output(u'Launchpad Pro Standalone Port')
    g['midiInPort'] = mido.open_input(u'Launchpad Pro MIDI Port', callback=midiInCallback)
    g['midiOutPort'] = mido.open_output(u'Launchpad Pro MIDI Port')

def midiInCallback(msg):
    if msg.type == 'sysex':
        if msg.data[0:5] == (0, 32, 41, 2, 16):
            # launchpad sysex
            data = msg.data[5:]
            if data[0] == 45:
                # mode status
                # 0 = live, 1 = standalone
                if data[1] == 0:
                    ui.modeChangeHandler().onLive()
            elif data[0] == 46:
                # live layout status
                # 0 = session, 1 = drum rack, 2 = chromatic note, 3 = user (drum)
                # 4 = audio (blank), 5 = fader, 6 = record arm (session), 7 = track select (session)
                # 8 = mute (session), 9 = solo (session), 10 = volume (fader), 11 = pad (fader)
                # 12 = sends (fader), 13 = stop clip (session)
                pass
            elif data[0] == 47:
                # standalone layout status
                # 0 = note, 1 = drum, 2 = fader, 3 = programmer
                if data[1] == 0:
                    # note
                    ui.modeChangeHandler().onNote()
                elif data[1] == 1:
                    # drum
                    ui.modeChangeHandler().onDrum()
                elif data[1] == 2:
                    # fader
                    ui.modeChangeHandler().onFader()
                elif data[1] == 3:
                    # programmer
                    ui.modeChangeHandler().onProgrammer()
    else:
        # print(msg)
        ui.midiHandler().onMsg(msg)