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


#ifndef INCLUDED_WEST_TIMESTAMP_TAGGER_FF_H
#define INCLUDED_WEST_TIMESTAMP_TAGGER_FF_H

#include <west/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace west {

    /*!
     * \brief Add a timestamp tag to a stream at a specified interval (in items)
     * \ingroup west
     *
     */
    class WEST_API timestamp_tagger_ff : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<timestamp_tagger_ff> sptr;

       /*!
        * \brief Add a timestamp to a stream with interval.
        *
        * Using the gr::high_res_timer timestamp samples at the specified
        * interval. This is intended for finding latency across blocks
        */
      static sptr make(size_t itemsize, unsigned int interval);
    };

  } // namespace west
} // namespace gr

#endif /* INCLUDED_WEST_TIMESTAMP_TAGGER_FF_H */

