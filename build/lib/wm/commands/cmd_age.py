
import click
from wm.cli import pass_context

@click.command('test', short_help='This is just a test for wm')
@pass_context
def cli(ctx):
    ctx.log('This is not important')
    ctx.vlog('wm yayaya')
