#!/usr/bin/env python
#
# Copyright 2013 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
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

    # this properly tests tag version
    # def test_001_t (self):
    #     tag = gr.tag_t()
    #     tag.key = pmt.string_to_symbol('payload_start')
    #     tag.value = pmt.from_long(True)
    #     tag.offset = 5
    #     src = blocks.vector_source_b(range(200), False, 1, (tag,))
    #     trigger = west.stream_trigged_pdu('payload_start')
    #     sink = blocks.message_debug()
    #     self.tb.connect(src, trigger)
    #     self.tb.msg_connect(trigger, "pdus", sink, "store")
    #     self.tb.run ()
    #     for ii in xrange(sink.num_messages() ):
    #         msg = sink.get_message(ii)
    #         print pmt.to_python(msg)

    def test_001_t (self):
        ac = [1,1,1,0,0,1,0]
        payload = [0,0,1,0,1,0,1,0]
        tx_data = ac + payload*30
        src = blocks.vector_source_b(tx_data, False)
        correlator = digital.correlate_access_code_bb("1110010", 3)
        trigger = west.stream_trigged_pdu('payload_start', 8)
        sink = blocks.message_debug()
        self.tb.connect(src, correlator, trigger)
        self.tb.msg_connect(trigger, "pdus", sink, "store")
        self.tb.run ()
        for ii in xrange(sink.num_messages() ):
            msg = sink.get_message(ii)
            msg_tuple = tuple(pmt.to_python(msg))
            print msg_tuple
            self.assertEqual(msg_tuple, tuple(payload))




if __name__ == '__main__':
    gr_unittest.run(qa_stream_trigged_pdu, "qa_stream_trigged_pdu.xml")

