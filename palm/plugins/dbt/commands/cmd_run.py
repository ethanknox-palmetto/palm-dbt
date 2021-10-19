import click
from typing import Optional
from pathlib import Path

@click.command("run")
@click.option("--fast", is_flag=True, help="will skip clean/deps/seed")
@click.option("--no-fail-fast", is_flag=True, help="Disables the setting which exits immediately if a single model fails to build")
@click.option("--persist", is_flag=True, help="will not drop the test schema at the end")
@click.option("--models", multiple=True, help="see dbt docs on models flag")
@click.option("--select", multiple=True, help="see dbt docs on select flag")
@click.option("--macros", multiple=True, help="see dbt docs on run operations and macros")
@click.option("--full-refresh", is_flag=True, help="will perform a full refresh on incremental models")
@click.option("--no-seed", is_flag=True, help="will skip seed full refresh")
@click.pass_context
def cli(ctx,
        fast: bool,
        no_fail_fast: bool,
        persist: bool,
        full_refresh: bool,
        no_seed: bool,
        models: Optional[tuple] = tuple(),
        select: Optional[tuple] = tuple(),
        macros: Optional[tuple] = tuple()):
    """ Runs the DBT repo. """

    dbt_palm_utils = ctx.obj.import_module('dbt_palm_utils', Path(Path(__file__).parent, 'dbt_palm_utils.py'))

    cmd = dbt_palm_utils.shell_options("run", **locals())
    ctx.obj.run_in_shell(cmd)
