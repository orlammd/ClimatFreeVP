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
		1:	SceneGroup("Intro-Items", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),
		2:	SceneGroup("Baby-Malabar", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),
		3:	SceneGroup("Noomi-Bhopal", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),

		4:	SceneGroup("BurnHBurn", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),

		5:	SceneGroup("Barracuda-UltraPo", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),

		6:	SceneGroup("63521-Surpiqure", [
					Scene("On Air",
						PortFilter('NanoIn') >> Discard()
					),
					Scene("Bank Select", 
						PortFilter('NanoIn') >> Discard() 
					),
				]
			),
	},
)

