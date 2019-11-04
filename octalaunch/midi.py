import ui
import mido

autochannel = 10

# macos
# launchpad_ports = [
#     u'Launchpad Pro Live Port',
#     u'Launchpad Pro Standalone Port',
#     u'Launchpad Pro MIDI Port'
# ]

# ubuntu
launchpad_ports = [
    u'Launchpad Pro MIDI 1',
    u'Launchpad Pro MIDI 2',
    u'Launchpad Pro MIDI 3'
]

g = {
    'liveOutPort': None,
    'liveInPort': None,
    'standaloneOutPort': None,
    'standaloneInPort': None,
    'midiOutPort': None,
    'midiInPort': None
}

def liveOutPort():
    return g['liveOutPort']

def liveInPort():
    return g['liveInPort']

def standaloneOutPort():
    return g['standaloneOutPort']

def standaloneInPort():
    return g['standaloneInPort']

def midiOutPort():
    return g['midiOutPort']

def midiInPort():
    return g['midiInPort']


def setupMidiPorts():
    g['liveInPort'] = mido.open_input(launchpad_ports[0], callback=liveInPortCallback)
    g['liveOutPort'] = mido.open_output(launchpad_ports[0])
    g['standaloneInPort'] = mido.open_input(launchpad_ports[1], callback=standaloneInPortCallback)
    g['standaloneOutPort'] = mido.open_output(launchpad_ports[1])
    g['midiInPort'] = mido.open_input(launchpad_ports[2], callback=midiInPortCallback)
    g['midiOutPort'] = mido.open_output(launchpad_ports[2])

def liveInPortCallback(msg):
    midiCallback(g['liveInPort'], msg)

def standaloneInPortCallback(msg):
    midiCallback(g['standaloneInPort'], msg)

def midiInPortCallback(msg):
    midiCallback(g['midiInPort'], msg)
    pass

def midiCallback(port, msg):
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
        ui.midiHandler().onMsg(port, msg)