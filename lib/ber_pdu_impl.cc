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
#include "ber_pdu_impl.h"
#include <string>
#include <cstdio>
#include <pmt/pmt.h>

namespace gr {
  namespace west {

    ber_pdu::sptr
    ber_pdu::make(std::string bitstream)
    {
      return gnuradio::get_initial_sptr
        (new ber_pdu_impl(bitstream));
    }

    /*
     * The private constructor
     */
    ber_pdu_impl::ber_pdu_impl(std::string bitstream)
      : gr::block("ber_pdu",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
        for(unsigned int ii=0; ii < bitstream.length(); ++ii) {
            const char this_char = bitstream.at(ii);
            unsigned char val = this_char == '0' ? 0 : 1;
            expected_payload.push_back(val);
        }
        //printf("expected: ");
        //for (unsigned int ii=0; ii < expected_payload.size(); ++ii) {
        //    printf("%01x", expected_payload[ii]);
        //}
        printf("\n");
        message_port_register_in(pmt::mp("pdus"));
        set_msg_handler(pmt::mp("pdus"), boost::bind(&ber_pdu_impl::handle, this, _1));
        total_errors = 0;
    }

    /*
     * Our virtual destructor.
     */
    ber_pdu_impl::~ber_pdu_impl()
    {
    }

    void
    ber_pdu_impl::handle(pmt::pmt_t vec)
    {
        size_t len = pmt::length(vec);
        const unsigned char* blob = pmt::u8vector_elements(vec, len);
        //printf("length of vector is: %i\n", (int)len);
        //printf("received: ");
        for (unsigned int ii=0; ii < len; ++ii) {
        //    printf("%01x", blob[ii]);
        //    if( ((ii+1) % 8) == 0  )
        //        printf(" ");
            unsigned char diff = 0x01 & (blob[ii] ^ expected_payload[ii]);
            total_errors += (unsigned int)diff;
            total_bits += 1;
        }
        printf("\n");
        std::cout << "total errors: " << total_errors;
        std::cout << " out of " << total_bits;
        std::cout << " : ratio  " << (float)total_errors/(float)total_bits << std::endl;
    }

    int
    ber_pdu_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        throw std::runtime_error("not a stream block");
    }

  } /* namespace west */
} /* namespace gr */

