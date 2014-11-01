#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: FM whole-band Channelizer to Measure Latency vs TP
# Author: Nathan West
# Generated: Wed Oct 29 20:19:42 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import time
import west

class fm_channelize_latency(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "FM whole-band Channelizer to Measure Latency vs TP")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3.125e6
        self.gain = gain = 10
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
        self.west_timestamp_tagger_ff_0 = west.timestamp_tagger_ff(gr.sizeof_gr_complex, 100)
        self.west_timestamp_sink_f_0 = west.timestamp_sink_f("timestamp", "fm_latency_meas")
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_fff(
        	   audio_rate / 50e3,
                  taps=(audio_taps),
        	  flt_size=10)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/nathan/Downloads/WFM-97.9MHz-3.125Msps.dat", False)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=200e3,
        	audio_decimation=int(200e3 / audio_rate),
        )
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=audio_rate, tau=75e-6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.analog_fm_deemph_0, 0))
        self.connect((self.analog_fm_deemph_0, 0), (self.west_timestamp_sink_f_0, 0))
        self.connect((self.west_timestamp_sink_f_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.west_timestamp_tagger_ff_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.west_timestamp_tagger_ff_0, 0))



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
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."

    for max_noutput_items in range(64,4096, 128):
        tb = fm_channelize_latency()
        start_time = gr.high_res_timer_now()
        tb.start(max_noutput_items)
        time.sleep(5)
        stop_time = gr.high_res_timer_now()
        throughput = tb.west_timestamp_sink_f_0.pc_throughput_avg()
        tb.stop()
        print "throughput is %i" % (throughput)


