.. include:: defined_substitutions.txt

Glossary
========

Term one:
~~~~~~~~~~

Each term is Heading3 followed by one or more lines of text.

Term two
~~~~~~~~~

Term three
~~~~~~~~~~

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
