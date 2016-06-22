        TAC KBP 2015 Tri-Lingual Entity Discovery and Linking
                    Evaluation Source Corpus V1.0
                             LDC2015E93

                         September 23, 2015
                     Linguistic Data Consortium


1. Overview

Text Analysis Conference (TAC) is a series of workshops organized by
the National Institute of Standards and Technology (NIST). TAC was
developed to encourage research in natural language processing (NLP)
and related applications by providing a large test collection, common
evaluation procedures, and a forum for researchers to share their
results. Through its various evaluations, the Knowledge Base
Population (KBP) track of TAC encourages the development of systems
that can match entities mentioned in natural texts with those
appearing in a knowledge base and extract novel information about
entities from a document collection and add it to a new or existing
knowledge base.

The goal of the Tri-Lingual Entity Discovery and Linking task is to
conduct end-to-end entity extraction, linking and clustering across
three languages, specifically, English, Chinese, and Spanish.  Given a
document collection, a TED&L system is required to automatically
extract (identify and classify) entity mentions (queries), link them
to nodes in the reference Knowledge Base (KB), and cluster NIL
mentions (those that do not have corresponding KB entries).  Compared
to the Entity Linking task, a TED&L system needs to extract queries
automatically.  For more information, please refer to the TED&L
section of NIST's TAC 2015 website at http://nlp.cs.rpi.edu/kbp/2015/.

This package contains the 500 source documents for use in the TAC KBP 
2015 Tri-Lingual Entity Discovery & Linking evaluation. Note that an
update to this package is currently planned that will include SERIF
annotations produce by BBN over the 500 documents included herein.


2. Contents

./README.txt
 
  This file

./data/ltf2src.perl 
  
  The perl script to reconvert LTF XML source docs back to original XML.  User
  documentation included in the script (run "perldoc" on the script file, or
  simply view the script file in any plain-text display, to read the
  documentation).
 
 ./data/cmn/discussion_forum/*

  This directory contains 82 discussion forum documents that were harvested
  from the web and converted into LTF.
  
./data/cmn/newswire/*

  This directory contains 84 newswire documents that were harvested
  from the web and converted into LTF.
  
./data/eng/discussion_forum/*

  This directory contains 85 discussion forum documents that were harvested
  from the web and converted into LTF.
  
./data/eng/newswire/*

  This directory contains 82 newswire documents that were harvested
  from the web and converted into LTF.

./data/spa/discussion_forum/*

  This directory contains 83 discussion forum documents that were harvested
  from the web and converted into LTF.

./data/spa/newswire/*

  This directory contains 84 newswire documents that were harvested
  from the web and converted into LTF.

./docs/TAC_KBP_2015_EDL_Guidelines_V1.2.pdf

  The most current version of the Entity Discovery & Linking annotation
  guidelines, encompassing Tri-lingual Entity Discovery & Linking.

./dtd/ltf.v1.5.dtd

  DTD for all docs found in ./data/{eng|spa|cmn}/{newswire|discussion_forum}/


3. Markup Frameworks 

3.1  Newswire Data

Newswire data use the following markup framework:

  <DOC id="{doc_id_string}">
  <SOURCE>
  ...
  </SOURCE>
  <DATE_TIME>
  ...
  </DATE_TIME>
  <HEADLINE>
  ...
  </HEADLINE>
  <TEXT>
  <P>
  ...
  </P>
  ...
  </TEXT>
  </DOC>

where the HEADLINE and DATE_TIME tags are optional (not always
present), and the TEXT content may or may not include "<P> ... </P>"
tags.

3.2  Discussion Forum Data

Discussion forum files use the following markup framework:

  <doc id="{doc_id_string}">
  <headline>
  ...
  </headline>
  <post ...>
  ...
  <quote ...>
  ...
  </quote>
  ...
  </post>
  ...
  </doc>

where there may be arbitrarily deep nesting of quote elements, and
other elements may be present (e.g. "<a...>...</a>" anchor tags).


4. Copyright Information

(c) 2015 Trustees of the University of Pennsylvania


5. Contact Information

For further information about this data release, contact the following
project staff at LDC:

  Joseph Ellis, Project Manager	     <joellis@ldc.upenn.edu>
  Jeremy Getman, Lead Annotator      <jgetman@ldc.upenn.edu>
  Neil Kuster, Lead Annotator        <neilkus@ldc.upenn.edu>
  Stephanie Strassel, PI             <strassel@ldc.upenn.edu>

--------------------------------------------------------------------------
README created by Neil Kuster on August 31, 2015
       updated by Neil Kuster on September 8, 2015
       updated by Neil Kuster on September 22, 2015
       updated by Jeremy Getman on September 22, 2015
       updated by Jeremy Getman on September 23, 2015
