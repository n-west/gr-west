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


#ifndef INCLUDED_WEST_TIMESTAMP_SINK_F_H
#define INCLUDED_WEST_TIMESTAMP_SINK_F_H

#include <west/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace west {

    /*!
     * \brief Calculate latency of items through blocks
     * \ingroup west
     *
     */
    class WEST_API timestamp_sink_f : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<timestamp_sink_f> sptr;

        /*!
         * \brief Return a shared_ptr to a new instance of west::timestamp_sink_f.
         *
         * To avoid accidental use of raw pointers, west::timestamp_sink_f's
         * constructor is in a private implementation
         * class. west::timestamp_sink_f::make is the public interface for
         * creating new instances.
         */
        static sptr make(std::string ts_tag, std::string filename);

        /*! \brief Return average latency of items
         *
         * A 1-tap IIR is used to internally track average latency. This
         * is a getter for that avg latency
         */
        virtual long long latency_avg(){};
    };

  } // namespace west
} // namespace gr

#endif /* INCLUDED_WEST_TIMESTAMP_SINK_F_H */

