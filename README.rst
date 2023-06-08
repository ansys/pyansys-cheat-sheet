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
#. In the `<cheat_sheet_template>`_ folder, copy ``pyansys_cheat_sheet.tex`` and then
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
~~~~~~~~~~~~~~~~~~~~~~ 
#. In ``makefile``, add a new makefile command:

   .. code:: TeX

        <your_project>_cheatsheat:
	        latexmk -f -pdf -use-make cheat_sheats/<your_folder_name>/<your_tex_file_name>.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true
           convert -density 150 -scene 1 $(BUILD_DIR)/<your_tex_file_name>.pdf $(BUILD_DIR)/<your_tex_file_name>.png

Here, replace <your_project>, <your_folder_name>, and <your_tex_file_name> with your actual project name, folder name, and TeX file name, respectively.
This command uses latexmk to compile your TeX file into a PDF, and then convert the first page of the PDF into a PNG file.

#.  In ``makefile``, add this command to ``make all``.

Cheat sheets
~~~~~~~~~~~~

`download PyMAPDL cheatsheet pdf <https://cheatsheets.docs.pyansys.com/pymapdl_cheat_sheet.pdf>`_

.. image:: https://cheatsheets.docs.pyansys.com/pymapdl_cheat_sheet.png
   :alt: pymapdl cheatsheet snapshot
   :width: 50%           
   

`download PyFluent cheatsheet pdf <https://cheatsheets.docs.pyansys.com/pyfluent_cheat_sheet.pdf>`_

.. image:: https://cheatsheets.docs.pyansys.com/pyfluent_cheat_sheet.png
   :alt: pyfluent cheatsheet snapshot
   :width: 50%

`download PyAEDT API cheatsheet pdf <https://cheatsheets.docs.pyansys.com/pyaedt_API_cheat_sheet.pdf>`_

.. image:: https://cheatsheets.docs.pyansys.com/pyaedt_API_cheat_sheet.png
   :alt: pyaedt API cheatsheet snapshot
   :width: 50%

`download PyEDB API cheatsheet pdf <https://cheatsheets.docs.pyansys.com/pyedb_API_cheat_sheet.pdf>`_

.. image:: https://cheatsheets.docs.pyansys.com/pymapdl_cheat_sheet.png
   :alt: pyedb API cheatsheet snapshot
   :width: 50%   

`download PyPrimeMesh API cheatsheet pdf <https://cheatsheets.docs.pyansys.com/pyprimemesh_cheat_sheet.pdf>`_

.. image:: https://cheatsheets.docs.pyansys.com/pyprimemesh_cheat_sheet.png
   :alt: PyPrimeMesh cheatsheet snapshot
   :width: 50%   