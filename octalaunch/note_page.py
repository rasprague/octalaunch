import ui
import midi
from track_page import TrackPage
from settings import settings

import mido

class NotePage(ui.Page):
    class NoteEventHandler(ui.EventHandler):
        def __init__(self, page):
            self.page = page
        def _trackToChannel(self):
            if self.page.trackPage.midiTrackMode:
                return settings['trackChannels']['midiTrackChannel'][settings['notePage']['selectedMidiTrack']]
            else:
                return settings['trackChannels']['audioTrackChannel'][settings['notePage']['selectedAudioTrack']]
        def _noteOutOfRange(self, note):
            if not self.page.trackPage.midiTrackMode:
                if note < 72 or note > 96:
                    return True
            return False
        def onNoteOn(self, port, msg):
            if self._noteOutOfRange(msg.note):
                return
            channel = self._trackToChannel()
            if channel is None:
                return
            outMsg = msg.copy(channel=channel)
            midi.midiOutPort().send(outMsg)
        def onPolyTouch(self, port, msg):
            if self._noteOutOfRange(msg.note):
                return
            channel = self._trackToChannel()
            if channel is None:
                return
            outMsg = msg.copy(channel=channel)
            midi.midiOutPort().send(outMsg)
        def onAftertouch(self, port, msg):
            channel = self._trackToChannel()
            if channel is None:
                return
            outMsg = msg.copy(channel=channel)
            midi.midiOutPort().send(outMsg)
        def onCC(self, port, msg):
            self.page.trackPage.eventHandler.onCC(msg)
    def __init__(self):
        self.trackPage = TrackPage('notePage')
        self.eventHandler = self.NoteEventHandler(self)
    def uiDraw(self):
        self.trackPage.uiDraw()