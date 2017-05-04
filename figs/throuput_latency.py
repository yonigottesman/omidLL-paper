import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import datetime


marksize=10
my_linewidth = 5
originalOmidLabel = 'Omid'
lorraGenericLabel = 'Omid LL'
lorraFPLabel = 'Fragola'



myfonsize = 25


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
    plt.plot(throughputs, originalOmid, linestyle='-', label=originalOmidLabel, marker='^', color=tableau20[6],
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)
    plt.plot(throughputs, lorraGeneric, marker='o', linestyle='-', color=tableau20[0], label=lorraGenericLabel,
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)
    plt.plot(throughputs, lorraFP, label=lorraFPLabel, marker='s', linestyle='-', color=tableau20[2], linewidth=my_linewidth,
             markersize=marksize, markeredgewidth=2)


    plt.ylabel("Latency [msec]",fontsize=myfonsize)
    plt.xlim((30,270))
    plt.ylim(0,100)
    plt.grid(True)
    #plt.legend(loc=0)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xlabel("Throughput (tps * 1000)", fontsize=myfonsize)
    plt.yticks(fontsize=myfonsize)
    plt.xticks(fontsize=myfonsize)
    #plt.title("Transaction Size "+ txsize[pltnum],fontsize=myfonsize)
    plt.tight_layout()

    plt.legend(loc=2,fontsize=myfonsize)
    plt.savefig("throughputLatency"+txsize[pltnum]+".pdf", bbox_inches='tight')
    #plt.show()

breakdowns_names = ['Put','Get','tx5','tx10','rwm']
operation_names = ['Write','Read','Read/\nWrite','Read/\nWrite','Read/\nWrite']
def breakdown(originalOmid,lorraGeneric,lorraFP,pltnum):

    begin_times = [originalOmid[0],lorraGeneric[0],lorraFP[0]]
    hbase_times = [originalOmid[1], lorraGeneric[1], lorraFP[1]]
    commit_times = [originalOmid[2], lorraGeneric[2], lorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    lorraGenericLabel = 'Omid\nLL'
    lorraFPLabel = 'Fragola'

    p3 = ax.bar(range(len(commit_times)), commit_times, bottom=np.array(begin_times)+np.array(hbase_times),
                label='Commit', alpha=0.5, color='g',align='center')
    p2 = ax.bar(range(len(hbase_times)), hbase_times, bottom=begin_times, label=operation_names[pltnum], alpha=1, color='r',
                align='center', )
    p1 = ax.bar(range(len(begin_times)), begin_times, label='Begin', alpha=1, color='b', align='center')
    plt.xticks(np.arange(3) ,[originalOmidLabel,lorraGenericLabel,lorraFPLabel],fontsize=myfonsize)

    if pltnum == 0 or pltnum == 1 or pltnum == 4:
        plt.ylim(0, 35)
    else:
        plt.ylim(0, 50)
    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Latency [msec]", fontsize=myfonsize)

    plt.legend(loc=0, fontsize=myfonsize)

    plt.tight_layout()
    plt.savefig("latency_" + breakdowns_names[pltnum] + ".pdf",
                bbox_inches='tight')
    #plt.show()


def singlebreakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,ylimit,txt):

    begin_times = [GEToriginalOmid[0], GETlorraGeneric[0], GETlorraFP[0]]
    hbase_times = [GEToriginalOmid[1], GETlorraGeneric[1], GETlorraFP[1]]
    commit_times = [GEToriginalOmid[2], GETlorraGeneric[2], GETlorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    lorraGenericLabel = 'Omid\nLL'
    lorraFPLabel = 'Fragola'

    p3 = ax.bar([4,5,6],commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                label='Commit', alpha=0.5, color='g', align='center')
    p2 = ax.bar([4,5,6], hbase_times, bottom=begin_times, label=operation_names[2], alpha=1,
                color='r', align='center', )
    p1 = ax.bar([4,5,6], begin_times, label='Begin', alpha=1, color='b', align='center')

    begin_times = [PUToriginalOmid[0], PUTlorraGeneric[0], PUTlorraFP[0]]
    hbase_times = [PUToriginalOmid[1], PUTlorraGeneric[1], PUTlorraFP[1]]
    commit_times = [PUToriginalOmid[2], PUTlorraGeneric[2], PUTlorraFP[2]]

    p3 = ax.bar([0, 1, 2], commit_times, bottom=np.array(begin_times) + np.array(hbase_times), alpha=0.5, color='g', align='center')
    p2 = ax.bar([0, 1, 2], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center', )
    p1 = ax.bar([0, 1, 2], begin_times,  alpha=1, color='b', align='center')

    ax.text(4, ylimit-5, txt[0], fontsize=myfonsize)
    ax.text(0, ylimit-5, txt[1], fontsize=myfonsize)

    plt.xticks([0,1,2,4,5,6], [originalOmidLabel, lorraGenericLabel, lorraFPLabel,originalOmidLabel, lorraGenericLabel, lorraFPLabel], fontsize=myfonsize)

    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Latency [msec]", fontsize=myfonsize)

    plt.xlim(-1,7)
    plt.ylim(0,ylimit)
    lgd = plt.legend(loc=7, fontsize=myfonsize)


    plt.tight_layout()
    plt.savefig("latency_" +txt[2] + ".pdf",
                bbox_inches='tight',bbox_extra_artists=(lgd,))
    plt.show()




def summery():
    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)
    speedup = [132,	56,	81,	-12,-15,]

    ax.plot([-1,0,1,2,3,4,5],[0,0,0,0,0,0,0],linestyle='-', color='black',linewidth = 4)
    xloc = [0,1,2,3,4]
    p1 = ax.bar(xloc, speedup, alpha=1, color=tableau20[0], align='center')
    plt.xticks(xloc ,['Write','Read','Read\n+Write','Tx of\nsize 5','Tx of\nsize 10'],fontsize=myfonsize)
    plt.ylim(-50, 150)
    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Speedup", fontsize=myfonsize)
    formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
    ax.yaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.savefig("speedup.pdf",
                bbox_inches='tight')

#    plt.show()



summery()

PUToriginalOmid = [13.36,1.77,13.41]
PUTlorraGeneric = [0.44,1.96,3.03]
PUTlorraFP = [0.00,2.34,0.00]
#breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,0)

GEToriginalOmid = [13.36,1.73,0.38]
GETlorraGeneric = [0.44,1.49,0.38]
GETlorraFP = [0.00,1.48,0.00]
#breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP)

singlebreakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,40,['Single read','Single write','PUTGET'])

