import ui
from settings import settings
import midi
import mido

class FaderPage(ui.Page):
    class EventHandler(ui.EventHandler):
        def onCC(self, port, msg):
            if msg.control >= 21 and msg.control <= 28:
                track = msg.control - 21
                channel = settings['trackChannels']['audioTrackChannel'][track]
                if not channel:
                    return
                levelControl = 7
                outMsg = mido.Message('control_change', channel=channel, control=levelControl, value=msg.value)
                #volumeControl = 25
                #outMsg = mido.Message('control_change', channel=channel, control=volumeControl, value=msg.value)
                midi.midiOutPort().send(outMsg)
    def __init__(self):
        self.eventHandler = self.EventHandler()