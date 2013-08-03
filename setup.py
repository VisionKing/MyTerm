# -*- coding:utf-8 -*-

from distutils.core import setup
import sys
import py2exe

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
#     sys.argv.append("-q")
     
manifest_template = ''' 
<assembly xmlns="urn:schemas-microsoft-com:asm.v1"
manifestVersion="1.0">
<assemblyIdentity
version="0.6.8.0"
processorArchitecture="x86"
name="%(prog)s"
type="win32"
/>
<description>%(prog)s</description>
<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
<security>
<requestedPrivileges>
<requestedExecutionLevel
level="asInvoker"
uiAccess="false"
/>
</requestedPrivileges>
</security>
</trustInfo>
<dependency>
<dependentAssembly>
<assemblyIdentity
type="win32"
name="Microsoft.VC90.CRT"
version="9.0.21022.8"
processorArchitecture="x86"
publicKeyToken="1fc8b3b9a1e18e3b"
/>
</dependentAssembly>
</dependency>
<dependency>
<dependentAssembly>
<assemblyIdentity
type="win32"
name="Microsoft.Windows.Common-Controls"
version="6.0.0.0"
processorArchitecture="x86"
publicKeyToken="6595b64144ccf1df"
language="*"
/>
</dependentAssembly>
</dependency>
</assembly>
''' 


myOptions = {
    "py2exe":{
        "compressed": 1,
        "optimize": 2,
        "ascii": 1,
#         "includes":,
        "dll_excludes": ["MSVCP90.dll","w9xpopen.exe"],
        "bundle_files": 2
     }
}

RT_MANIFEST = 24

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        
MyTerm_windows = Target(
    # used for the versioninfo resource
    copyright = "Copywrong All Lefts Unreserved.",
    name = 'MyTerm',
    version = '1.1',
    description = 'MyTerm',
    author = 'gamesun',
    url = r'https://github.com/gamesun/MyTerm',
    
    # what to build
    script = "main.py",
    dest_base = "MyTerm",
    icon_resources = [(1, "icon\icon.ico")],
    other_resources= [(RT_MANIFEST, 1, manifest_template % dict(prog = "MyTerm"))]
)

setup(
    options = myOptions,
#     zipfile = None,
#     zipfile = "lib/shared.zip",
#    data_files = [('', ['icon\icon16.ico',])],
    windows = [MyTerm_windows]
)