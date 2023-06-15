PyAnsys cheat sheets
====================

Introduction
------------
This repository contains cheat sheets for PyAnsys libraries. Procedures follow for creating
and deploying a cheat sheet.

Create cheat sheet
~~~~~~~~~~~~~~~~~~
You use a template to create a cheat sheet. Here is the procedure to follow:

#. In the `<cheat_sheets>`_ folder, create a child folder with an appropriate project
   name. For example, ``pymapdl_cheat_sheet``.
#. In the `<template>`_ folder, copy ``pyansys_cheat_sheet.tex`` and then
   paste it into your new project folder.
#. Rename this copy of ``pyansys_cheat_sheet.tex`` so that it uses your project folder
   name. For example, ``pymapdl_cheat_sheet.tex``.
#. Inside this LaTeX file, do the following:

   #. Change the PDF title from ``PyAnsys Cheat Sheet`` to your project title.
   #. In ``pdfinfo``, add a subject and keywords.
   #. Change the title of the cheat sheet from ``Cheat sheet for PyAnsys`` to
      `Cheat sheet for <project title>``
   #. In ``Add heading here``, add the heading name.
   #. In ``Add description of code block here``, add a description.
   #. In the block ``Add code here``, add the Python code.
   #. If you have more than one code block, add the following code:

      .. code:: TeX

            \begin{lstlisting}[language=Python]
            Add code here
            \end{lstlisting} 

#. In ``References from PyAnsys documentation``, add references to the library's documentation,
   replacing link names with the names of the guides. For example, this reference adds a link to
   the *PyAnsys Developer's Guide*:

   .. code:: TeX

        item \href{https://dev.docs.pyansys.com/}{\color{blue}{PyAnsys Developer's Guide}}

Generate cheat sheet
~~~~~~~~~~~~~~~~~~~~

**For Linux users**


#. In ``makefile``, add a new makefile command:

   .. code:: bash

        <your_project>_cheat_sheat:
	        latexmk -f -pdf -use-make cheat_sheats/<your_folder_name>/<your_tex_file_name>.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true
           convert -density 150 -scene 1 $(BUILD_DIR)/<your_tex_file_name>.pdf $(BUILD_DIR)/<your_tex_file_name>.png

   Here, replace ``<your_project>``, ``<your_folder_name>``, and ``<your_tex_file_name>`` with your actual project name, folder name, and TeX file name, respectively.
   This command uses latexmk to compile your TeX file into a PDF, and then convert the first page of the PDF into a PNG file.

#.  In ``makefile``, add this command to ``make all``.

**For Windows users**

#. In ``make.bat``, add a new makefile command:

   .. code:: bash

         :<your_project>_cheat_sheet
            pdflatex -output-directory=%BUILDDIR% cheat_sheats/<your_folder_name>/<your_tex_file_name>.tex --interaction=nonstopmode
            goto end

   Here, replace ``<your_project>``, ``<your_folder_name>``, and ``<your_tex_file_name>`` with your actual project name, folder name, and TeX file name, respectively.
   This command uses latexmk to compile your TeX file into a PDF.

#.  In ``make.bat``, add this command to ``all``.


Generate cheat sheets using docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Cheatsheet Development Environment Using Docker <https://github.com/ansys/pyansys-cheat-sheet/tree/main/docker>_` contains
the steps to build and run the Docker container, which includes all the necessary dependencies for cheatsheet development with PyAnsys.

Add cheat sheet in landing page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``index.rst`` in ``doc/source``, add a new grid item card for your cheatsheet by adding the following command:


.. code:: bash

   .. grid-item::

           .. card:: <Your_project_name>
               :img-top: https://cheatsheets.docs.pyansys.com/<your_tex_file_name>.png
               :link: https://cheatsheets.docs.pyansys.com/<your_tex_file_name>.pdf


Cheat sheets
~~~~~~~~~~~~~

In the `Documentation <https://cheatsheets.docs.pyansys.com/>`_ page, you can find a comprehensive collection of cheat sheets specifically 
designed for various PyANSYS products. These cheat sheets are carefully crafted to provide concise and practical information, serving as 
valuable references for your development or learning journey with PyANSYS. Feel free to post issues and other questions 
at `Pyansys cheat sheet issues <https://github.com/ansys/pyansys-cheat-sheet/issues>`_. This is the best place to post questions and code.