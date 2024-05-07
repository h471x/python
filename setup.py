from classes.utils.package import PackageManager as PkgMngr
from classes.utils.filerunner import FileRunner as runFile

if __name__ == '__main__':
    pkg = PkgMngr(PkgMngr.getPkg())
    pkg.install()

    postgresConf = runFile('config/postgres/postgresql.sh')
    postgresConf.runShell()
