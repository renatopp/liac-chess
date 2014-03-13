import sys
import cx_Freeze

base = None
target_name = 'liac_chess'
if sys.platform == "win32":
    base = "Win32GUI"
    target_name = 'liac_chess.exe'

def main():
    executables = [cx_Freeze.Executable(
            "main.py",
            targetName=target_name,
            base=base,
    )]

    freezer = cx_Freeze.Freezer(executables,
            includes=[],
            excludes=['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 
                 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 
                 'tcl', 'Tkconstants', 'Tkinter'],
            replacePaths=[],
            compress=True,
            optimizeFlag=1,
            copyDependentFiles=True,
            initScript=None,
            base=None,
            path=None,
            createLibraryZip = False,
            appendScriptToExe = True,
            targetDir=None,
            zipIncludes=[],
            includeFiles=['assets/', 'docs/', 'data/'],
            icon='assets/ico/liac_chess.ico',
            silent=None)
    freezer.Freeze()

if __name__ == '__main__':
    main()