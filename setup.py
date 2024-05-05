from classes.utils.package import PackageManager as PkgMngr

if __name__ == '__main__':
    pkg = PkgMngr(PkgMngr.getPkg())
    pkg.install()
