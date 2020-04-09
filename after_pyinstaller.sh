#!/usr/bin/env bash
mkdir dist/ProperTree.app/Contents/Resources/lib
cp -R /usr/local/Cellar/tcl-tk/8.6.10/lib/tcl* dist/ProperTree.app/Contents/Resources/lib/
ln -s Resources/lib dist/ProperTree.app/Contents/