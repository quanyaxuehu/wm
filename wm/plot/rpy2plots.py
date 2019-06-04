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


def theme_scatter(plot):
    plot += gg.theme_bw()
    plot += gg.theme(panel_grid_major=gg.element_line(color="white"), panel_grid_minor=gg.element_line(color="white"),
                        plot_title = gg.element_text(hjust = 0.5),legend_title=gg.element_blank(),
                        legend_background=gg.element_rect(fill="white", colour="black"),legend_position='right')
    return plot


def theme_bx(plot):
    plot += gg.theme_bw()
    plot += gg.theme(panel_grid_major=gg.element_line(color="white"),panel_grid_minor=gg.element_line(color="white"),
                    plot_title = gg.element_text(hjust = 0.5),legend_title=gg.element_blank(),
                    legend_background=gg.element_rect(fill="white", colour="black"),legend_key=gg.element_blank())
    return plot

def box_plot(data,group,y,color=None,legend=False,flip=False,save=None):
    asc = ro.r['as.character']
    plot = gg2.ggplot(data) +gg.aes_string(x=asc(group),y=y,fill=asc(group)) +gg.geom_boxplot()
    if not legend:
        plot += gg.guides(fill=False)
    plot += gg.labs(x = "", y = "", title = "")
    plot += gg.theme(axis_text_x=gg.element_blank(),axis_ticks_x = gg.element_blank())
    plot = theme_bx(plot)
    if flip:
        plot += gg.coord_flip()
    if color:
        plot +=  gg.scale_fill_manual(values=color)
    if save:
        gg.ggsave(save,plot)
    else:
        return plot

def extract_legend(plot):
    grob = gg.ggplotGrob(plot)
    for x in grob.rx2('grobs'):
        if 'guide-box' in str(x.rx2('name')):
            return x

def combined_plot(plots:list,nrow,ncol,heights,widths,save=None):
    grid = importr('gridExtra')
    if not heights:
        heights = [1/nrow for x in range(nrow)]
    if not widths:
        heights = [1/nrow for x in range(nrow)]
    plot = grid.grid_arrange(*plots,nrow=nrow,ncol=ncol,heights=heights,widths=heights)
    if save:
        gg.ggsave(plot,save)
    else:
        return plot
