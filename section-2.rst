.. include:: defined_substitutions.txt

JupyterLab primer
===================

  .. admonition:: learning-objectives

     - Understand how to navigate JupyterLab
     - Understand how to use a Jupyter notebook
     - Understand how to edit a Jupyter notebook
     - Access the command line using JupyterLab


Intro to Jupyter and JupyterLab
---------------------------------

|Jupyter| is an open source project that develops platforms for users to run
code in a way that prioritizes effective communication. Instead of long lines
of code (which often end up poorly documented), Jupyter platforms such as
JupyterLab mixes blocks of explanatory text with code and visualizations.

Many people are used to using computers with a graphical interface (GUI,
pronounced "gooey"), i.e. point-and-click interfaces. However, most scientific
software is usually has a command line interface - every instruction is in the
form of written text. Although the command line can take time to learn, it is
preferred by researchers because every command is documented and unambiguous.

Jupyter mixes GUI and command line by allowing you to see the commands needed to
run software and the using a the GUI execute the command. Even if you don't
know command line you can start to understand how the software works, or even
modify it.

This primer will teach you enough about Jupyter to complete the lesson using
|CyVerse| (We will not cover setting up and instally JupyterLab). To learn more
about Jupyter visit the |Jupyter| website and also see the full set of
|JupyterLab documentation|.

Navigate Jupyter Lab
-----------------------

  .. note::

    This documentation will not cover all elements of the lab interface, only
    what is needed to complete subsequent lessons. For a full explanation
    see the |JupyterLab documentation|.

**Navigation Sidebar**

Upon starting JupyterLab you will see the JupyterLab workspace. On the left
sidebar you will see individual files. You can navigate and open files from
this menu.


|Navigate gif|

Using the Launcher to Run and Edit Jupyter Notebooks
-----------------------------------------------------

|Jupyter Notebooks| are documents that allow you to combine text, code, images,
and other interactive objects. Tutorials will typically be made up of one or
more notebooks (which have the .ipynb file extension). To show you how a
notebook works, we will use the Launcher to create a notebook.

  1. From the **Launcher** click *Python 3* - this will launch a notebook
     enabling you to run code written in the Python language.

     |Launch Python|

  .. tip::

       There is a launch button for other code languages your JupyterLab
       supports. Jupyter supports a wide variety of languages including
       Python, R, Julia, and others - though your specific installation
       may vary.

  2. Everything done in a notebook is done in a **cell**. Cells can be *code*
     (some code you want to run) or |Markdown| - a form of HTML you can use
     to write text. Cells can also be *Raw* but we won't address that here.
     A dropdown menu at the top of the notebook allows you to choose the
     type of cell you want.

     |Cell types|

  3. To run some code, type the code into a code cell, and then press the play
     button to run the code.

     |code cell|

  4. To enter text, links, or images change the cell type to **Markdown** and
     use |Markdown| format to enter your text.

     |markdown cell|


  .. note::

      In a tutorial, cells will often be pre-filled with code (or which you must
      complete!). Cells can be one one of three states:

      - **Unrun Cells**: If a cell has not been run, the brackets next to the
        cell will be empty.

        |unrun cell|

      - **Running Cells**: If a cell is running, there will be an '\*' until the
        cell code completes. You can use the stop button at the top of the
        notebook to stop the execution of a cell.

        |running cell|

      - **Run Cells**: Once a cell has been run, a number will appear. Every time
        a code cell is executed, the number displayed will increment up.

        |run cell|

  5. You can edit any cell by rewriting the code or text in the cell. Click the
     disk/save icon or choose **Save Notebook** from the file menu to save
     your changes.

  6. Use the '+' button at the top of the notebook to add more cells.

  7. Above the navigation panel press the '+' button to get back to the Launcher.

Notebook Tips
--------------

Some additional tips for working with your notebooks:

 1. There are a number of keyboard shortcuts you can use to add, delete, run
    cells:

    - cntrl+enter : Run a cell
    - b: New cell below
    - dd (press 'd' twice): Delete cell

    See the Edit menu for popular functions and shortcut keys

 2. Right-clicking on a notebook in the navigation panel allows you
    to use some helpful functions including:

    - Renaming a notebook
    - Downloading a notebook

 3. In the **Kernel** menu you can shutdown and restart a notebook which has
    stalled for some reason. Try **Interrupt Kernel** or **Restart Kernel** if
    your notebook freezes and no longer responds to commands.

Using the Bash Terminal in Jupyter Lab
----------------------------------------

The Linux |Bash| terminal is also accessible using JupyterLab. How your terminal
is configured will depend on how your JupyterLab instance has been setup. To
Access the terminal, go to the launcher and click **Terminal**.

|bash terminal|


----


 .. |Navigate gif| image:: ./img/jupyter_navigate.gif
    :width: 600
    :height: 400

 .. |Launch Python| image:: ./img/launch_python_notebook.png
    :width: 350
    :height: 175

 .. |Cell types| image:: ./img/cell_types.png
    :width: 350
    :height: 100

 .. |code cell| image:: ./img/code_cell.gif
    :width: 350
    :height: 100

 .. |markdown cell| image:: ./img/markdown_cell.gif
    :width: 350
    :height: 100

 .. |unrun cell| image:: ./img/unrun_cell.png
    :width: 25
    :height: 25

 .. |running cell| image:: ./img/running_cell.png
    :width: 25
    :height: 25

 .. |run cell| image:: ./img/run_cell.png
    :width: 25
    :height: 25

 .. |bash terminal| image:: ./img/bash_terminal.png
    :width: 600
    :height: 150



..
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
