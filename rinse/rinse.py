from rinse import installr
from pkg_resources import resource_filename
from os import name as osname
from sys import platform as sysplat
import click
from rinse.core import LInstallR, MacInstall, WInstallR


@click.command()
@click.option("--path", "-p", default="~/",
              help="Select a relative installation path for R.")
@click.option("--version", "-v", default="latest",
              help="Select the version of R to install.")
@click.option("--repos", "-r", default="http://cran.rstudio.com")
@click.option("--source", "method", flag_value="source", default=True)
@click.option("--spack", "method", flag_value="spack")
@click.option("--local", "method", flag_value="local")
@click.option("--init", "-i", default=False,
              help="Initialize rinse.")
@click.option("--name", "-n", default=".rinse",
              help="Select a name for the installation directory for R.")
def rinse(path, name, version, repos, method, init):

    if osname == "posix":
        if sysplat == "darwin":
            rinstall = MacInstall()
            rinstall.raise_error()
        elif "linux" in str(sysplat):
            rinstall = LInstallR(path=path, version=version, repos=repos, method=method, name=name, init=init)
            rinstall.install()
        else:
            raise OSError("rinse does not support the %s operating system at this time." % sysplat)
    elif osname == "nt":
        if sysplat == "win32":
            rinstall = WInstallR()
            rinstall.raise_error()
        else:
            raise OSError("rinse does not support the %s operating system at this time." % sysplat)

    # Create temporary directory and files
    # tmp_dir = mkdtemp()
    # script_path = f"{tmp_dir}/script.sh"
    # script = import_temp(INSTALLR)
    # stdout = f"{tmp_dir}/stdout.txt"
    # stderr = f"{tmp_dir}/stderr.txt"
    # updated_script = script.safe_substitute(version=version, path=path,
    #                                         url=url, tmp_dir=tmp_dir,
    #                                         stdout=stdout, stderr=stderr)
    # with open(script_path, "w") as out:
    #     out.write(updated_script)
    #
    # # Run updated installation script
    # click.echo(f"$ bash {script_path}")
    # install_proc = run(["bash", script_path])
    # if install_proc.returncode != 0:
    #     click.echo(f"Check the following files for installation output:\n"
    #                f"  - {stdout}\n  - {stderr}")
