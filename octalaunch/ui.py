g = {
    'modeChangeHandler': None,
    'midiHandler': None
}

def modeChangeHandler():
    return g['modeChangeHandler']

def midiHandler():
    return g['midiHandler']

def setup(modeChangeHandler, midiHandler):
    g['modeChangeHandler'] = modeChangeHandler
    g['midiHandler'] = midiHandler

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
    def onMsg(self, port, msg):
        pass

class EventHandler(object):
    def onNoteOn(self, port, msg):
        pass
    def onPolytouch(self, port, msg):
        pass
    def onAftertouch(self, port, msg):
        pass
    def onCC(self, port, msg):
        pass

class Page(object):
    def __init__(self):
        self.eventHandler = None
    def uiClear(self):
        pass
    def uiDraw(self):
        pass
    def onMsg(self, port, msg):
        if msg.type == 'note_on':
            self.eventHandler.onNoteOn(port, msg)
        elif msg.type == 'polytouch':
            self.eventHandler.onPolytouch(port, msg)
        elif msg.type == 'aftertouch':
            self.eventHandler.onAftertouch(port, msg)
        elif msg.type == 'control_change':
            self.eventHandler.onCC(port, msg)
