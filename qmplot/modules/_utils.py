"""Utils functions for plot figure
"""
import matplotlib.pyplot as plt


class General(object):
    def __init__(self):
        pass

    @staticmethod
    def get_figure(is_show, fig_name=None, dpi=300):
        if fig_name:
            plt.savefig(fig_name, bbox_inches="tight", dpi=dpi)

        if is_show:
            plt.show()

        plt.clf()
        plt.close()

        return
