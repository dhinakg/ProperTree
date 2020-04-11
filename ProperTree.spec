# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ProperTree.command', 'Scripts/plist.py', 'Scripts/plistwindow.py', 'Scripts/run.py', 'Scripts/utils.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += Tree('./Scripts', prefix='Scripts')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ProperTree',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          windowed=False,
          icon="Scripts/shortcut.ico")
app = BUNDLE(exe,
         name='ProperTree.app',
         icon="Scripts/shortcut.icns",
         bundle_identifier='com.corpnewt.ProperTree',
         info_plist={
            'NSRequiresAquaSystemAppearance': False,
            "CFBundleShortVersionString": "0.0",
            "CFBundleSignature": "????",
            "CFBundleInfoDictionaryVersion": "0.0",
            "NSHumanReadableCopyright": "Copyright 2020 CorpNewt", 
            "CFBundleDocumentTypes": [
                {
                    "CFBundleTypeName": "Property List",
                    "CFBundleTypeRole": "Viewer",
                    "CFBundleTypeIconFile": "plist",
                    "CFBundleTypeExtensions": [
                    "plist"
                    ]
                }
            ],
            "CFBundleDevelopmentRegion": "English",
            "CFBundleExecutable": "ProperTree",
            "CFBundleName": "ProperTree",
            "LSMinimumSystemVersion": "10.4",
            "LSMultipleInstancesProhibited": True,
            "CFBundlePackageType": "APPL",
            "CFBundleVersion": "0.0"
            },
         )
