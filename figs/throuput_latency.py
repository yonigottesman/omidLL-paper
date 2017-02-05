import numpy as np
import matplotlib.pyplot as plt

marksize=5
my_linewidth = 3
originalOmidLabel = 'Omid'
lorraGenericLabel = 'Lorra (generic)'
lorraFPLabel = 'Lorra (fast-path)'
myfonsize = 30


# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

throughputs = [32.55, 63.97, 84.37, 108.56, 162.35, 204.09, 254.77, 272.08]

txsize = ['0','1','5','10']

def draw_throughput_latency(originalOmid,lorraGeneric,lorraFP,pltnum):
    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)
    plt.plot(throughputs, originalOmid, linestyle='-', label=originalOmidLabel, marker='x', color=tableau20[6],
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=1)
    plt.plot(throughputs, lorraGeneric, marker='o', linestyle='-', color=tableau20[0], label=lorraGenericLabel,
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=1)
    plt.plot(throughputs, lorraFP, label=lorraFPLabel, marker='s', linestyle='-', color=tableau20[2], linewidth=my_linewidth,
             markersize=marksize, markeredgewidth=1)


    plt.ylabel("Latency [usec]",fontsize=myfonsize)
    plt.xlim((30,270))
    plt.ylim(0,100)
    plt.grid(True)
    #plt.legend(loc=0)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xlabel("Throughput (tps * 1000)", fontsize=myfonsize)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    #plt.title("Transaction Size "+ txsize[pltnum],fontsize=myfonsize)
    plt.tight_layout()
    plt.legend(loc=2,fontsize=20)
    plt.savefig("/Users/yonatang/omid_project/omidLL-paper/figs/throughputLatency"+txsize[pltnum]+".pdf", bbox_inches='tight')
    plt.show()

breakdowns_names = ['Put','Get','tx5','tx10','rwm']
def breakdown(originalOmid,lorraGeneric,lorraFP,pltnum):

    begin_times = [originalOmid[0],lorraGeneric[0],lorraFP[0]]
    hbase_times = [originalOmid[1], lorraGeneric[1], lorraFP[1]]
    commit_times = [originalOmid[2], lorraGeneric[2], lorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    p1 = ax.bar(range(len(begin_times)), begin_times, label='Begin', alpha=0.5, color='b',align='center')
    p2 = ax.bar(range(len(hbase_times)), hbase_times, bottom=begin_times, label='Hbase', alpha=0.5, color='r',align='center')
    p3 = ax.bar(range(len(commit_times)), commit_times, bottom=np.array(begin_times)+np.array(hbase_times), label='Commit', alpha=0.5, color='g',align='center')
    plt.xticks(np.arange(3) ,[originalOmidLabel,lorraGenericLabel,lorraFPLabel],fontsize=30)

    plt.ylim(0, 50)
    plt.grid(True)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.legend(loc=0, fontsize=20)
    plt.savefig("/Users/yonatang/omid_project/omidLL-paper/figs/latency_" + breakdowns_names[pltnum] + ".pdf",
                bbox_inches='tight')
    #plt.show()


PUToriginalOmid = [13.36,1.77,13.41]
PUTlorraGeneric = [0.44,1.96,3.03]
PUTlorraFP = [0.00,2.34,0.00]
breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,0)

PUToriginalOmid = [13.36,1.77,13.41]
PUTlorraGeneric = [0.44,1.96,3.03]
PUTlorraFP = [0.00,2.34,0.00]
breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,1)

PUToriginalOmid = [13.36,1.77,13.41]
PUTlorraGeneric = [0.44,1.96,3.03]
PUTlorraFP = [0.00,2.34,0.00]
breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,2)

PUToriginalOmid = [13.36,1.77,13.41]
PUTlorraGeneric = [0.44,1.96,3.03]
PUTlorraFP = [0.00,2.34,0.00]
breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,3)

PUToriginalOmid = [13.36,1.77,13.41]
PUTlorraGeneric = [0.44,1.96,3.03]
PUTlorraFP = [0.00,2.34,0.00]
breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,4)


#
# TX1originalOmid = [19.66	,20.55	,22.00	,22.69	,34.03	,40.00	,47.53	,76.17]
# TX1lorraGeneric = [4.0, 4.0, 4.24, 4.0, 4.0, 3.82, 5.0, 5.0]
# TX1lorraFP = [2.1, 2.1, 2.13, 2.1, 2.1, 2.12, 2.1, 2.1]
# draw_throughput_latency(TX1originalOmid,TX1lorraGeneric,TX1lorraFP,1)
#
#
#
# TX5originalOmid = [31.59, 33.05, 34.0, 34.47, 52.69, 65.0, 80.0, 100.87]
# TX5lorraGeneric = [12.0, 12.0, 11.91, 12.0, 12.0, 11.24, 12.0, 12.0]
# TX5lorraFP = [13.0, 13.0, 13.23, 13.15, 13.15, 13.15, 14.0, 14.0]
# draw_throughput_latency(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,2)
#
#
#
# TX10originalOmid =[40.25, 42.28, 44.0, 45.04, 52.7, 64.0, 77.73, 125.42]
# TX10lorraGeneric = [21.0, 21.0, 20.32, 21.0, 21.0, 19.8, 21.0, 21.0]
# TX10lorraFP =[24.0, 24.0, 24.22, 24.0, 23.0, 23.23, 26.0, 29.0]
# draw_throughput_latency(TX10originalOmid,TX10lorraGeneric,TX10lorraFP,3)




