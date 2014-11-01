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

#include <cstdio>
#include <fstream>
#include <string>
#include <gnuradio/io_signature.h>
#include <gnuradio/high_res_timer.h>
#include "timestamp_sink_f_impl.h"

namespace gr {
  namespace west {

    timestamp_sink_f::sptr
    timestamp_sink_f::make(std::string ts_tag, std::string filename)
    {
      return gnuradio::get_initial_sptr
        (new timestamp_sink_f_impl(ts_tag, filename));
    }

    /*
     * The private constructor
     */
    timestamp_sink_f_impl::timestamp_sink_f_impl(std::string ts_tag, std::string filename)
      : gr::sync_block("timestamp_sink_f",
                gr::io_signature::make(1, 1, sizeof(float)),
                gr::io_signature::make(0, 1, sizeof(float)))
    {
        tag_key = pmt::string_to_symbol(ts_tag);
        //out_file = fopen(filename.c_str(), "w");
        out_file.open(filename.c_str(), std::ofstream::out);
        pc_latency_avg = 0;
        nlatency_tags = 0;
    }

    /*
     * Our virtual destructor.
     */
    timestamp_sink_f_impl::~timestamp_sink_f_impl()
    {
        //fflush(out_file);
        //fclose(out_file);
        out_file.close();
    }

    int
    timestamp_sink_f_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        //float *out = (float *) output_items[0];

        get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0) + noutput_items, tag_key);
        for( unsigned int ii = 0; ii < tags.size(); ++ii) {
            gr::high_res_timer_type current_time = gr::high_res_timer_now();
            unsigned int tagged_time = pmt::to_uint64(tags[ii].value);
            unsigned int latency = current_time - tagged_time;
            pc_latency_avg += ((float)latency - pc_latency_avg)/(float)(nlatency_tags+1);
            nlatency_tags += 1;
            out_file << latency << "," << pc_latency_avg << std::endl;

            //printf("tagged at %u; read at %u; latency %u; avg %lli\n",
            //        tagged_time, current_time, latency, pc_latency_avg);
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace west */
} /* namespace gr */

