import click

@click.group()
def cli():
    pass

@cli.command('haha',help = 'haha')
@click.option('--count', default=1, help='please enter a count')
@click.option('--name', help='please enter your name')

def hello(count,name):
    """"I don't know what is this"""
    for i in range(count):
        print('hello', name,'!')


##看看不用子命令的方法：需要直接放到cli()函数中，而不是另起一个函数
# @click.command('hello', short_help='Iode.')
# @click.option('--count', default=1, help='please enter a count')
# @click.option('--name', help='please enter your name')

# def cli(count,name):
#     """"I don't know what is this"""
#     for i in range(count):
#         print('hello', name,'!')
#
# if __name__ == '__main__':
#     cli()
