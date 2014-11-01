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
#include <gnuradio/high_res_timer.h>
#include "timestamp_tagger_ff_impl.h"

namespace gr {
  namespace west {

    timestamp_tagger_ff::sptr
    timestamp_tagger_ff::make(size_t itemsize, unsigned int interval)
    {
      return gnuradio::get_initial_sptr
        (new timestamp_tagger_ff_impl(itemsize, interval));
    }

    /*
     * The private constructor
     */
    timestamp_tagger_ff_impl::timestamp_tagger_ff_impl(size_t itemsize, unsigned int interval)
      : gr::sync_block("timestamp_tagger_ff",
                gr::io_signature::make(1, 1, itemsize),
                gr::io_signature::make(1, 1, itemsize)),
                interval(interval*itemsize),
                fractional_interval(interval*itemsize),
                itemsize(itemsize)
    {
        total_nitems = 0;
        //interval = interval;
        //fractional_interval = interval;
        tag_key = pmt::string_to_symbol("timestamp");
        //timer = boost::posix_time::microsec_clock::local_time();
    }

    /*
     * Our virtual destructor.
     */
    timestamp_tagger_ff_impl::~timestamp_tagger_ff_impl()
    {
    }

    int
    timestamp_tagger_ff_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const unsigned char *in = (const unsigned char *) input_items[0];
        unsigned char *out = (unsigned char *) output_items[0];

        std::memcpy(out, in, itemsize * noutput_items);
        static int ii=0;
        while( (total_nitems + fractional_interval) < (nitems_read(0) + noutput_items)) {
            int offset = (total_nitems + fractional_interval);
            pmt::pmt_t current_time = pmt::from_uint64(gr::high_res_timer_now());
            total_nitems = total_nitems + fractional_interval;
            add_item_tag(0, offset, tag_key, current_time);
            fractional_interval = interval;
            //printf("%i:total_nitems + fractional_interval (%i) < (%i)  nitems_read(0) + noutput_items\n", ii, total_nitems + fractional_interval, nitems_read(0) + noutput_items);
            ii++;
        }
        // fractional interval keeps track of when the next time tag needs to be added
        // in the case where noutput_items % interval != 0
        if(fractional_interval == interval ) {
            fractional_interval = nitems_read(0) + noutput_items - total_nitems;
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace west */
} /* namespace gr */

