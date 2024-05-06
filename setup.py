from classes.utils.package import PackageManager as PkgMngr
from classes.utils.fileinit import InitFilesGenerator as initFile

if __name__ == '__main__':
    pkg = PkgMngr(PkgMngr.getPkg())
    pkg.install()
