import ui
import util

from settings import settings

import note_page
import drum_page
import fader_page

g = {
    'currentPage': None,
    'livePage': None,
    'notePage': None,
    'drumPage': None,
    'faderPage': None,
    'programmerPage': None
}

def livePage():
    return g['livePage']

def notePage():
    return g['notePage']

def drumPage():
    return g['drumPage']

def faderPage():
    return g['faderPage']

def programmerPage():
    return g['programmerPage']

def setCurrentPage(newPage):
    g['currentPage'] = newPage
    util.sleep_ms(100)
    newPage.uiDraw()

class LivePage(ui.Page):
    pass

class ProgrammerPage(ui.Page):
    pass

class ModeChangeHandler(ui.ModeChangeHandler):
    def onLive(self):
        setCurrentPage(livePage())
        settings['selectedPage'] = 'live'
    def onNote(self):
        setCurrentPage(notePage())
        settings['selectedPage'] = 'note'
    def onDrum(self):
        setCurrentPage(drumPage())
        settings['selectedPage'] = 'drum'
    def onFader(self):
        setCurrentPage(faderPage())
        settings['selectedPage'] = 'fader'
    def onProgrammer(self):
        setCurrentPage(programmerPage())
        settings['selectedPage'] = 'programmer'
    
class MidiHandler(ui.MidiHandler):
    def onMsg(self, port, msg):
        g['currentPage'].onMsg(port, msg)

def setup():
    g['currentPage'] = None
    g['livePage'] = LivePage()
    g['notePage'] = note_page.NotePage()
    g['drumPage'] = drum_page.DrumPage()
    g['faderPage'] = fader_page.FaderPage()
    g['programmerPage'] = ProgrammerPage()
    ui.setup(modeChangeHandler=ModeChangeHandler(), midiHandler=MidiHandler())