TX5originalOmid = [13.36,8.76,13.76]
TX5lorraGeneric = [0.44,8.60,3.08]
TX5lorraFP = [0.76,10.52,2.43]
#breakdown(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,2)

TX10originalOmid = [13.36,17.51,14.06]
TX10lorraGeneric = [0.44,17.20,3.12]
TX10lorraFP = [0.76,21.05,2.56]
#breakdown(TX10originalOmid,TX10lorraGeneric,TX10lorraFP,3)

singlebreakdown(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,TX10originalOmid,TX10lorraGeneric,TX10lorraFP,60,['TX size 5','TX size 10','5_10'])

RMWoriginalOmid = [13.36,3.50,14.06]
RMWlorraGeneric = [0.44,3.44,3.12]
RMWlorraFP = [0.00,3.86,0.00]
breakdown(RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,4)



TX1originalOmid = [19.66,20.55,22.00,22.69,34.03,40.00,47.53,76.17]
TX1lorraGeneric = [4.0, 4.0, 4.24, 4.0, 4.0, 3.82, 5.0, 5.0]
TX1lorraFP = [2.1, 2.1, 2.13, 2.1, 2.1, 2.12, 2.1, 2.1]
draw_throughput_latency(TX1originalOmid,TX1lorraGeneric,TX1lorraFP,1)



TX5originalOmid = [31.59, 33.05, 34.0, 34.47, 52.69, 65.0, 80.0, 100.87]
TX5lorraGeneric = [12.0, 12.0, 11.91, 12.0, 12.0, 11.24, 12.0, 12.0]
TX5lorraFP = [13.0, 13.0, 13.23, 13.15, 13.15, 13.15, 14.0, 14.0]
draw_throughput_latency(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,2)



TX10originalOmid =[40.25, 42.28, 44.0, 45.04, 52.7, 64.0, 77.73, 125.42]
TX10lorraGeneric = [21.0, 21.0, 20.32, 21.0, 21.0, 19.8, 21.0, 21.0]
TX10lorraFP =[24.0, 24.0, 24.22, 24.0, 23.0, 23.23, 26.0, 29.0]
draw_throughput_latency(TX10originalOmid,TX10lorraGeneric,TX10lorraFP,3)




