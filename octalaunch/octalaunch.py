#!/usr/bin/env python

import sys

try:
    import lauchpad_rtmidi as launchpad
except ImportError:
    try:
        import launchpad_py as launchpad
    except ImportError:
        sys.exit('error loading launchpad.py')

import ui
import octatrack_pages
import settings
import util
import midi

import mido

g = {
    'lp': None,
}

def setupLaunchpad():
    lp = launchpad.LaunchpadPro()
    lp.Open(0, 'pro')
    lp.Reset()
    lp.ButtonFlush()
    
    g['lp'] = lp

def triggerOctatackMidiDump():
    outMsg = mido.Message('control_change', channel=midi.autochannel, control=61, value=0)
    midi.midiOutPort().send(outMsg)
    
def gotoSavedSelectedPage():
    # launchpad sysex 'header'
    headerMsg = mido.Message('sysex', data=(0, 32, 41, 2, 16))

    page = settings.settings['selectedPage']
    if page == 'live':
        outMsg = headerMsg.copy()
        outMsg.data += (33, 0)
        midi.liveOutPort().send(outMsg)
    else:
        outMsg = headerMsg.copy()
        outMsg.data += (33, 1)
        midi.liveOutPort().send(outMsg)
        outMsg = headerMsg.copy()
        if page == 'note':
            outMsg.data += (44, 0)
        elif page == 'drum':
            outMsg.data += (44, 1)
        elif page == 'fader':
            outMsg.data += (44, 2)
        elif page == 'programmer':
            outMsg.data += (44, 3)
        midi.standaloneOutPort().send(outMsg)

def main():
    settings.load()
    midi.setupMidiPorts()
    octatrack_pages.setup()
    setupLaunchpad()
    triggerOctatackMidiDump()
    gotoSavedSelectedPage()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        print('\n')
        print('save settings . . .')
        settings.save()
        print('exit.')

if __name__ == '__main__':
    main()
