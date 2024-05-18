from classes.utils.package import PackageManager as PkgMngr
from classes.utils.filerunner import FileRunner as RunFile

if __name__ == '__main__':
    pkg = PkgMngr(PkgMngr.get_pkg())
    pkg.install()

    postgres_conf = RunFile('config/postgres/postgresql.sh')
    postgres_conf.run_shell()
