
import click
from glob import glob
from rpy2.robjects.packages import importr
from wm.plot.rpy2plots import *
#data,x,y,group=None,title='Scatter Plot',gradient=None,ellipse:dict=False,label:bool=False,subbox=False,save=None,color=None,shape=None

@click.group()
def ggplot():
    pass
@click.command()
@click.option('-d','-data',help = 'input data')
@click.option('-x',help = 'column name of x')
@click.option('-y',help = 'column name of y')
@click.option('-s','-save',help = 'output files')
def scatter(d,x,y,s):
    utils = importr('utils')
    data = utils.read_csv(glob(d)[0])
    scatter_plot(data = data,x = x,y = y,save=s)

@click.command()
@click.option('-d','-data',help = 'input data')
@click.option('-g','-group',help = 'group')
@click.option('-y',help = 'column name of y')
@click.option('-s','-save',help = 'output files')
def box(d,g,y,s):
    utils = importr('utils')
    data = utils.read_csv(glob(d)[0])
    box_plot(data = data,group = str(g),y = y,save=s)
    ##problem not fixed: if group is int, fig will not be normal.

ggplot.add_command(scatter)
ggplot.add_command(box)


if __name__ == "__main__":
    ggplot()





## how to use: wm plot -x wt -y mpg