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


#ifndef INCLUDED_WEST_STREAM_TRIGGED_PDU_H
#define INCLUDED_WEST_STREAM_TRIGGED_PDU_H

#include <west/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace west {

    /*!
     * \brief <+description of block+>
     * \ingroup west
     *
     */
    class WEST_API stream_trigged_pdu : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<stream_trigged_pdu> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of west::stream_trigged_pdu.
       *
       * To avoid accidental use of raw pointers, west::stream_trigged_pdu's
       * constructor is in a private implementation
       * class. west::stream_trigged_pdu::make is the public interface for
       * creating new instances.
       */
      static sptr make(std::string tag_name, unsigned int length);
    };

  } // namespace west
} // namespace gr

#endif /* INCLUDED_WEST_STREAM_TRIGGED_PDU_H */

