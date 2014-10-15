/* -*- c++ -*- */
/*
 * Copyright 2014 Nathan West.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "stream_trigged_pdu_impl.h"
#include <iostream>

namespace gr {
  namespace west {

    stream_trigged_pdu::sptr
    stream_trigged_pdu::make(std::string tag_name, unsigned int length)
    {
      return gnuradio::get_initial_sptr
        (new stream_trigged_pdu_impl(tag_name, length));
    }

    /*
     * The private constructor
     */
    stream_trigged_pdu_impl::stream_trigged_pdu_impl(std::string tag_name, unsigned int length)
      : gr::block("stream_trigged_pdu",
              gr::io_signature::make(0, 1, sizeof(char)),
              gr::io_signature::make(0, 0, 0))
    {
        message_port_register_out(pmt::mp("pdus"));
        tag_key = pmt::string_to_symbol(tag_name);
        triggered = false;
        vector_iterator = 0;
        magic_length = length;
        items_remaining = magic_length;
    }

    /*
     * Our virtual destructor.
     */
    stream_trigged_pdu_impl::~stream_trigged_pdu_impl()
    {
    }

    void
    stream_trigged_pdu_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        ninput_items_required[0] = noutput_items;
    }

    void
    stream_trigged_pdu_impl::insert_to_vector ( const unsigned char * input_items, unsigned int n_buffer_items)
    {
        for( unsigned int ii = 0; ii < n_buffer_items; ++ii ){
            pdu_vector.push_back(input_items[ii] & 0x1);
            if( pdu_vector.size() == magic_length ) {
                pmt::pmt_t pdu_output = pmt::init_u8vector(magic_length, pdu_vector);
                message_port_pub(pmt::mp("pdus"), pdu_output);
                pdu_vector.clear();
                vector_iterator = 0;
            }
        }
    }

    int
    stream_trigged_pdu_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const unsigned char *in = (const unsigned char *) input_items[0];

        /*
         *      THIS WORKS IF THE STREAM IS TAGGED PROPERLY
         *  BUT THE CURRENT GR CORRELATE ACCESS CODE TAG BLOCK IS BROKEN
        */
        // Grab tags, throw them into dict
        //if( !triggered ) {
        //    get_tags_in_range(d_tags, 0, nitems_read(0), nitems_read(0) + ninput_items[0], tag_key);
        //    if( d_tags.size() > 0) {
        //        triggered = true;
        //        insert_to_vector( in+d_tags[0].offset, ninput_items[0] - d_tags[0].offset);
        //    }
        //}
        //else {
        //        insert_to_vector( in, ninput_items[0]);
        //}

        if( !triggered ) {
            for( unsigned int ii=0; ii < ninput_items[0]; ++ii) {
                if( (in[ii] >> 1) & 0x01 ) {
                    // This is the start of the payload
                    triggered = true;
                    insert_to_vector( in+ii, ninput_items[0] - ii );
                    break;
                }
            }
        }
        else {
            // We already found the payload
            insert_to_vector( in, ninput_items[0] );
        }

        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume_each (noutput_items);

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace west */
} /* namespace gr */

