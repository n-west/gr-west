/* -*- c++ -*- */

#define WEST_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "west_swig_doc.i"

%{
#include "west/timestamp_tagger_ff.h"
#include "west/stream_trigged_pdu.h"
#include "west/ber_pdu.h"
#include "west/timestamp_sink_f.h"
%}

%include "west/timestamp_tagger_ff.h"
GR_SWIG_BLOCK_MAGIC2(west, timestamp_tagger_ff);
%include "west/stream_trigged_pdu.h"
GR_SWIG_BLOCK_MAGIC2(west, stream_trigged_pdu);
%include "west/ber_pdu.h"
GR_SWIG_BLOCK_MAGIC2(west, ber_pdu);
%include "west/timestamp_sink_f.h"
GR_SWIG_BLOCK_MAGIC2(west, timestamp_sink_f);
