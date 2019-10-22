import ui
import midi
from settings import settings
import mido

class _TrackSelectPage(ui.Page):
    class TrackSelectEventHandler(ui.EventHandler):
        def __init__(self, page):
            self.page = page
        def onCC(self, msg):
            # midi mode toggle
            if msg.control == 98:
                if msg.value == 127:
                    self.page.parentPage.midiTrackMode = not self.page.parentPage.midiTrackMode
                self.page.parentPage.uiDraw()
            # track select
            elif msg.control in self.page.trackButtons:
                if self.page.parentPage.midiTrackMode:
                    settings[self.page.pageSettingsKey]['selectedMidiTrack'] = self.page.trackButtons.index(msg.control)
                else:
                    settings[self.page.pageSettingsKey]['selectedAudioTrack'] = self.page.trackButtons.index(msg.control)
                self.page.parentPage.uiDraw()
    def __init__(self, parentPage, pageSettingsKey):
        self.parentPage = parentPage
        self.pageSettingsKey = pageSettingsKey
        self.trackButtons = [1, 2, 3, 4, 5, 6, 7, 8]
        self.eventHandler = self.TrackSelectEventHandler(self)
    def uiDraw(self):
        # draw midi mode toggle
        color = None
        if self.parentPage.midiTrackMode:
            color = 9
        else:
            color = 5
        outMsg = mido.Message('control_change', channel=midi.autochannel, control=98, value=color)
        midi.standaloneOutPort().send(outMsg)

        # draw selected track
        selectedTrack = None
        hightlightColor = None
        if self.parentPage.midiTrackMode:
            selectedTrack = settings[self.pageSettingsKey]['selectedMidiTrack']
            hightlightColor = 9
        else:
            selectedTrack = settings[self.pageSettingsKey]['selectedAudioTrack']
            hightlightColor = 5
        for i in range(len(self.trackButtons)):
            color = hightlightColor if i == selectedTrack else 0
            outMsg = mido.Message('control_change', channel=midi.autochannel, control=self.trackButtons[i], value=color)
            midi.standaloneOutPort().send(outMsg)

class _MidiChannelPage(ui.Page):
    class MidiChannelEventHandler(ui.EventHandler):
        def __init__(self, page):
            self.page = page
        def onCC(self, msg):
            # shift to midi settings mode
            # use button 97 as settings shift button
            if msg.control == 97:
                if msg.value == 0:
                    self.page.parentPage.midiChannelSettingsMode = False
                elif msg.value == 127:
                    self.page.parentPage.midiChannelSettingsMode = True
                self.page.parentPage.uiDraw()
            # clear midi channel for track
            if self.page.parentPage.midiChannelSettingsMode:
                if msg.control == 96:
                    if msg.value == 127:
                        if self.page.parentPage.midiTrackMode:
                            track = settings[self.page.pageSettingsKey]['selectedMidiTrack']
                            settings['trackChannels']['midiTrackChannel'][track] = None
                        else:
                            track = settings[self.page.pageSettingsKey]['selectedAudioTrack']
                            settings['trackChannels']['audioTrackChannel'][track] = None
                # set midi channel for track
                elif msg.control in self.page.midiChannelButtons:
                    if msg.value == 127:
                        if self.page.parentPage.midiTrackMode:
                            track = settings[self.page.pageSettingsKey]['selectedMidiTrack']
                            channel = self.page.midiChannelButtons.index(msg.control)
                            settings['trackChannels']['midiTrackChannel'][track] = channel
                        else:
                            track = settings[self.page.pageSettingsKey]['selectedAudioTrack']
                            channel = self.page.midiChannelButtons.index(msg.control)
                            settings['trackChannels']['audioTrackChannel'][track] = channel
                self.page.parentPage.uiDraw()
    def __init__(self, parentPage, pageSettingsKey):
        self.parentPage = parentPage
        self.pageSettingsKey = pageSettingsKey
        self.midiChannelButtons = [80, 70, 60, 50, 40, 30, 20, 10, 89, 79, 69, 59, 49, 39, 29, 19]
        self.eventHandler = self.MidiChannelEventHandler(self)
    def uiDraw(self):
        # draw settings shift
        color = None
        if self.parentPage.midiChannelSettingsMode:
            color = 3
        else:
            color = 4
        outMsg = mido.Message('control_change', channel=midi.autochannel, control=97, value=color)
        midi.standaloneOutPort().send(outMsg)
        
        if self.parentPage.midiChannelSettingsMode:
            # draw channel clear button
            color = 45
            outMsg = mido.Message('control_change', channel=midi.autochannel, control=96, value=color)
            midi.standaloneOutPort().send(outMsg)
            # draw channel for selected track
            selectedTrack = None
            channel = None
            hightlightColor = None
            if self.parentPage.midiTrackMode:
                selectedTrack = settings[self.pageSettingsKey]['selectedMidiTrack']
                channel = settings['trackChannels']['midiTrackChannel'][selectedTrack]
                hightlightColor = 9
            else:
                selectedTrack = settings[self.pageSettingsKey]['selectedAudioTrack']
                channel = settings['trackChannels']['audioTrackChannel'][selectedTrack]
                hightlightColor = 5
            for i in range(len(self.midiChannelButtons)):
                color = None
                if i == channel:
                    color = hightlightColor
                else:
                    color = 0
                outMsg = mido.Message('control_change', channel=midi.autochannel, control=self.midiChannelButtons[i], value=color)
                midi.standaloneOutPort().send(outMsg)
        else:
            # clear
            for button in self.midiChannelButtons + [96]:
                color = 0
                outMsg = mido.Message('control_change', channel=midi.autochannel, control=button, value=color)
                midi.standaloneOutPort().send(outMsg)

class TrackPage(object):
    class TrackEventHandler(ui.EventHandler):
        def __init__(self, page):
            self.page = page
        def onCC(self, msg):
            self.page.trackSelectPage.eventHandler.onCC(msg)
            self.page.midiChannelPage.eventHandler.onCC(msg)
                
    def __init__(self, pageSettingsKey):
        self.midiTrackMode = False
        self.midiChannelSettingsMode = False
        self.trackSelectPage = _TrackSelectPage(self, pageSettingsKey)
        self.midiChannelPage = _MidiChannelPage(self, pageSettingsKey)
        self.eventHandler = self.TrackEventHandler(self)
    def uiDraw(self):
        self.trackSelectPage.uiDraw()
        self.midiChannelPage.uiDraw()