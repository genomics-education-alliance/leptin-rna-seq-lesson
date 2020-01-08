.. include:: defined_substitutions.txt


Pseudoalignment of Data Using Kallisto
===========================================

  .. admonition:: learning-objectives

     - Know how counting RNA-Seq reads allows you to make inferences about
       gene expression
     - Know the types of data need to us Kallisto
     - Use Kallisto to align RNA-Seq reads to a transcriptome



The Ideal RNA-Seq experiment
-------------------------------

In a perfect world, RNA-Seq might work something like this:

 1. We know the location of every single gene in the genome (even genes that
    are identical duplicates of each other).
 2. At any given time, we can get an exact readout of how many mRNAs a gene
    has produced (transcription) and for protein coding mRNA transcripts we
    know how much protein was yielded.
 3. Given 1 and 2, we can clearly tell if gene transcription is different
    between two different samples (e.g. normal tissue and cancerous).


Real-world RNA-Seq
-------------------------------

Unfortunately, here are just some of the ways a real world experiment fails to
meet our ideal expectations:

 1. We don't know the location of every gene in the genome (often we think we
    know most of them though!).
 2. Genomes contain gene duplications (identical or near identical copies).
    Since our DNA sequencing reads are often around 100 nucleotides we may
    have difficulty telling where a read came from (and thus how to count it).
 3. Even if we have an idea of how much RNA is being produced, we don't know
    how much of it ends up making a protein.


RNA-Seq with Kallisto
-------------------------------

Despite these challenges, RNA-Seq is a very useful experiment and researchers
have worked through many of the challenges above to develop software that
can help us infer what is happening in the transcriptome.

|Kallisto| is a quick, highly-efficient software for quantifying transcript
abundances in an RNA-Seq experiment. Even on a typical laptop, Kallisto can
quantify 30 million reads in less than 3 minutes.

In order to analyze data with Kallisto we need several inputs:

 1. We need the FastQ files from the RNA-Seq experiment; we usually start with
    reads that have already been trimmed/filtered

 2. We need a reference transcriptome. This is a file that has the sequences
    for all the known expressed genes. Reference transcriptomes are usually
    available from repositories like |Ensembl| and NCBI. We will be using the
    mouse reference transcriptome (available on the linked page
    "Download sequences in FASTA format for **transcript**"). Unlike a genome,
    the transcriptome is only coding genes.

*Optional*

We also will get the annotations and chromosome information for our subsequent
visualization steps:

 3. We need a reference annotations. This is a file that has the names and
    locations for all the genes in the transcriptome. Annotations have
    information like how many introns/exons a gene contains, and perhaps other
    information about the gene (such as a predicted function). This information
    also comes from the |Ensembl| page

 4. Because of the way we sequenced (single-end sequencing) we also need to know
    the chromosome lengths and this information from the NCBI
    |mouse reference| page.

**Basic Kallisto Steps**

