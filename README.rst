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
       your project title.
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

#. In ``makefile``, add this command to ``make all``.

   
