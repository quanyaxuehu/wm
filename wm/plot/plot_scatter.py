#!/usr/bin/python3
'''
this script contains function to draw scatter plots using python and rpy2
'''
import rpy2.robjects as ro
import rpy2.robjects.packages as rpkg
from rpy2.robjects.packages import importr
import rpy2.robjects.lib.ggplot2 as gg2
gg = gg2.ggplot2

def scatter_plot(data,x,y,group=None,title='Scatter Plot',gradient=None,ellipse:dict=False,label:bool=False,subbox=False,save=None,color=None,shape=None):
    plot = gg2.ggplot(data) + gg.geom_point(size=3) +gg.aes_string(x=x,y=y)
    plot = theme_scatter(plot)
    plot += gg.labs(title=title,x=x,y=y)
    if gradient:
        plot += gg.aes_string(color=group)
        plot += gg.scale_colour_gradientn(colours=ro.StrVector(gradient),name="")
    elif group:
        plot += gg.aes_string(color=group,shape=group)
        if color:
            color = ro.StrVector(color)
            plot += gg.scale_color_manual(values=color)
        if shape:
            shape = ro.IntVector(shape)
            plot += gg.scale_shape_manual(values=shape)
        if ellipse:
            elip = {'level':0.8,'type':'t'}
            elip.update(ellipse)
            plot += gg.stat_ellipse(level=elip['level'],type=elip['type'])
    if label:
        plot += gg.geom_text(label=data.rownames,hjust=0.5,vjust=-1,size=3,alpha=0.8)
    if save:
        gg.ggsave(save,plot)
    else:
        return plot