Analysis with Kallisto has two main steps (see the manual on the |Kallisto|
home page):

  .. list-table::

    * - Step
      - Description
      - Command
      - Command explanation
      - Input
      - Output
    * - 1
      - Genome indexing
      -  .. code-block:: bash

             kallisto index <--index=> <transcriptome.fa.gz>
      - - `kallisto index`: Command to begin the indexing
        - `--index=`: The name your want your index file to be called
        - `transcriptome.fa.gz`: A transcriptome in fasta format (may becompressed ".gz")
      - Reference transcriptome
      - Kallisto index (no file extension)
    * - 2
      - Pseudoalignment*
      - .. code-block:: bash

             kallisto quant
             --single
             --threads=<t>
             --index=<index name>
             --bootstrap-samples=<b>
             --fragment-length=<f>
             --sd=<s>
             --output-dir=<dir>
             --genomebam
             --gtf=<annotations.gff>
             --chromosomes=<chromosome_list.tsv>
             <fastq_input.fastq.gz>
      - - `kallisto quant`: Command to start Kallisto
        - `single`: Indicates this is single-end sequence data
        - `threads=[t]`: Optional - indicates how many CPU threads to use
        - `bootstrap-samples=<b>`: Conduct <b> (integer) of bootstrap samplings
        - `fragment-length=<f>`: Estimated average fragment length the
           sequencing library used DNA fragments of length f (integer)
        - `sd=<s>`:  Estimated standard deviation of fragment length
                     (default: -l, -s values are estimated from paired
                     end data, but are required when using --single)
        - `output-dir=<dir>`: Name of directory where results should be output
        - `genomebam`: Create a pseudobam file (will be used in visualization)
           to see where individual reads map on the genome
        - `gtf=<annotations.gff>`:GTF file for transcriptome annotation information
           (required for --genomebam)
        - `chromosomes=<chromosome_list.tsv>`: Tab separated file with
           chromosome names and lengths (optional for --genomebam, but
           recommended)
        - `<fastq_input.fastq.gz>`: FastQ file for analysis
      - - FastQ file (one per run of Kallisto)
        - Kallisto index (from indexing step)
      - - `abundances.h5`: HDF5 binary file containing run info,
           abundance estimates, bootstrap estimates, and transcript length
           information length
        - `abundances.tsv`: Plaintext file of the abundance estimates. It does
           not contains bootstrap estimates. When plaintext mode is selected;
           output plaintext abundance estimates. Alternatively, kallisto
           h5dump will output an HDF5 file to plaintext. The first line contains
           a header for each column, including estimated counts, TPM,
           effective length
        - `run_info.json`: a json file containing information about the run

**\*Note**: The Psuedoalignment step in the JupyterNotbook is written in a
"For Loop" since we want to run it for one or more fastq files. If you have
only one file, a for loop is overkill, but for more files, the For Loop is
efficient since it would automatically run analysis on one file right after
another. See `Linux/Bash Command Line Primer <section-3.rst>`_ for more
information.

Pseudoalignment and genomics word search
------------------------------------------

Alignment of reads is an expansive topic. Several reviews cover some of the
important topics including |Stark et. al. 2019|. This |blog post| and the
|kallisto paper| are required readings to get a deep understanding of the
subject.

To try and reduce this problem to its most basic, let's use an analogy.
In the traditional case, when software does alignment, it tries to match a
read to the genome.

  .. code-block:: text

      Genome: ACTACGTAGCCGTCAAATATCCCGGGTATCGTACGATCGACGT

      Read:   AAATTTCCCGGG

If we move things around we can find the match:

  .. code-block:: text

      Genome: ACTACGTAGCCGTCAAATATCCCGGGTATCGTACGATCGACGT
                            |||| |||||||
      Read:                 AAATTTCCCGGG

In this example a "|" appears when there is a match, and we have one mismatch.
Although finding this match was simple, the genome is far more complex.

