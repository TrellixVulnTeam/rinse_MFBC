from rinse import installr
from pkg_resources import resource_filename
from os.path import expanduser, abspath
import click
from rinse.core import InstallR

INSTALLR = resource_filename(installr.__name__, "installr.sh")


@click.command()
@click.option("--path", "-p", default="~/.rinse",
              help="Select an installation path for R.")
@click.option("--version", "-v", default="latest",
              help="Select the version of R to install.")
@click.option("--repos", "-r", default="http://cran.rstudio.com")
def rinse(version, path, repos):

    # Normalize paths
    path = abspath(expanduser(path))

    # Build URL
    if version == "latest":
        url = f"{repos}/src/base/R-latest.tar.gz"
    else:
        major_version = version[0:1]
        url = f"{repos}/src/base/R-{major_version}/R-{version}.tar.gz"
    method = None

    rinse = InstallR(path=path, version=version, method=method, url=url)
    rinse.install()

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
