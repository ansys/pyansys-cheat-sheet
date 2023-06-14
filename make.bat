@ECHO OFF

pushd %~dp0

SET BUILDDIR=_build

rem Note: If you are using make.bat file for building locally, change L2 of .tex files from 
rem ``\usepackage{{./../static/style}}`` to ``\usepackage{{.\..\static\style}}``


if "%1" == "all" goto all
if "%1" == "pymapdl_cheat_sheet" goto pymapdl_cheat_sheet
if "%1" == "pyfluent_cheat_sheet" goto pyfluent_cheat_sheet
if "%1" == "pyaedt_API_cheat_sheet" goto pyaedt_API_cheat_sheet
if "%1" == "pyedb_API_cheat_sheet" goto pyedb_API_cheat_sheet
if "%1" == "pyprimemesh_cheat_sheet" goto pyedb_API_cheat_sheet
if "%1" == "clean" goto clean

:pymapdl_cheat_sheet
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyfluent_cheat_sheet
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyaedt_API_cheat_sheet
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/aedt_cheat_sheet/pyaedt_API_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyedb_API_cheat_sheet
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/aedt_cheat_sheet/pyedb_API_cheat_sheet.tex --interaction=nonstopmode
    goto end

:pyprimemesh_cheat_sheet
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pyprimemesh_cheat_sheet/pyprimemesh_cheat_sheet.tex --interaction=nonstopmode
    goto end

:all
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/aedt_cheat_sheet/pyaedt_API_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/aedt_cheat_sheet/pyedb_API_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pyprimemesh_cheat_sheet/pyprimemesh_cheat_sheet.tex --interaction=nonstopmode
    goto end

:clean
    rmdir /S /Q %BUILDDIR%

:end
popd