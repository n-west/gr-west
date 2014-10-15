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

#ifndef INCLUDED_WEST_TIMESTAMP_TAGGER_FF_IMPL_H
#define INCLUDED_WEST_TIMESTAMP_TAGGER_FF_IMPL_H

#include <west/timestamp_tagger_ff.h>

namespace gr {
  namespace west {

    class timestamp_tagger_ff_impl : public timestamp_tagger_ff
    {
        private:
            unsigned int interval;
            unsigned int fractional_interval;
            unsigned int total_nitems;
            size_t itemsize;
            pmt::pmt_t tag_key;
            boost::posix_time::ptime timer;

        public:
            timestamp_tagger_ff_impl(size_t itemsize, unsigned int interval);
            ~timestamp_tagger_ff_impl();

            // Where all the action really happens
            int work(int noutput_items,
	             gr_vector_const_void_star &input_items,
	             gr_vector_void_star &output_items);
    };

  } // namespace west
} // namespace gr

#endif /* INCLUDED_WEST_TIMESTAMP_TAGGER_FF_IMPL_H */