In the word search below is the word "DNA". Can you find it?
It may take you a while. Searching for words is a process similar to taking
sequencing reads and trying to match them to the genome. Computers are fast,
but just as matching a small word (3 letters) in a large (1639 letter) word
puzzle is time-intensive, it take a long time to match millions of short reads
against genomes of billions of nucleotides.

  .. code-block:: text

      CUSVFVMAASJFHUTMNCCQMBVXOLBEETYHSRBWOSEY
      MOBJEYXAZMPMFENZHQKMHHSCZUXUQYEBQONJVYWH
      LCMIFVSPNMAGIJAOOFCWNYYDETTLMGCDOBSLOPXO
      ZAUSKOGLCYOIKIXZSHOXHLYGZJLRLZMRGHRFRJWN
      HBEOJQLIXUYAIAWMJASRBOVSBHMAHJFPUOXTQIYZ
      LSSCVOGPJCIIMUILZCFKLASLFLQFIZVSYXWJYNMJ
      QPWLYGLRTSTQHYUVFVGGPDMICLGDUMZOVPHFPLOD
      YFZAYPVONRRCPHJPNJVROZEZPBLZNYBQHOVUPOGJ
      SAVCNZWIYQKHJOLKQBHZYGJZKUEHKJLCLXOLMUJF
      YJAGKRFQOQRNAXXXZAZUMMWMLKWNREHDFOLVVYWK
      ATOXWLBGQECNAMWJIMONGSAVKGSHUVUOROVJRJGT
      AJLVEYWLSFPUIYABELQZLYLUGZJGPGWEVPXYCHGO
      IPXOCIPREEDCYTFZHBDTTOIJRWLEYEMMTRIDSMGJ
      BNEZKUNVOXZFIXAAGGYUWAYZSNVUHXJZMMPXBPTE
      QMVXMUJAFUGBBLAVVCGVBDIGDBIDBSHTEVPCJTUB
      ELJIPXDVTMPNCROAPIHZMROJXZFCDHRYWIEUSZST
      ERRCPCLAPIJROAAUKZNDYYKNWKNUNFDKSTLYTXKA
      UAMNKGZVKWMOYGLLWUJOECUNBRUGRPWWUNNVEXYF
      MQYPHTEPNKPLWECXVORINUEHHVLVBNFUJJXNEZYT
      MJDQTZMIRJXMLYUCXYCVFQHHQBERSMGQLRWNYAJP
      IELYQQDAIXJDTUONASHBTLCZISHQWCMJZFAFJOXE
      UGZWMJGDLLRKIZVVLPHYBCULVCAIRMMEQPRRHFHQ
      FFCWSFSQZJTBCVFHUAEECJPXKHMKRKJFBZVQNOMZ
      ZZZEMQQNVWUXDOYBDHSDFLHMAQEWFKWPMIGJVZUT
      ZNEQDNAHXMPBLRVDEBJRJFTDOIWUPFLSIYOOHNQH
      TTMIXMVUMETGMJWFEWCRITKZWZGVMCNQRAPDCJZD
      AXPTCGYNKVFDPALHRQNPKQUBSEGOOQCVUDDHTIWR
      GEMJXKJGSSRAROGDWETVVTZMWUSCYXIKTUFLUIXO
      BDZFSFRPFXHALCKUGTOHGMEHYPRPTFXUSWSKDBWC
      UGGJXCDKYYZZFLDAWLDYJLCRSTDSMLOGPCVAUDZZ
      AHGKHDAGOHYQDKGWDTOGFVOSRKJCPRRENRQRBBPQ
      ABHWPOFZYTGHXPREABCTWABQLZLYBOQVHOMUHGRS
      FPNWCEQGTYJEDRWAVDYKUAZMLVVNTYNRZHPFHYGR
      UAJNXZWZSBLEVYIGLRPFNZLOGRULAHIAHDLXTJXF
      DQEKRQNVJACCBVGABSKTWRPYEFXNEHSICVLHWOIV
      GVOGZWUSLGRGHMVENEYNSBCZRLOZYCMXCYGWUMSG
      LFXDWDWHJYXAXDVWVMTPKQVTAYHNCADYJCNKNDZM
      ASJBGHYSPRUIIVQDAVUQBEEDNQKBKQPMKYQKRIKV
      MWFHPISMEIUIVZVBEUKTFOUADMUDXAJSGYHLXUSP
      OSIVVLZMDTLDMCLGZLEGWLPVPWOLNERAINTAESFR


Pseudoalignment is one approach to this computational "word search". It takes
advantage of a trick to speed up performance without loosing accuracy.
Take the second line in our "DNA" word search puzzle:

.. code-block:: text

    MOBJEYXAZMPMFENZHQKMHHSCZUXUQYEBQONJVYWH

There is no "D" in this line. True, We don't know that until we read the entire
line, but once we realize this line can't possible be a match without a "D"
We can ignore this line. Word search puzzles don't have to be read in just one
direction (words might be on diagonals, backwards, etc.), but now consider
what happens in the pseudoalignment "word search". In this case we are searching
not the entire genome, but linear transcripts:

