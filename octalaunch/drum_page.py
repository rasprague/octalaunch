import ui
import util
import midi
from track_page import TrackPage
from settings import settings

import mido

class DrumPage(ui.Page):
    class EventHandler(ui.EventHandler):
        def __init__(self, page):
            self.page = page
        def _noteToSlice(self, note):
            baseNote = 36
            return (note - baseNote) * 2
        def _audioTrackToNote(self):
            baseAudioTrackNote = 36
            selectedTrack = settings['drumPage']['selectedAudioTrack']
            return baseAudioTrackNote + selectedTrack
        def onNoteOn(self, msg):
            if not self.page.trackPage.midiTrackMode:
                # trigger slices
                selectedTrack = settings['drumPage']['selectedAudioTrack']
                channel = settings['trackChannels']['audioTrackChannel'][selectedTrack]
                if not channel:
                    return
                if msg.velocity == 0:
                    outMsg = mido.Message('note_off', channel=channel, note=self._audioTrackToNote(), velocity=msg.velocity)
                    midi.midiOutPort().send(outMsg)
                else:
                    outMsg = mido.Message('control_change', channel=channel, control=17, value=self._noteToSlice(msg.note))
                    midi.midiOutPort().send(outMsg)
                    util.sleep_ms(60)
                    outMsg = mido.Message('note_on', channel=channel, note=self._audioTrackToNote(), velocity=msg.velocity)
                    midi.midiOutPort().send(outMsg)
            else:
                # pass the notes through
                selectedTrack = settings['drumPage']['selectedMidiTrack']
                channel = settings['trackChannels']['audioMidiChannel'][selectedTrack]
                if not channel:
                    return
                outMsg = msg.copy(channel=channel)
                midi.midiOutPort().send(outMsg)
        def onPolytouch(self, msg):
            if self.page.trackPage.midiTrackMode:
                selectedTrack = settings['drumPage']['selectedMidiTrack']
                channel = settings['trackChannels']['audioMidiChannel'][selectedTrack]
                if not channel:
                    return
                outMsg = msg.copy(channel=channel)
                midi.midiOutPort().send(outMsg)
        def onAftertouch(self, msg):
            if self.page.trackPage.midiTrackMode:
                selectedTrack = settings['drumPage']['selectedMidiTrack']
                channel = settings['trackChannels']['audioMidiChannel'][selectedTrack]
                if not channel:
                    return
                outMsg = msg.copy(channel=channel)
                midi.midiOutPort().send(outMsg)
        def onCC(self, msg):
            self.page.trackPage.eventHandler.onCC(msg)
                
    def __init__(self):
        self.trackPage = TrackPage('drumPage')
        self.eventHandler = self.EventHandler(self)
    
    def uiDraw(self):
        self.trackPage.uiDraw()