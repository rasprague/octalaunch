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
    if msg.type is 'clock':
        return
    elif msg.type is 'sysex':
        h = []
        for b in msg.data:
            h.append(hex(b))
        print('sysex [%s]' % ' '.join(h))
    else:
        print(msg)

def setupMidiPorts():
    # g['liveInPort'] = mido.open_input(launchpad_ports[0], callback=midiCallback)
    # g['liveOutPort'] = mido.open_output(launchpad_ports[0])
    # g['standaloneInPort'] = mido.open_input(launchpad_ports[1], callback=midiCallback)
    # g['standaloneOutPort'] = mido.open_output(launchpad_ports[1])
    #g['midiInPort'] = mido.open_input(launchpad_ports[2], callback=midiCallback)
    #g['midiOutPort'] = mido.open_output(launchpad_ports[2])
    g['opzInPort'] = mido.open_input('OP-Z MIDI 1', callback=midiCallback)
    g['opzOutPort'] = mido.open_output('OP-Z MIDI 1')

setupMidiPorts()

####
def octatrackCCDumpRequest():
    return mido.Message('control_change', channel=10, control=61, value=0)

def octatrackCCDump():
    midiOutPort().send(octatrackCCDumpRequest())
####
def opzStatusRequest():
    # msg = mido.Message('sysex', data=[0x00, 0x20, 0x76, 0x01, 0x00, 0x03, 0x2D, 0x0E, 0x05])
    msg = mido.Message('sysex', data=[0x00, 0x20, 0x76, 0x01, 0x00, 0x01, 0x4E, 0x2E, 0x06])
    g['opzOutPort'].send(msg)

####

import code
code.interact(local=locals())
