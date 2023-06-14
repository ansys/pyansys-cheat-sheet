@ECHO OFF

pushd %~dp0

SET BUILDDIR=_build
SET CHEATSHEETS=pymapdl_cheat_sheet pyfluent_cheat_sheet pyaedt_API_cheat_sheet pyedb_API_cheat_sheet

rem Note: If you are using make.bat file for building locally, change L2 of .tex files from 
rem ``\usepackage{{./../static/style}}`` to ``\usepackage{{.\..\static\style}}``

all: %CHEATSHEETS% 

if "%1" == "pymapdl_cheat_sheet" goto pymapdl_cheat_sheet
if "%1" == "pyfluent_cheat_sheet" goto pyfluent_cheat_sheet
if "%1" == "pyaedt_API_cheat_sheet" goto pyaedt_API_cheat_sheet
if "%1" == "pyedb_API_cheat_sheet" goto pyedb_API_cheat_sheet
if "%1" == "pyprimemesh_cheat_sheet" goto pyedb_API_cheat_sheet
if "%1" == "clean" goto clean

:pymapdl_cheat_sheet
    pdflatex -include-directory="cheat_sheets\mapdl_cheat_sheet" -output-directory=%BUILDDIR% pymapdl_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyfluent_cheat_sheet
    pdflatex -include-directory="cheat_sheets\pyfluent_cheat_sheet" -output-directory=%BUILDDIR% pyfluent_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyaedt_API_cheat_sheet
    pdflatex -include-directory="cheat_sheets\aedt_cheat_sheet" -output-directory=%BUILDDIR% pyaedt_API_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyedb_API_cheat_sheet
    pdflatex -include-directory="cheat_sheets\aedt_cheat_sheet" -output-directory=%BUILDDIR% pyedb_API_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyprimemesh_cheat_sheet
    pdflatex -include-directory="cheat_sheets\pyprimesh_cheat_sheet" -output-directory=%BUILDDIR% pyprimemesh_cheat_sheet.tex --interaction=nonstopmode
    goto end

:clean
    rmdir /S /Q %BUILDDIR%

:end
popd