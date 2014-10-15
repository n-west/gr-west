#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Nathan West.
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
import pmt

import west_swig as west

class qa_ber_pdu (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        tag = gr.tag_t()
        tag.key = pmt.string_to_symbol('payload_start')
        tag.value = pmt.from_long(True)
        tag.offset = 5
        src = blocks.vector_source_b(range(200), False, 1, (tag,))
        trigger = west.stream_trigged_pdu('payload_start', 8)
        sink = west.ber_pdu(''.join(map(lambda x: "{0:b}".format(x), [0,1]*4)))
        self.tb.connect(src, trigger)
        self.tb.msg_connect(trigger, 'pdus', sink, 'pdus')
        self.tb.run()



if __name__ == '__main__':
    gr_unittest.run(qa_ber_pdu, "qa_ber_pdu.xml")
