from classes.package import PackageManager as PkgMn

if __name__ == '__main__':
    pkg = PkgMn(PkgMn.getPkg())
    pkg.install()
