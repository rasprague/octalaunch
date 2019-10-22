# Octalaunch
Get your Launchpad Pro playing the Octatrack

The Octrack from Elektron is a fine piece of music gear, able to handle anything from sample playing and chopping, to audio mixing and mangling, and much more. However, playing it like an instrument isn't so fun. Its 16 trigger buttons, layed out in a single row, is cumbersome to play on. Banging out beats with sample slices doesn't feel quite right, and playing melodic sample chromaitcally is unituitive. Also, its MIDI implementation is a bit strange in parts.

Enter the Launchpad from Novation. The Launchpad is a MIDI controller featuring an 8x8 grid of light-up drum pads. It's a playable surface that looks great and feels great. The Pro model adds velocity sensitivity; aftertouch; a slick note scale mode; standalone Note, Drum, and Fader modes (no Ableton Live needed); and hardware MIDI ports on the back. What it doesn't do is allow for any customizing of the MIDI notes or CCs it sends.

That's where Octalauch comes in. Octalauch sits between the Lauchpad Pro and the Octatack, utilizing the Launchpad's standalone modes, and translates between the two. Note mode restricts the notes played to the range the Octatack can understand (no more mistakenly muting tracks, arming track, or starting/stopping the sequencer). Drum mode triggers sample slices MPC style. Fader mode controls the volume of each Audio track.

# Goals
Initial aims for Octalaunch is to improve upon the plaabliity of the Octatrack. I'm focusing efforts on areas the Octatrack doesn't do so well, e.g. playing chromatically, triggering sample slices, and controlling track volumes in one place. Functions it already does well I won't be focusing on, e.g. track muting, track parameters, freeze delay, etc.

# Gear setup
Plug the Lauchpad Pro to the computer running Octalauch via USB. Harware MIDI out from the Lauchpad Pro plugs into the MIDI port on the Octatrack.

As for Lauchpad Pro settings, for each of the standalone Note, Drum, and Fader modes, disable MIDI out and set the MIDI channel to the autochannel (the default is channel 11)

# How to use
** Coming soon **

# The future
* Fully custom layouts that don't rely on the standalone modes (e.g. our own Live mode)
* support for other grooveboxes / hardware setups
* Single-board computer (e.g. Raspberry Pi) support and testing

# Dependencies
mido - MIDI Objects for Python https://mido.readthedocs.io
rtmidi - Cross platform realtime MIDI i/o https://pypi.org/project/python-rtmidi/

Elektron Octatrack - https://www.elektron.se/products/octatrack-mkii/
Novation Launchpad Pro - https://novationmusic.com/launch/launchpad-pro
