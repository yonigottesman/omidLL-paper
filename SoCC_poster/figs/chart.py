import matplotlib.pyplot as plt
#-----------------------------
marksize=10
my_linewidth = 5
originalOmidLabel = 'Omid'
lorraGenericLabel = 'Vanilla Fragola'
lorraFPLabel = 'FP Fragola'
# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

throughputs = [32.55, 63.97, 84.37, 108.56, 162.35, 204.09, 254.77, 272.08, 278.05,477.94]
ylim = 50
myfonsize = 25
#-----------------------------




def draw_chart(x_axis,y1,y2,y3,x_name, pdf_name):
    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    plt.plot(x_axis, y1, linestyle='-', label=originalOmidLabel, marker='^', color=tableau20[6],
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)

    plt.plot(x_axis, y2, marker='o', linestyle='-', color=tableau20[0], label=lorraGenericLabel,
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)

    plt.plot(x_axis, y3, label=lorraFPLabel, marker='s', linestyle='-', color=tableau20[2],
             linewidth=my_linewidth,
             markersize=marksize, markeredgewidth=2)

    plt.ylabel("Y Name [msec]", fontsize=myfonsize)
    plt.xlim((30, 480))
    plt.ylim(0, ylim)
    plt.grid(True)
    # plt.legend(loc=0)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xlabel(x_name, fontsize=myfonsize)
    plt.yticks(fontsize=myfonsize)
    plt.xticks(fontsize=myfonsize)
    # plt.title("Transaction Size "+ txsize[pltnum],fontsize=myfonsize)
    plt.tight_layout()

    plt.legend(loc=1, fontsize=myfonsize)
    plt.savefig(pdf_name + ".pdf", bbox_inches='tight')
    plt.show()


def main():

    x = [32.55, 63.97, 84.37, 108.56, 162.35, 204.09, 254.77, 272.08, 278.05,477.94]
    y1 = [19.66,20.55,22.00,22.69,34.03,40.00,47.53,76.17,None,None]
    y2 = [4.0, 4.0, 4.24, 4.0, 4.0, 3.82, 5.0, 5.0,5.20,10.04]
    y3 = [2.1, 2.1, 2.13, 2.1, 2.1, 2.12, 2.1, 2.1,2.45,2 ]

    draw_chart(x, y1, y2, y3, "MYXNAME","GALI!@#")


if __name__ == "__main__":
    main()
