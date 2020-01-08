.. include:: defined_substitutions.txt

Trimming and Filtering Data
============================

  .. admonition:: learning-objectives

     - Know why data may need to be filtered or trimmed
     - Know some of the basic functionalities of Trimmomatic
     - Use Trimmomatic to trim a FastQ file



Filtering and trimming of data
-------------------------------

As the FastQ/FastQC lesson suggests, DNA generated from a sequencing experiment
will have errors. One of the reasons we want to generate millions of reads in
a high-throughput sequencing experiment is so that we have more than enough data
to be able to get an "average" (multiple observations at the same location).
Still though, there are limitations to sequencing technologies, and if our
Phred score indicates that some reads or some portions of reads are of low
quality, we may want to remove those data. Also, in generating a library for
DNA sequencing, we often need to attach |adapter sequences| as part of the
PCR/cloning of the sequence. Trimming can remove these contaminating sequences
as well.

|Trimmomatic| is a popular software for trimming sequencing reads. There are a
number of operations you can perform to selectively trim individual sequences.
Remember, as FastQ file may contain perhaps millions of individual sequencing
reads. When you use Trimmomatic, you will usually use a quality report (like
the FastQC report) to decide, what operations on average, will give you the
desired result. For example, if you generally have good sequence data (high
Phred score) for the first 100 bases of your reads, but then the average quality
is low for the last 25 bases, you might want to trim the last 25 bases off all
reads. If you have adapters on your sequence that take up the first 15 bases,
you may want to remove those before analyzing your data.


Trimmomatic Functionalities
-------------------------------

The |Trimmomatic| website has a manual with the full description of
functionalities. Here are just a few to consider (taken from the
Trimmomatic manual):

 .. list-table::

   * - Trimmomatic Function
     - Description
     - Example usage
   * - SLIDINGWINDOW
     - Perform a sliding window trimming, cutting once the average quality
       within the window falls below a threshold. By considering multiple bases,
       a single poor quality base will not cause the removal of high quality
       data later in the read
     - -  .. code-block:: bash

           SLIDINGWINDOW:<windowSize>:<requiredQuality>
       - windowSize: specifies the number of bases to average across
       - requiredQuality: specifies the average quality required
   * - HEADCROP
     - Removes the specified number of bases, regardless of quality, from the
       beginning of the read
     - -  .. code-block:: bash

           HEADCROP:<length>
       - length: The number of bases to remove from the start of the read
   * - MINLEN
     - Removes reads that fall below the specified minimal length. If required,
       it should normally be after all other processing steps. Reads removed by
       this step will be counted and included in the „dropped reads‟ count
       presented in the Trimmomatic summary
     - -  .. code-block:: bash

           MINLEN:<length>
       - length: Specifies the minimum length of reads to be kept


Use Trimmomatic to trim and filter RNA-Seq reads
---------------------------------------------------

Using the Jupyter Notebook, you will run Trimmomatic using the SLIDINGWINDOW and
MINLEN functions. Then use FastQC to see how your trim settings have changed
(and hopefully improved) the quality of the data.

1. Access the `JupyterLab Lesson on CyVerse <section-1.rst>`_ and complete
   **Notebook 2: Trimming bad data**

     .. admonition:: Notebook Preview

       This is a preview of the notebook in this lesson. Go back to
       `JupyterLab Lesson on CyVerse`_ to launch and use the interactive
       notebook.

       .. raw:: html

         <iframe src="_static/notebook-2.html"
         height="600" width=100%></iframe>

Questions
------------

.. admonition:: Question
   :class: admonition-question

   1. What are some reasons why sequencing data may need to be trimmed and/or
      filtered

   2. What does the Trimmomatic SLIDINGWINDOW function do?

   **Bonus**

   Examine your FastQC report before and after trimming. What are some
   differences you can spot? Did trimming help? What settings might you
   change next to improve the outcome?

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
