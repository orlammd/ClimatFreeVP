from mididings import Call
import mididings.engine as _engine
import mididings.setup as _setup
import mididings.misc as _misc

import mididings.extra.panic as _panic

import liblo as _liblo

class OSCCustomInterface(object):
    def __init__(self, port=56418):
        self.port = port

    def on_start(self):
        if self.port is not None:
            self.server = _liblo.ServerThread(self.port)
            self.server.register_methods(self)
            self.server.start()

    def on_exit(self):
        if self.port is not None:
            self.server.stop()
            del self.server

    @_liblo.make_method('/pedalBoard/button', 'i')
    def button_cb(self, path, args):
	if args[0] == 12:
	    _engine.switch_subscene(2)
	if args[0] == 11:
            _liblo.send(9999, '/video/freeze/toggle')
	if _engine.current_subscene() == 2:
	    _engine.switch_scene(args[0])
	    _engine.switch_subscene(1)
	if _engine.current_subscene() == 1:
    	    if args[0] < 7: # Desactivation des boutons 7, 8, 9, 10
	        clip_number = args[0] + (_engine.current_scene()-1)*6
                _liblo.send(9999, '/clip/select', clip_number)
                _liblo.send(9999, '/clip/goto', 1)

