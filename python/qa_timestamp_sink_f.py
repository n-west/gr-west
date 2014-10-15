#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import west_swig as west

class qa_timestamp_sink_f (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        tx_data = range(4096*10)
        src = blocks.vector_source_f(tx_data, False)
        but = west.timestamp_tagger_ff(4, 10)
        sink = west.timestamp_sink_f("timestamp", "foo")
        self.tb.connect(src, but, sink)
        self.tb.run ()
        # check data

    def test_002_t (self):
        # set up fg
        tx_data = range(4096*10)
        src = blocks.vector_source_f(tx_data, False)
        but = west.timestamp_tagger_ff(4, 10)
        sink = west.timestamp_sink_f("timestamp", "foo2")
        self.tb.connect(src, but, sink)
        self.tb.run ()
        # check data
        print "latency avg is %i"%sink.latency_avg()

if __name__ == '__main__':
    gr_unittest.run(qa_timestamp_sink_f, "qa_timestamp_sink_f.xml")
