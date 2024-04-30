from classes.package import PackageManager as PkgMgt

if __name__ == '__main__':
    pkg = PkgMgt(PkgMgt.getPkg())
    pkg.install()
