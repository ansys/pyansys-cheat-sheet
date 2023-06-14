@ECHO OFF

pushd %~dp0

SET BUILDDIR=_build

if "%1" == "all" goto all
if "%1" == "pymapdl_cheat_sheet" goto pymapdl_cheat_sheet
if "%1" == "pyfluent_cheat_sheet" goto pyfluent_cheat_sheet
if "%1" == "pyaedt_API_cheat_sheet" goto pyaedt_API_cheat_sheet
if "%1" == "pyedb_API_cheat_sheet" goto pyedb_API_cheat_sheet
if "%1" == "pyprimemesh_cheat_sheet" goto pyedb_API_cheat_sheet
if "%1" == "pydpf-core" goto pydpf-core_cheat_sheet
if "%1" == "clean" goto clean
if "%1" == "help" goto help
if "%1" == "" goto help

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

:pydpf-core_cheat_sheet
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pydpf-core_cheat_sheet/pydpf-core_cheat_sheet.tex --interaction=nonstopmode
    goto end

:all
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/mapdl_cheat_sheet/pymapdl_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pyfluent_cheat_sheet/pyfluent_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/aedt_cheat_sheet/pyaedt_API_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/aedt_cheat_sheet/pyedb_API_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pyprimemesh_cheat_sheet/pyprimemesh_cheat_sheet.tex --interaction=nonstopmode
    pdflatex -output-directory=%BUILDDIR% cheat_sheets/pydpf-core_cheat_sheet/pydpf-core_cheat_sheet.tex --interaction=nonstopmode
    goto end

:clean
    rmdir /S /Q %BUILDDIR%

:help
@echo off

REM Display the help message
echo Available targets:
echo   all:         Build all cheat sheets
echo   clean:       Remove the build directory and temporary files
echo   help:        Show this help message
echo.
echo Individual Cheat Sheet Targets:
echo   pymapdl_cheat_sheet:       Build the pymapdl cheat sheet
echo   pyfluent_cheat_sheet:      Build the pyfluent cheat sheet
echo   pyaedt_API_cheat_sheet:    Build the pyaedt API cheat sheet
echo   pyedb_API_cheat_sheet:     Build the pyedb API cheat sheet
echo   pyprimemesh_cheat_sheet:   Build the pyprimemesh cheat sheet

:end
popd