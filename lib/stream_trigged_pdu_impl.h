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

#ifndef INCLUDED_WEST_STREAM_TRIGGED_PDU_IMPL_H
#define INCLUDED_WEST_STREAM_TRIGGED_PDU_IMPL_H

#include <west/stream_trigged_pdu.h>
#include <pmt/pmt.h>

namespace gr {
  namespace west {

    class stream_trigged_pdu_impl : public stream_trigged_pdu
    {
        private:
            void insert_to_vector ( const unsigned char* input_items, unsigned int n_buffer_items);

            pmt::pmt_t tag_key;
            std::vector<tag_t>  d_tags;
            bool triggered;
            unsigned int vector_iterator;
            int items_remaining;
            int magic_length;
            std::vector<unsigned char> pdu_vector;

        public:
            stream_trigged_pdu_impl(std::string tag_name, unsigned int length);
            ~stream_trigged_pdu_impl();

          // Where all the action really happens
          void forecast (int noutput_items, gr_vector_int &ninput_items_required);

          int general_work(int noutput_items,
               gr_vector_int &ninput_items,
               gr_vector_const_void_star &input_items,
               gr_vector_void_star &output_items);
    };

  } // namespace west
} // namespace gr

#endif /* INCLUDED_WEST_STREAM_TRIGGED_PDU_IMPL_H */

