PyAnsys cheat sheets
====================

Introduction
------------
This repository contains cheat sheets for PyAnsys libraries. In the
`PyAnsys Cheat Sheet documentation <https://cheatsheets.docs.pyansys.com/>`_,
you can see the cheat sheets that have been released for various PyAnsys
libraries. These cheat sheets are carefully crafted to provide concise and
practical information, serving as valuable references. On the
`PyAnsys Cheat Sheet Issues <https://github.com/ansys/pyansys-cheat-sheet/issues>`_
page, you can create issues to report bugs and request new features. On the
`PyAnsys Cheat Sheet Discussions <https://github.com/ansys/pyansys-cheat-sheet/discussions>`_
page or the `Discussions <https://discuss.ansys.com/>`_ page on the Ansys Developer portal,
you can post questions, share ideas, and get community feedback..

The following sections describe how to create, generate, and deploy a PyAnsys cheat sheet.

Create a cheat sheet
~~~~~~~~~~~~~~~~~~~~
You create a cheat sheet from a template as indicated in these steps:

#. In the `<cheat_sheets>`_ folder, create a child folder with an appropriate project
   name. For example, ``pymapdl_cheat_sheet``.
#. In the `<template>`_ folder, copy ``pyansys_cheat_sheet.tex`` and then
   paste it into your new project folder.
#. Rename this copy of ``pyansys_cheat_sheet.tex`` so that it uses your project folder
   name. For example, ``pymapdl_cheat_sheet.tex``.
#. Inside this LaTeX file, do the following:

   #. In the ``pdfinfo`` element, change the PDF title from ``PyAnsys cheat sheet`` to
      your project title and then add a subject and keywords.
   #. Under the ``Add the title of cheat sheet here`` comment, change the title from
      ``PyAnsys cheat sheet`` to ``<project title> cheat sheet``.

      The next several steps explain how to complete the ``section`` element for each
      of the cheat sheet's three columns.

   #. Replace the ``Add heading here`` text with the column heading.
   #. Replace the ``Add description of code block here`` text with a description.
   #. Replace the ``Add code here`` text with a Python code block.
   #. If you have more than one code block, add the following code:

      .. code:: TeX

            \begin{lstlisting}[language=Python]
            Add code here
            \end{lstlisting} 

#. In the ``References from PyAnsys documentation`` subsection, add references to the
   library's documentation, replacing link names with the names of the guides. For example,
   this reference adds a link to the *PyAnsys Developer's Guide*:

   .. code:: TeX

        item \href{https://dev.docs.pyansys.com/}{\color{blue}{PyAnsys Developer's Guide}}

Generate the cheat sheet
~~~~~~~~~~~~~~~~~~~~~~~~

**For Linux users**


#. In the root directory of the repository, open the ``makefile`` file and add this command in
the ``all: $(CHEATSHEETS)`` section:

   .. code:: bash

        <your_project>_cheat_sheat:
	        latexmk -f -pdf -use-make cheat_sheats/<your_folder_name>/<your_tex_file_name>.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true
           convert -density 150 -scene 1 $(BUILD_DIR)/<your_tex_file_name>.pdf $(BUILD_DIR)/<your_tex_file_name>.png

#. In this new comand, replace ``<your_project>``, ``<your_folder_name>``, and ``<your_tex_file_name>``
   with your actual project name, folder name, and TeX filename, respectively.

   This command uses ``latexmk`` to compile your TeX file into a PDF and then converts the first page of the PDF into a PNG file.

#.  At the top of the file, in the ``CHEATSHEETS=`` line, add the project name of your cheat sheet.

**For Windows users**

#. In the root directory of the repository, open the ``makefile`` file and add this command in
   the ``all: $(CHEATSHEETS)`` section:

   .. code:: bash

         :<your_project>_cheat_sheet
            pdflatex -output-directory=%BUILDDIR% cheat_sheats/<your_folder_name>/<your_tex_file_name>.tex --interaction=nonstopmode
            goto end

#. In this new command, replace ``<your_project>``, ``<your_folder_name>``, and ``<your_tex_file_name>``
   with your actual project name, folder name, and TeX filename, respectively.
   
   This command uses ``latexmk`` to compile your TeX file into a PDF.

#. In the root directory of the repository, open the ``make.bat`` file and add the ``CALL`` command for your project
   to the ``:all`` section.


Generate a cheat sheet using Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use Doker to generate a cheat sheet. Using Docker allows you to generate a cheat
sheet without worrying about dependencies and environment setup. The Docker container
includes all the necessary dependencies for cheat sheet development. For more information,
see the `README.md <https://github.com/ansys/pyansys-cheat-sheet/tree/main/docker>_`
file in the repository's ``docker`` folder.

Deploy a cheatsheet
~~~~~~~~~~~~~~~~~~~

Once your cheat sheet is approved for release, you can deploy it by adding it to the
`PyAnsys Cheat Sheets documentation <https://cheatsheets.docs.pyansys.com/>`_.

#. In the ``doc/source`` directory, open the ``index.rst`` file, which is the
   only page in the documentation.

#. To add a new grid item card for your cheat sheet, paste this code block where
   your cheat sheet should appear alphabetically in the grid:

.. code:: bash

   .. grid-item::

           .. card:: <your_project_name>
               :img-top: https://cheatsheets.docs.pyansys.com/<your_tex_file_name>.png
               :link: https://cheatsheets.docs.pyansys.com/<your_tex_file_name>.pdf

#. In this code block, replace ``<your_project_name>``, ``<your_tex_file_name>.png``, and
   ``<your_tex_file_name>.pdf`` with your actual project name and the TeX filenames for your PNG
   file and PDF file, respectively.

Additionally, ensure that links for viewing and downloading the cheat sheet are added to a
"Documentation and issues" section in both your PyAnsys library's README file and the overall
``index`` RST file for your library's documenation. For example, see this section in both
the ``README.rst`` file for the `PyFluent repository <https://github.com/ansys/pyfluent>`_ and the 
overall `index RST file <https://fluent.docs.pyansys.com/version/stable/>`_ for the PyFluent
documentation.
