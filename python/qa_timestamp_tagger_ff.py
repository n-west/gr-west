#!/usr/bin/env python
#
# Copyright 2013 Nathan West.
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
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest, blocks, digital
import pmt
import west_swig as west


class qa_stream_trigged_pdu (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        tx_data = range(256)
        src = blocks.vector_source_f(tx_data, False)
        but = west.timestamp_tagger_ff(4, 10)
        sink = blocks.tag_debug(4, "dbg_sink", "timestamp")
        self.tb.connect(src, but, sink)
        self.tb.run ()


if __name__ == '__main__':
    gr_unittest.run(qa_stream_trigged_pdu, "qa_stream_trigged_pdu.xml")

