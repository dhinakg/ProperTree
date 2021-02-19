#!/usr/bin/env bash
# mkdir dist/lib
# cp -R /usr/local/Cellar/tcl-tk/8.6.10/lib/tcl* dist/lib/
# mkdir dist/ProperTree.app/Contents/Resources/lib
# cp -Rf /usr/local/Cellar/tcl-tk/8.6.10/lib/tcl* dist/ProperTree.app/Contents/Resources/lib/
# chmod -R 755 dist/ProperTree.app/Contents/Resources/lib/
# ln -s Resources/lib dist/ProperTree.app/Contents/
rm -f dist/ProperTree.app.zip
cd dist
zip -r ProperTree.app.zip ProperTree.app