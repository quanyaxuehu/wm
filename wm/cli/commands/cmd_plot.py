
import click

from wm.plot.plot_start import  plot_start
@click.command(short_help = 'This is a test for using rpy2')
@click.option('-x',help = 'column name of x')
@click.option('-y',help = 'column name of y')

def plot(x,y):
    plot_start(x,y)

## how to use: wm plot -x wt -y mpg