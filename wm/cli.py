
import os
import sys
import click


CONTEXT_SETTINGS = dict(auto_envvar_prefix='DEMO')


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))


class SdnadmCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    # def get_command(self, ctx, cmd_name):
    #     list_commands = self.list_commands(ctx)
    #     if cmd_name in set(list_commands):
    #         name = cmd_name
        #return name

    def get_command(self, ctx, cmd_name):
        list_commands = self.list_commands(ctx)
        if cmd_name in set(list_commands):
            name = cmd_name
            try:
                if sys.version_info[0] == 2:
                    name = name.encode('ascii', 'replace')
                    # 将字符串处理成只有UTF-8字符
                mod = __import__('wm.commands.cmd_' + name,
                                 None, None, name)
                method = getattr(mod, name)
            except ImportError:
                return
            return method
        else:
            pass

    # def get_command(self, ctx, name):
    #     try:
    #         if sys.version_info[0] == 2:
    #             print(name)
    #             name = name.encode('ascii', 'replace')
    #             print(name)
    #             #将字符串处理成只有UTF-8字符
    #         mod = __import__('wm.commands.cmd_' + name,
    #                          None, None, ['cli'])
    #     except ImportError:
    #         return
    #     return mod.cli


@click.command(cls=SdnadmCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True,
              help='show debug message.')
@pass_context
def cli(ctx, verbose):
    """wm tools"""
    ctx.verbose = verbose


if __name__ == '__main__':
    cli()