.. code-block:: text

    Transcript 1: CUSVFVMAASJFHUTMNCCQMBVXOLBEETYHSRBWOSEY
    Transcript 2: MOBJEYXAZMPMFENZHQKMHHSCZUXUQYEBQONJVYWH
    Transcript 3: LCMIFVSPNMAGIJAOOFCWNYYDETTLMGCDOBSLOPXO
    Transcript 4: ZAUSKOGLCYOIKIXZSHOXHLYGZJLRLZMRGHRFRJWN
    Transcript 5: ZNEQDNAHXMPBLRVDEBJRJFTDOIWUPFLSIYOOHNQH

We can immediately eliminate transcripts that don't contain the letter D:

.. code-block:: text

    Transcript 3: LCMIFVSPNMAGIJAOOFCWNYYDETTLMGCDOBSLOPXO
    Transcript 4:
    Transcript 5: ZNEQDNAHXMPBLRVDEBJRJFTDOIWUPFLSIYOOHNQH

Immediately, the problem is made easier by throwing away transcripts that could
not contain the answer. This is not an exact analogy but basically, rather than
trying to match every read to every position in the genome, Kallisto is faster
because 1) we are only matching to the transcriptome (a subset of the genome)
and 2) we focus only on transcripts that *could have* generated a particular
read.

  .. note::

     Pseudoalignment is just one approach to aligning RNA-Seq reads. Other
     software will do full alignments of the read to a transcriptome or
     genome. These methods have different advantages and requirements - the
     |Stark et. al. 2019| is a suggested reading.


Use Kallisto to Pseudoalign RNA-Seq Reads
---------------------------------------------------

Using the Jupyter Notebook, you will run use Kallisto to analyze trimmed RNA-Seq
reads. The notebook covers importing reference data (transcriptome,
annotations, chromosome coordinates) from Ensembl and NCBI.

1. Access the `JupyterLab Lesson on CyVerse <section-1.rst>`_ and complete
   **Notebook 3: RNA-Seq from scratch - Kallisto**


     .. admonition:: Notebook Preview

       This is a preview of the notebook in this lesson. Go back to
       `JupyterLab Lesson on CyVerse`_ to launch and use the interactive
       notebook.

       .. raw:: html

         <iframe src="_static/notebook-3.html"
         height="600" width=100%></iframe>

Questions
------------

.. admonition:: Question
   :class: admonition-question

   1. What are some of the constraints we have to work within when doing an
      RNA-Seq experiment (e.g. the difference between the ideal experiment
      and the real-world experiment?)

   2. In addition to FastQ reads, what are some other datasets needed to do
      RNA-Seq using Kallisto?

   3. Use an analogy to explain Kallisto pseudoalignment

   **Bonus**

   Using the referenced papers and other research materials you can find, what
   are some other software tools that could be used as an alternative to
   Kallisto in RNA-Seq? Do they require the same datasets as Kallisto
   does in order to run?


----

.. Comment: Place Images Below This Line
   use :width: to give a desired width for your image
   use :height: to give a desired height for your image
   replace the image name/location and URL if hyperlinked

 .. |Static image| image:: ./img/IMAGENAME.png
    :width: 25
    :height: 25

 .. |Clickable hyperlinked image| image:: ./img/IMAGENAME.png
    :width: 500
    :height: 100
 .. _link : http://link-url

.. Comment: Place URLS Below This Line

   # Use this example to ensure that links open in new tabs, avoiding
   # forcing users to leave the document, and making it easy to update links
   # In a single place in this document

   .. |Substitution| raw:: html # Place this anywhere in the text you want a hyperlink

      <a href="REPLACE_THIS_WITH_URL" target="blank">Replace_with_text</a>


.. |Github Repo Link|  raw:: html

   <a href="FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX_FIX" target="blank">Github Repo Link</a>
