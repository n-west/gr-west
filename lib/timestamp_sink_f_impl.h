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

#ifndef INCLUDED_WEST_TIMESTAMP_SINK_F_IMPL_H
#define INCLUDED_WEST_TIMESTAMP_SINK_F_IMPL_H

#include <west/timestamp_sink_f.h>

namespace gr {
  namespace west {

    class timestamp_sink_f_impl : public timestamp_sink_f
    {
        private:
            pmt::pmt_t tag_key;
            FILE* out_file;
            std::vector<gr::tag_t> tags;
            long long pc_latency_avg;
            long long nlatency_tags;

        public:
            timestamp_sink_f_impl(std::string ts_tag, std::string filename);
            ~timestamp_sink_f_impl();

            long long latency_avg() const { return pc_latency_avg; };
            // Where all the action really happens
            int work(int noutput_items,
	             gr_vector_const_void_star &input_items,
	             gr_vector_void_star &output_items);
    };

  } // namespace west
} // namespace gr

#endif /* INCLUDED_WEST_TIMESTAMP_SINK_F_IMPL_H */

