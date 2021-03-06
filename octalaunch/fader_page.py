import ui
from settings import settings
import midi
import mido

class FaderPage(ui.Page):
    class EventHandler(ui.EventHandler):
        def __init__(self, page):
            self.page = page
        def onCC(self, port, msg):
            levelControl = 46
            volumeControl = 25
            trackMute = 49

            if port == midi.standaloneInPort():
                if msg.control >= 21 and msg.control <= 28:
                    track = msg.control - 21
                    channel = settings['trackChannels']['audioTrackChannel'][track]
                    if channel is None:
                        return
                    outMsg = mido.Message('control_change', channel=channel, control=levelControl, value=msg.value)
                    #outMsg = mido.Message('control_change', channel=channel, control=volumeControl, value=msg.value)
                    midi.midiOutPort().send(outMsg)
                elif msg.control in self.page.trackButtons:
                    if msg.value == 127:
                        track = msg.control - 1
                        channel = settings['trackChannels']['audioTrackChannel'][track]
                        self.page.muted[track] = not self.page.muted[track]
                        value = None
                        if self.page.muted[track]:
                            value = 127
                        else:
                            value = 0
                        outMsg = mido.Message('control_change', channel=channel, control=trackMute, value=value)
                        midi.midiOutPort().send(outMsg)
                    self.page.uiDraw()
            elif port == midi.midiInPort():
                if msg.control == levelControl:
                    channel = msg.channel
                    value = msg.value
                    # send midi cc to standalone port to light up fader value
                    outMsg = mido.Message('control_change', channel=midi.autochannel, control=channel+21, value=value)
                    midi.standaloneOutPort().send(outMsg)
                elif msg.control == trackMute:
                    channel = msg.channel
                    muted = (msg.value != 0)
                    track = settings['trackChannels']['audioTrackChannel'].index(channel)
                    self.page.muted[track] = muted
                    self.page.uiDraw()
                    
    def __init__(self):
        self.trackButtons = [1, 2, 3, 4, 5, 6, 7, 8]
        self.muted = [False, False, False, False, False, False, False, False]
        self.eventHandler = self.EventHandler(self)
    def uiDraw(self):
        for track in range(len(self.trackButtons)):
            color = None
            if self.muted[track]:
                color = 0
            else:
                color = 5
            outMsg = mido.Message('control_change', channel=midi.autochannel, control=self.trackButtons[track], value=color)
            midi.standaloneOutPort().send(outMsg)