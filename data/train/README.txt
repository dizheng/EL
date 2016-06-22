     TAC KBP 2015 Tri-lingual Entity Discovery & Linking Training 
               Gold Standard Knowledge Base Links V1.0
                             LDC2015E75

                            August 17, 2015
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

The goal of the Tri-lingual Entity Discovery and Linking task is to
conduct end-to-end entity extraction, linking and clustering across
three languages, specifically, English, Chinese, and Spanish.  Given a
document collection, a TED&L system is required to automatically
extract (identify and classify) entity mentions (queries), link them
to nodes in the reference Knowledge Base (KB), and cluster NIL
mentions (those that do not have corresponding KB entries).  Compared
to the Entity Linking task, a TED&L system needs to extract queries
automatically.  For more information, please refer to the TED&L
section of NIST's TAC 2015 website at http://nlp.cs.rpi.edu/kbp/2015/.

This package contains the TAC KBP 2015 Tri-lingual Entity Discovery &
Linking training gold standard entity mentions as well as the source 
documents, KB links, NIL equivalence class clusters, and entity type 
information for each, and for each discussion forum document, the 
offset regions that align with quotes in the text.


2. Contents

./README.txt
 
  This file

./data/tac_kbp_2015_tedl_training_gold_standard_entity_mentions.tab

  This file contains 30,839 gold standard responses. Each response 
  consists of the following fields:

  Column 1:  system run ID (always "LDC" in these data)

  Column 2:  mention (query) ID: unique for each entity name mention and
             in the format of 'TEDL15_TRAINING_XXXXX'

  Column 3:  mention string: the full string of the query entity mention.

  Column 4:  (document ID):(mention head start offset)–(mention head end
             offset): an ID for a document in the source corpus from which the
             mention head was extracted, the starting offset of the mention
             head, and the ending offset of the mention head (e.g.
             AFP_ENG_20080610.0052:244-252).  These are character offsets (not
             byte offsets); first character in a documents is at offset 0.

  Column 5:  Knowledge Base (KB) link ID or NIL cluster ID: If the ID
             begins with "m", the text refers to an entity in the KB (e.g.
             'm.09b6zr').  If the given query is not linked to an entity in
             the KB, then it is given a NIL ID, which consists of "NIL"
             plus a five-digit, zero-padded integer (e.g. 'NIL00001',
             'NIL00002').  Entity mentions pointing to equivalent referents
             are indicated by shared KB link IDs or NIL cluster IDs;
             otherwise, all the IDs are distinct from one another.

  Column 6:  entity type: {GPE, ORG, PER, LOC, FAC, TTL} type indicator
             for the entity

  Column 7:  mention type: {NAM, NOM} type indicator for the entity mention

  Column 8:  a confidence value: Always "1.0" in LDC responses.

  Column 9:  web-search - (Y/N) indicating whether the annotator made use
             of web searches in order to make the linking judgment.

  Column 10: wiki text - (Y/N) indicating whether the annotator made use
             of the wiki text in the knowledge base (as opposed to just
             the infobox information) in order to make the linking judgment.

  Column 11: Unknown - (Y/N) indicating whether the source document
             contained insufficient information about the query entity in
             order to determine whether or not it existed in the KB.  Note
             that for entity mentions with a KB ID, this value will always be 
             'Y'. NIL entities can have either 'Y' or 'N' in this column.

./data/source_docs/{cmn,eng,spa}/*

  These directories contain all 444 of the source documents listed in column
  4 of the gold standard entity mentions table.
  
./data/source_docs/quote_regions.tab
  
  This is a list of offset regions that align with quotes in the text, 
  provided for each discussion forum document in this corpus.
  
./data/source_docs/ltf2src.perl 
  
  The perl script to reconvert LTF XML source docs back to origina XML.  User
  documentation included in the script (run "perldoc" on the script file, or
  simply view the script file in any plain-text display, to read the
  documentation).
 
./docs/TAC_KBP_2015_EDL_Guidelines_V1.2.pdf

  The most current version of the Entity Discovery & Linking annotation 
  guidelines, encompassing Tri-lingual Entity Discovery & Linking.

./dtd/ltf.v1.5.dtd

  The dtd against which all ltf.xml files in ./data/source_docs/{cmn,eng,spa}/
  validate.


3. Text Normalization

Name string matches are case and punctuation sensitive. The only text
normalization done is:

   1. conversion of newlines to a space, except where preceding
      character is hyphen ("-") where newline is removed

   2. conversion of multiple consecutive spaces (including U+00A0,
      "non-breaking space") to a single space


4. Copyright Information

(c) 2015 Trustees of the University of Pennsylvania


5. Contact Information

For further information about this data release, contact the following
project staff at LDC:

  Joseph Ellis, Project Manager      <joellis@ldc.upenn.edu>
  Jeremy Getman, Lead Annotator      <jgetman@ldc.upenn.edu>
  Neil Kuster, Lead Annotator        <neilkus@ldc.upenn.edu>
  Stephanie Strassel, PI             <strassel@ldc.upenn.edu>

--------------------------------------------------------------------------
README created by Neil Kuster on August 17, 2015
       updated by Jeremy Getman on August 19, 2015
       updated by Jeremy Getman on August 20, 2015
