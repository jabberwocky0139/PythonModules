# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

class PlotWrapper:
    # x_coor : iterable
    # y_coor : iterable or func
    # x_range, y_range : 2 element array-like object
    # x_label, y_label, title, line_color : string
    # line_width : integer
    def plot_wrapper(self, x_coor, y_coor,  x_range=None, y_range=None, x_label=None, y_label=None, title=None, line_color="blue", line_width=1):
        # plot
        if callable(y_coor):
            plt.plot(x_coor, [y_coor(y) for y in x_coor], color=line_color, linewidth=line_width)
        else:
            plt.plot(x_coor, y_coor, color=line_color, linewidth=line_width)
        if x_range is not None:
	    # set xrange
            plt.xlim(x_range[0], x_range[1])
        if y_range is not None:
            # set yrange
            plt.ylim(y_range[0], y_range[1])
        if x_label is not None:
            # set xlabel
            plt.xlabel(x_label)
        if y_label is not None:
            # set ylabel
            plt.ylabel(y_label)
        if title is not None:
            # set title
            plt.title(title)
        # おまじない
        plt.legend()
        # show plot data
        plt.show()

