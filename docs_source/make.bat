@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build

set BUILDMODE=%1

if "%1" == "github" (
    set BUILDMODE=html
)

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

python build_definitions.py
rmdir /s /q %BUILDDIR%
%SPHINXBUILD% -M %BUILDMODE% %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

if "%1" == "github" (
    rmdir /s /q ..\docs
    robocopy %BUILDDIR%/html ../docs /E > nul
    echo.Generated files copied to ../docs
	python trim.py ../docs/index.html
)

goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
