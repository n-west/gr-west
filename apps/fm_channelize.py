#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: FM whole-band Channelizer
# Author: Nathan West
# Generated: Wed Oct 29 14:47:15 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sys

from distutils.version import StrictVersion
class fm_channelize(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FM whole-band Channelizer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FM whole-band Channelizer")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fm_channelize")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3.125e6
        self.gain = gain = 25
        self.pfb_transition_width = pfb_transition_width = 120e3
        self.pfb_samp_rate = pfb_samp_rate = samp_rate
        self.pfb_gain = pfb_gain = 1
        self.pfb_cutoff_freq = pfb_cutoff_freq = 80e3
        self.pfb_attenuation = pfb_attenuation = 60
        self.audio_transition_width = audio_transition_width = 3e3/10
        self.audio_samp_rate = audio_samp_rate = 44.1e3
        self.audio_gain = audio_gain = gain
        self.audio_cutoff_freq = audio_cutoff_freq = 18e3/10
        self.audio_attenuation = audio_attenuation = 80
        self.pfb_taps = pfb_taps = firdes.low_pass_2(pfb_gain, pfb_samp_rate, pfb_cutoff_freq, pfb_transition_width, pfb_attenuation)
        self.audio_taps = audio_taps = firdes.low_pass_2(audio_gain, audio_samp_rate, audio_cutoff_freq, audio_transition_width, audio_attenuation)
        self.pfb_ntaps = pfb_ntaps = pfb_taps.__len__()
        self.channel = channel = 0
        self.audio_rate = audio_rate = 44.1e3
        self.audio_ntaps = audio_ntaps = audio_taps.__len__()

        ##################################################
        # Blocks
        ##################################################
        self._channel_layout = Qt.QVBoxLayout()
        self._channel_tool_bar = Qt.QToolBar(self)
        self._channel_layout.addWidget(self._channel_tool_bar)
        self._channel_tool_bar.addWidget(Qt.QLabel("fm channel"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._channel_counter = qwt_counter_pyslot()
        self._channel_counter.setRange(0, 125, 1)
        self._channel_counter.setNumButtons(2)
        self._channel_counter.setValue(self.channel)
        self._channel_tool_bar.addWidget(self._channel_counter)
        self._channel_counter.valueChanged.connect(self.set_channel)
        self._channel_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._channel_slider.setRange(0, 125, 1)
        self._channel_slider.setValue(self.channel)
        self._channel_slider.setMinimumWidth(125)
        self._channel_slider.valueChanged.connect(self.set_channel)
        self._channel_layout.addWidget(self._channel_slider)
        self.top_layout.addLayout(self._channel_layout)
        self.pfb_decimator_ccf_0 = pfb.decimator_ccf(
        	  15,
        	  (pfb_taps),
        	  channel,
        	  100,
                  True,
                  True)
        self.pfb_decimator_ccf_0.declare_sample_delay(0)
        	
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_fff(
        	   audio_rate / 50e3,
                  taps=(audio_taps),
        	  flt_size=10)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self._gain_layout = Qt.QVBoxLayout()
        self._gain_tool_bar = Qt.QToolBar(self)
        self._gain_layout.addWidget(self._gain_tool_bar)
        self._gain_tool_bar.addWidget(Qt.QLabel("Gain"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._gain_counter = qwt_counter_pyslot()
        self._gain_counter.setRange(0, 100, 1)
        self._gain_counter.setNumButtons(2)
        self._gain_counter.setValue(self.gain)
        self._gain_tool_bar.addWidget(self._gain_counter)
        self._gain_counter.valueChanged.connect(self.set_gain)
        self._gain_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._gain_slider.setRange(0, 100, 1)
        self._gain_slider.setValue(self.gain)
        self._gain_slider.setMinimumWidth(200)
        self._gain_slider.valueChanged.connect(self.set_gain)
        self._gain_layout.addWidget(self._gain_slider)
        self.top_layout.addLayout(self._gain_layout)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/nathan/Downloads/WFM-97.9MHz-3.125Msps.dat", True)
        self.audio_sink_0 = audio.sink(int(audio_rate), "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=200e3,
        	audio_decimation=int(200e3 / audio_rate),
        )
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=audio_rate, tau=75e-6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.pfb_decimator_ccf_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.pfb_decimator_ccf_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.analog_fm_deemph_0, 0))
        self.connect((self.analog_fm_deemph_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_fm_deemph_0, 0), (self.blocks_null_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_channelize")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_pfb_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_audio_gain(self.gain)
        Qt.QMetaObject.invokeMethod(self._gain_counter, "setValue", Qt.Q_ARG("double", self.gain))
        Qt.QMetaObject.invokeMethod(self._gain_slider, "setValue", Qt.Q_ARG("double", self.gain))

    def get_pfb_transition_width(self):
        return self.pfb_transition_width

    def set_pfb_transition_width(self, pfb_transition_width):
        self.pfb_transition_width = pfb_transition_width
        self.set_pfb_taps(firdes.low_pass_2(self.pfb_gain, self.pfb_samp_rate, self.pfb_cutoff_freq, self.pfb_transition_width, self.pfb_attenuation))

    def get_pfb_samp_rate(self):
        return self.pfb_samp_rate

    def set_pfb_samp_rate(self, pfb_samp_rate):
        self.pfb_samp_rate = pfb_samp_rate
        self.set_pfb_taps(firdes.low_pass_2(self.pfb_gain, self.pfb_samp_rate, self.pfb_cutoff_freq, self.pfb_transition_width, self.pfb_attenuation))

    def get_pfb_gain(self):
        return self.pfb_gain

    def set_pfb_gain(self, pfb_gain):
        self.pfb_gain = pfb_gain
        self.set_pfb_taps(firdes.low_pass_2(self.pfb_gain, self.pfb_samp_rate, self.pfb_cutoff_freq, self.pfb_transition_width, self.pfb_attenuation))

    def get_pfb_cutoff_freq(self):
        return self.pfb_cutoff_freq

    def set_pfb_cutoff_freq(self, pfb_cutoff_freq):
        self.pfb_cutoff_freq = pfb_cutoff_freq
        self.set_pfb_taps(firdes.low_pass_2(self.pfb_gain, self.pfb_samp_rate, self.pfb_cutoff_freq, self.pfb_transition_width, self.pfb_attenuation))

    def get_pfb_attenuation(self):
        return self.pfb_attenuation

    def set_pfb_attenuation(self, pfb_attenuation):
        self.pfb_attenuation = pfb_attenuation
        self.set_pfb_taps(firdes.low_pass_2(self.pfb_gain, self.pfb_samp_rate, self.pfb_cutoff_freq, self.pfb_transition_width, self.pfb_attenuation))

    def get_audio_transition_width(self):
        return self.audio_transition_width

    def set_audio_transition_width(self, audio_transition_width):
        self.audio_transition_width = audio_transition_width
        self.set_audio_taps(firdes.low_pass_2(self.audio_gain, self.audio_samp_rate, self.audio_cutoff_freq, self.audio_transition_width, self.audio_attenuation))

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate
        self.set_audio_taps(firdes.low_pass_2(self.audio_gain, self.audio_samp_rate, self.audio_cutoff_freq, self.audio_transition_width, self.audio_attenuation))

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.set_audio_taps(firdes.low_pass_2(self.audio_gain, self.audio_samp_rate, self.audio_cutoff_freq, self.audio_transition_width, self.audio_attenuation))

    def get_audio_cutoff_freq(self):
        return self.audio_cutoff_freq

    def set_audio_cutoff_freq(self, audio_cutoff_freq):
        self.audio_cutoff_freq = audio_cutoff_freq
        self.set_audio_taps(firdes.low_pass_2(self.audio_gain, self.audio_samp_rate, self.audio_cutoff_freq, self.audio_transition_width, self.audio_attenuation))

    def get_audio_attenuation(self):
        return self.audio_attenuation

    def set_audio_attenuation(self, audio_attenuation):
        self.audio_attenuation = audio_attenuation
        self.set_audio_taps(firdes.low_pass_2(self.audio_gain, self.audio_samp_rate, self.audio_cutoff_freq, self.audio_transition_width, self.audio_attenuation))

    def get_pfb_taps(self):
        return self.pfb_taps

    def set_pfb_taps(self, pfb_taps):
        self.pfb_taps = pfb_taps
        self.set_pfb_ntaps(self.pfb_taps.__len__())
        self.pfb_decimator_ccf_0.set_taps((self.pfb_taps))

    def get_audio_taps(self):
        return self.audio_taps

    def set_audio_taps(self, audio_taps):
        self.audio_taps = audio_taps
        self.set_audio_ntaps(self.audio_taps.__len__())
        self.pfb_arb_resampler_xxx_0.set_taps((self.audio_taps))

    def get_pfb_ntaps(self):
        return self.pfb_ntaps

    def set_pfb_ntaps(self, pfb_ntaps):
        self.pfb_ntaps = pfb_ntaps

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        Qt.QMetaObject.invokeMethod(self._channel_counter, "setValue", Qt.Q_ARG("double", self.channel))
        Qt.QMetaObject.invokeMethod(self._channel_slider, "setValue", Qt.Q_ARG("double", self.channel))
        self.pfb_decimator_ccf_0.set_channel(int(self.channel))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.pfb_arb_resampler_xxx_0.set_rate( self.audio_rate / 50e3)

    def get_audio_ntaps(self):
        return self.audio_ntaps

    def set_audio_ntaps(self, audio_ntaps):
        self.audio_ntaps = audio_ntaps

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = fm_channelize()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
