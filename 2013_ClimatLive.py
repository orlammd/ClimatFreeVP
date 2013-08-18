# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from customosc import OSCCustomInterface

config(
	backend='alsa',
	client_name='OSCRouter',
	out_ports=['CtrlOut'],
	in_ports=['NanoIn']
)

hook(
    OSCInterface(56422, 56423),
    AutoRestart(),
    OSCCustomInterface(56418)
)


#### Actions #################################################
run(
	scenes = {
# TU COPIES A PARTIR DE LA
		1:	SceneGroup("Bab Safe", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),
# JUSQUE LA, ET TU CHANGES LE NOM DE SceneGroup ET LE NUMERO
		2:	SceneGroup("63521", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),
# TU COLLES ICI
	},
)

