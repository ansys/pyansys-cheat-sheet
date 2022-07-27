PyAnsys Cheat Sheats
====================

Introduction
------------
This repository contains the cheat sheats for different pyansys library.

To make cheatsheat using this template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make a new cheat sheat :

- make a folder inside the `<cheat_sheats>`_ in the project name.
  for example: 
        pymapdl_cheat_sheat.
- copy the `pyansys_cheat_sheat.tex` inside the new folder from `<cheat_sheat_template>_` .
- Rename the `pyansys_cheat_sheat.tex` inside your folder to a format of  `your_project_chatsheat.tex`

Inside the tex file:
^^^^^^^^^^^^^^^^^^^^

- Change the pdf title from `PyAnsys Cheat sheat` to the project title.
- Add subject and keywords in pdfinfo.
- Change the title of cheatsheat from `Cheat sheet for PYANSYS` to the project title.
- Change the session name in `Add heading here` 
- Add discription of the session in `add description of code block here`.
- Add the python code in the block `ADD code here`.
- Add the following code if you have more than one code block for one session: 
    \begin{lstlisting}[language=Python]

    ADD code here

    \end{lstlisting} 
- add references to the documentation in the `References from PyAnsys Documentation`  
   and replace the link name with the reference name 
   Example:
   
        item \href{https://dev.docs.pyansys.com/}{\color{blue}{PyAnsys dev-guide}}
   
   link the dev-guide in blue color with name in pdf as Pyansys dev-guide.

To Generate cheatsheat
~~~~~~~~~~~~~~~~~~~~~~ 
- Add new makefile command in makefile as:
    <your_project>_cheatsheat:
	    latexmk -f -pdf -use-make cheat_sheats/<your_folder_name>/<your_tex_file_name>.tex -cd -outdir=../../$(BUILD) -interaction=nonstopmode || true

- Add the command to make all in makefile