g = {
    'modeChangeHandler': None,
    'midiHandler': None
}

def modeChangeHandler():
    return g['modeChangeHandler']

def midiHandler():
    return g['midiHandler']

class ModeChangeHandler(object):
    def onLive(self):
        pass
    def onNote(self):
        pass
    def onDrum(self):
        pass
    def onFader(self):
        pass
    def onProgrammer(self):
        pass

class MidiHandler(object):
    def onMsg(self, msg):
        pass

class EventHandler(object):
    def onNoteOn(self, msg):
        pass
    def onPolytouch(self, msg):
        pass
    def onAftertouch(self, msg):
        pass
    def onCC(self, msg):
        pass

class Page(object):
    def __init__(self):
        self.eventHandler = None
    def uiClear(self):
        pass
    def uiDraw(self):
        pass
    def onMsg(self, msg):
        if msg.type == 'note_on':
            self.eventHandler.onNoteOn(msg)
        elif msg.type == 'polytouch':
            self.eventHandler.onPolytouch(msg)
        elif msg.type == 'aftertouch':
            self.eventHandler.onAftertouch(msg)
        elif msg.type == 'control_change':
            self.eventHandler.onCC(msg)
    