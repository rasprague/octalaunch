# Octalaunch
Get your Launchpad Pro playing the Octatrack

## tl;dr
Hook up a Launchpad Pro to an Octatrack. Use its excellent Note mode to play samples chromaticaly, its Drum mode to play sample slices MPC style, and its Fader mode to view and change track levels from one place.

## The long version
The Octrack from Elektron is a fine piece of music gear, able to handle anything from sample playing and chopping, to audio mixing and mangling, and much more. However, playing it like an instrument isn't so fun. Its 16 trigger buttons, layed out in a single row, is cumbersome to play on. Banging out beats with sample slices doesn't feel quite right, and playing melodic sample chromatically is unintuitive. Also, its MIDI implementation is a bit strange in parts.

Enter the Launchpad from Novation. The Launchpad is a MIDI controller featuring an 8x8 grid of light-up drum pads. It's a playable surface that looks great and feels great. The Pro model adds velocity sensitivity; aftertouch; a slick note scale mode; standalone Note, Drum, and Fader modes (no Ableton Live needed); and hardware MIDI ports on the back. What it doesn't do is allow for any customizing of the MIDI notes or CCs it sends.

That's where Octalaunch comes in. Octalaunch sits between the Launchpad Pro and the Octatack, utilizing the Launchpad's standalone modes, and translates between the two. Note mode restricts the notes played to the range the Octatack can understand (no more mistakenly muting tracks, arming tracks, or starting/stopping the sequencer). Drum mode triggers sample slices MPC style. Fader mode controls the volume of each Audio track.

## Goals
The initial aim for Octalaunch is to improve upon the playability of the Octatrack. I'm focusing efforts on areas the Octatrack doesn't do so well, e.g. playing chromatically, triggering sample slices, controlling track volumes in one place, etc. Functions it already does well I won't be focusing on, e.g. track muting, track parameters, freeze delay, etc.

## Gear setup
Plug the Launchpad Pro into the computer running Octalaunch via USB. Hardware MIDI out from the Launchpad Pro plugs into the MIDI in port on the Octatrack; hardware MIDI in from the Launchpad Pro plugs into the MIDI out port of the Octatrack.

For Launchpad Pro settings, for each of the standalone Note, Drum, and Fader modes, disable MIDI out and set the MIDI channel to the autochannel (the default is channel 11). See "Setup Page Options" in the Launchpad Pro manual.

## How to use
** Coming soon **

## The future
* Fully custom layouts that don't rely on the standalone modes (e.g. our own Live mode)
* Support for other Launchpad models
* Support for other grooveboxes / hardware setups
* Single-board computer support and testing (e.g. Raspberry Pi)

### Dependencies
* mido - MIDI Objects for Python https://mido.readthedocs.io
* rtmidi - Cross platform realtime MIDI i/o https://pypi.org/project/python-rtmidi/

### Links
* Elektron Octatrack - https://www.elektron.se/products/octatrack-mkii/
* Novation Launchpad Pro - https://novationmusic.com/launch/launchpad-pro
