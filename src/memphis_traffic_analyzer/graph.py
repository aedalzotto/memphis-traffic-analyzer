import matplotlib.pyplot as plt
from math import floor, ceil
from .dmni import DMNI
from .edges import Edges

class Graph:
    def __init__(
            self, 
            scen_path, 
            ids, 
            start_ms=None, 
            comp_path=None, 
            comp_ids=None,
            export=False
    ):
        self.figs = []
        self.axes = []

        dmni = DMNI(scen_path)
        for id in ids:
            traffic = dmni[id]
            if start_ms is not None:
                traffic = traffic.drop(traffic[traffic['snd_time']/100000.0 < start_ms].index)

            edges = Edges(traffic)
            fig, ax = plt.subplots(len(edges))
            
            min_x = floor(
                min([edges[edge]['snd_time'].min()/100000.0 for edge in edges])
            )
            max_x = ceil(
                max([edges[edge]['snd_time'].max()/100000.0 for edge in edges])
            )

            for i, edge in enumerate(edges):
                if len(edges) > 1:
                    ax_ref = ax[i]
                else:
                    ax_ref = ax

                ax_ref.plot(edges[edge]['snd_time']/100000.0, edges[edge]['latency']/100.0, "o--", label="e{},{}".format(edge[0], edge[1]))
                # ax_ref.set_xlabel("Time (ms)")
                ax_ref.set_ylabel("Latency (µs)")
                ax_ref.legend(loc="lower right")
                ax_ref.set_xlim([min_x, max_x])

                if export:
                    print("Edge {}".format(edge))
                    [print("({}, {})".format(row['snd_time']/100000.0, row['latency']/100.0)) for index, row in edges[edge].iterrows()]
                    print("")

            self.figs.append(fig)
            self.axes.append(ax)

        if comp_path is not None:
            dmni_comp = DMNI(comp_path)
            for idx, comp_id in enumerate(comp_ids):
                traffic = dmni_comp[comp_id]
                if start_ms is not None:
                    traffic = traffic.drop(traffic[traffic['snd_time']/100000.0 < start_ms].index)
                edges = Edges(traffic)

                for i, edge in enumerate(edges):
                    if len(edges) > 1:
                        self.axes[idx][i].plot(edges[edge]['snd_time']/100000.0, edges[edge]['snd_time']/100.0, "o--")
                    else:
                        self.axes[idx].plot(edges[edge][0]/100000.0, edges[edge]['snd_time']/100.0, "o--")

    def show(self):
        for fig in self.figs:
            fig.show()
        
        plt.xlabel("Time (ms)")
        plt.show()
        
    def save(self, path):
        plt.savefig(path, bbox_inches='tight')
