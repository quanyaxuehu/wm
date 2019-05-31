

from rpy2.robjects.packages import importr
from glob import glob
import warnings

def plot_start(x,y):
    import rpy2.robjects.lib.ggplot2 as ggplot2
    ##由于这一条import会有警告信息，放到这里，只有调用这个函数才会出现警告。
    utils = importr('utils')
    data= utils.read_csv(glob('*.csv')[0])
    plot = ggplot2.ggplot(data)
    plot = (plot
          + ggplot2.aes_string(x=x, y=y)
          + ggplot2.geom_point()
          + ggplot2.scale_colour_gradient(low="yellow", high="red")
          + ggplot2.labs(title="mtcars", x='wt', y='mpg'))
    plot.save('point.png')
if __name__ =='__main__':
    plot_start()








