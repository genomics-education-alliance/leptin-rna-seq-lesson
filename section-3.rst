.. include:: defined_substitutions.txt

Linux/Bash Command Line Primer
=================================

  .. admonition:: learning-objectives

     - Understand how what the command line is
     - Understand basic command line syntax
     - Know the functions of the most common commands

Command Line Intro
----------------------

The *Command Line* (sometimes called 'the terminal', 'shell', 'Bash', etc.) is an
alternative to using a graphical interface (GUI, pronounced "gooey") or
point-and-click interfaces to operate a computer. Actually, command line came
before GUIs and although it's older, it is the most popular way for researchers
to use the computer and installed software. Imagine trying to explain to someone
how to make a recipe using *only* pictures (not even video). You would need a
lot of photos! If they wanted to modify the recipe for someone else, they would
need to take new photos. While photos help a cook, having written instructions is
much clearer. Using the command line, we can explicitly write every single
instruction we want the computer to run; this means our analysis is
always completely documented.

  .. note::


      It does take time to learn the command line, and some things about the
      command line are difficult the first time you try. This primer will cover
      just the basics needed to make the tutorial easier to understand.
      To learn more, we suggest the |Software Carpentry| lessons on the UNIX
      command line.

Command Line Syntax
----------------------

As the name suggests, everything run at the command line is a command. The
Syntax for a command looks like this:

  .. code-block:: bash

    command [options]

The `[options]` are some options that modify the command, and as the name
implies these are optional. Some commands may take an `<input>`; here the
pointed brackets suggest that the input is required.

One common command is the `ls` (list) command. Typing this will show the
contents of the current directory:

  .. code-block:: bash

    ls

To see what directory you are in, you can use the `pwd` command to see the
current working directory:

  .. code-block:: bash

    pwd


The ls command takes options. You can list the content of a specific directory.
For example to see the contents of `/home/gea_user/` you would try:

  .. code-block:: bash

    ls /home/gea_user/

Note there is always a space between a command (`ls`) and its inputs or options
(`/home/gea_user/`)


Command Glossary
----------------------

These are some commands you are likely to see:

 - `cat` - Concatenate: Print a file to the screen

   - Example:  `cat file.text`

 - `cd` - Change Directory: Change the working directory to a new directory

   - Example:  `cd /path/to/desired/new/directory`

 - `cut` - Cut: Choose a column from a tab-delimited file (spreadsheet)

   - Example:  `cut -f (column number to choose) file.txt`

 - `head` - Head: See the first few lines of a file

   - Example:  `head -n (number of lines to show) file.txt`

 - `ls` - List: Show the content of a directory

   - Example:  `ls /directory/to/show`

 - `mkdir` - Make directory: Make a new directory/folder

   - Example:  `mkdir name_of_new_directory`

 - `mv` - Move: Move a file(s) or directory

   - Example:  `mv /file/at/old/location/ /new/location/to/move/to`

 - `rm` - Remove: Delete a file/directory (must use -r option to delete a directory)

   - Example:  `rm name_of_file_to_delete`

 - `wget` - W get: Download a file from a URL

   - Example:  `wget http://some.url.com`

More Command Line Syntax Tips
--------------------------------

**Pay attention to spaces and special characters**

The Command Line requires you to be very exact in your syntax. In general, you
don't want to have file names with special characters (e.g. !#$%^&* etc.).
Also, you cannot use spaces in file names (use underscore or dash instead).

**Wildcards**

In some cases you will see the wildcard character '\*'. This asterisk generally
means match any character. For example the command

  .. code-block:: bash

    mv *.html /directory

Would mean "move any file as long as it ends in ".html" to a place called
`/directory`"


Long Commands and Loops
------------------------

**Long Commands**

Sometimes you will see a command that looks like this:

  .. code-block:: bash

    for file in *_trimmed.fastq.gz; do output=$(basename --suffix=.fastq.gz_trimmed.fastq.gz $file)_quant; kallisto quant\
    --single\
    --threads=8\
    --index=/home/gea_user/rna-seq-project/transcriptome/Mus_musculus.GRCm38_index\
    --bootstrap-samples=25\
    --fragment-length=200\
    --sd=20\
    --output-dir=$output
    done

The backslash (\\) is just a way of splitting up the command over multiple lines to make
it easier to read. We could also write the same command like this (more difficult
to read):

  .. code-block:: bash

    for file in *_trimmed.fastq.gz; do output=$(basename --suffix=.fastq.gz_trimmed.fastq.gz $file)_quant;
    kallisto quant --single --threads=8 --index=/home/gea_user/rna-seq-project/transcriptome/Mus_musculus.GRCm38_index
    --bootstrap-samples=25 --fragment-length=200 --sd=20 --output-dir=$output;
    done

**Loops**

You will also see loops with a syntax that begins with a statement like 'for' or
'while'. For example:

    .. code-block:: bash

      for trimmed_file in /home/gea_user/rna-seq-project/trimmed-reads/*_trimmed.fastq.gz
       do
       fastqc $trimmed_file
       done

    or

    .. code-block:: bash

      while read line; do prefetch $line; done<finalsamples.txt; done

A loop usually takes several files and performs one or more operations
to that file. See the Software Carpentry |loop lesson| for more on this.

**Variables**

At the shell you will sometimes see a '$' in front of a word. This '$' indicates
that the word is a variable. You will usually see this inside of loops and the
Software Carpentry |loop lesson| also goes into further explanation.

  .. tip::

    The website |Explain Shell| allows you to take a line of Linux code and
    break it down into an annotated explanation. 



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

   <a href="https://github.com/JasonJWilliamsNY/leptin-rna-seq-lesson-dev" target="blank">Github Repo Link</a>
