import mido

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


def midiCallback(msg):
    if msg.type is not 'clock':
        print(msg)

def setupMidiPorts():
    # g['liveInPort'] = mido.open_input(launchpad_ports[0], callback=midiCallback)
    # g['liveOutPort'] = mido.open_output(launchpad_ports[0])
    # g['standaloneInPort'] = mido.open_input(launchpad_ports[1], callback=midiCallback)
    # g['standaloneOutPort'] = mido.open_output(launchpad_ports[1])
    g['midiInPort'] = mido.open_input(launchpad_ports[2], callback=midiCallback)
    g['midiOutPort'] = mido.open_output(launchpad_ports[2])

setupMidiPorts()

####
def octatrackCCDumpRequest():
    return mido.Message('control_change', channel=10, control=61, value=0)

####
import code
code.interact(local=locals())
