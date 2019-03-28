from os import name as osname
from sys import platform as sysplat
import click
from rinse.core import InstallR, LInstallR, MacInstallR, WInstallR


@click.group()
@click.option("--install", default=None,
              help="Select the version of R to install.", show_default=True)
@click.option("--global", "-g", "glbl", default=None,
              help="Select the version of R available to your global environment.")
@click.option("--repos", "-r", default="http://cran.rstudio.com")
@click.option("--source", "method", flag_value="source", default=True, show_default=True)
@click.option("--spack", "method", flag_value="spack", show_default=True)
@click.option("--local", "method", flag_value="local", show_default=True)
@click.option("--path", "-p", default="~/.beRi",
              help="Select a relative installation path for rinse.", show_default=True)
@click.option("--name", "-n", default=".rinse",
              help="Select a name for the installation directory for R.", show_default=True)
# @click.option("--init", "-i", default=False, is_flag=True,
#             help="Initialize rinse using the /<path>/<name>.", show_default=True)
@click.option("--config_file", default=None,
              help="A text file for sending commands to the configure script that"
                   " configures R to adapt to many kinds of systems.", show_default=True)
@click.option("--config_help", default=False,
              help="Display the help message for configuring R.", show_default=True)
@click.option("--config_clear", "-c", default=list(["all"]), multiple=True,
              help="Remove any files associated with previous attempts to install R.", show_default=True)
@click.pass_context
def rinse(ctx, install, glbl, repos, method, path, name, config_file, config_help, config_clear):
    ctx['path'] = path
    ctx['name'] = name
    if path != "~/.beRi":
        raise NotImplementedError("Rinse only supports installing into the home directory at this time.")

    if osname == "posix":
        if sysplat == "darwin":
            rinstall = MacInstallR()
            rinstall.raise_error()
        elif "linux" in str(sysplat):
            rinstall = LInstallR(glbl=glbl, path=path, install=install, repos=repos, method=method, name=name, init=init,
                                 config_file=config_file, config_help=config_help, config_clear=config_clear)
            if install is not None:
                rinstall.installer()
        else:
            raise OSError("rinse does not support the %s operating system at this time." % sysplat)
    elif osname == "nt":
        if sysplat == "win32":
            rinstall = WInstallR()
            rinstall.raise_error()
        else:
            raise OSError("rinse does not support the %s operating system at this time." % sysplat)


@rinse.command(help="Initialize rinse using the /<path>/<name>.")
@click.pass_context
def init(ctx):
    # Initialize rinse
    InstallR(path=ctx['path'], name=ctx['name'])


@rinse.command()
@click.pass_context
def install(ctx):
    pass
