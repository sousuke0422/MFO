import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
font = {"family": "IPAexGothic"}
plt.rc('font', **font)


def pie_chart(data: list, label: list, file_name: str):
    plt.style.use('ggplot')
    plt.rcParams.update({'font.size': 15})
    size = (9, 5)  # 凡例を配置する関係でsizeは横長にしておきます。
    col = cm.Spectral(np.arange(len(data)) / float(len(data)))
    plt.figure(figsize=size, dpi=100)
    plt.pie(data, colors=col, counterclock=False, startangle=90,
            autopct=lambda p: '{:0.1f}%'.format(p) if p >= 5 else '')
    plt.subplots_adjust(left=0, right=0.7)
    plt.legend(label, fancybox=True, loc='center left', bbox_to_anchor=(0.9, 0.5))
    plt.axis('equal')
    plt.savefig(f"{file_name}", bbox_inches='tight', pad_inches=0.05)
    return True
