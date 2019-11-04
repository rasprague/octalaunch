import ui
from settings import settings
import midi
import mido

class FaderPage(ui.Page):
    class EventHandler(ui.EventHandler):
        def onCC(self, port, msg):
            levelControl = 46
            #volumeControl = 25
            if port == midi.standaloneInPort():
                if msg.control >= 21 and msg.control <= 28:
                    track = msg.control - 21
                    channel = settings['trackChannels']['audioTrackChannel'][track]
                    if channel is None:
                        return
                    
                    outMsg = mido.Message('control_change', channel=channel, control=levelControl, value=msg.value)
                    #outMsg = mido.Message('control_change', channel=channel, control=volumeControl, value=msg.value)
                    midi.midiOutPort().send(outMsg)
            elif port == midi.midiInPort():
                if msg.control == levelControl:
                    channel = msg.channel
                    value = msg.value
                    # send midi cc to standalone port to light up fader value
                    outMsg = mido.Message('control_change', channel=midi.autochannel, control=channel+21, value=value)
                    midi.standaloneOutPort().send(outMsg)
    def __init__(self):
        self.eventHandler = self.EventHandler()