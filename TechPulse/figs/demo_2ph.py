import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import FuncFormatter
import datetime


marksize=10
my_linewidth = 5
originalOmidLabel = '2 PC'
lorraGenericLabel = 'Vanilla Fragola'
lorraFPLabel = 'FP Fragola'
lorra2PhLabel = 'Vanilla Fragola 2PC'


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


throughputs = [107.69	,227.02,	338.68,	461.72]
txsize = ['0','1','5','10']
def draw_throughput_latency(originalOmid,lorraGeneric,lorraFP,pltnum,ylim=50):
    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)
    plt.plot(throughputs, originalOmid, linestyle='-', label=originalOmidLabel, marker='^', color=tableau20[6],
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)
    plt.plot(throughputs, lorraGeneric, marker='o', linestyle='-', color=tableau20[0], label=lorraGenericLabel,
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)
    # plt.plot(throughputs, lorra2ph, marker='*', linestyle='-', color=tableau20[4], label=lorra2PhLabel,
    #          linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)
    plt.plot(throughputs, lorraFP, label=lorraFPLabel, marker='s', linestyle='-', color=tableau20[2], linewidth=my_linewidth,
             markersize=marksize, markeredgewidth=2)

    plt.ylabel("Latency [msec]",fontsize=myfonsize)
    plt.xlim((100,480))
    plt.ylim(0,ylim)
    plt.grid(True)
    #plt.legend(loc=0)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xlabel("Throughput (tps * 1000)", fontsize=myfonsize)
    plt.yticks(fontsize=myfonsize)
    plt.xticks(fontsize=myfonsize)
    plt.title("Transaction Size "+ txsize[pltnum],fontsize=myfonsize)
    plt.tight_layout()

    plt.legend(loc=2,fontsize=myfonsize)
    #plt.show()


breakdowns_names = ['Put','Get','tx5','tx10','rwm']
operation_names = ['Write','Read','Read/\nWrite','Read/\nWrite','Read/\nWrite']

def new_breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,s,txt):

    commit_hatch = ""
    hbase_hatch = ""
    begin_hatch = ""

    omid_color='g'
    generic_colot='r'
    fp_color='b'

    begin_times = [GEToriginalOmid[0], GETlorraGeneric[0], GETlorraFP[0]]
    hbase_times = [GEToriginalOmid[1], GETlorraGeneric[1], GETlorraFP[1]]
    commit_times = [GEToriginalOmid[2], GETlorraGeneric[2], GETlorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    lorraGenericLabel = 'Vanilla\nFragola'
    lorraFPLabel = 'FP\nFragola'

    p3 = ax.bar([4,5,6],commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                label='Commit', alpha=0.5, color='g', align='center',hatch=commit_hatch)

    p2 = ax.bar([4,5,6], hbase_times, bottom=begin_times, label=operation_names[2], alpha=1,
                color='r', align='center', hatch=hbase_hatch)
    p1 = ax.bar([4,5,6], begin_times, label='Begin', alpha=1, color='b', align='center',hatch=begin_hatch)

    begin_times = [PUToriginalOmid[0], PUTlorraGeneric[0], PUTlorraFP[0]]
    hbase_times = [PUToriginalOmid[1], PUTlorraGeneric[1], PUTlorraFP[1]]
    commit_times = [PUToriginalOmid[2], PUTlorraGeneric[2], PUTlorraFP[2]]

    p3 = ax.bar([0, 1, 2], commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                alpha=0.5, color='g', align='center',hatch=commit_hatch)
    p2 = ax.bar([0, 1, 2], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center',hatch=hbase_hatch )
    p1 = ax.bar([0, 1, 2], begin_times,  alpha=1, color='b', align='center',hatch=begin_hatch)

    begin_times = [RMWoriginalOmid[0], RMWlorraGeneric[0], RMWlorraFP[0]]
    hbase_times = [RMWoriginalOmid[1], RMWlorraGeneric[1], RMWlorraFP[1]]
    commit_times = [RMWoriginalOmid[2], RMWlorraGeneric[2], RMWlorraFP[2]]

    p3 = ax.bar([8, 9, 10], commit_times, bottom=np.array(begin_times) + np.array(hbase_times), alpha=0.5, color='g', align='center',hatch=commit_hatch)
    p2 = ax.bar([8, 9, 10], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center',hatch=hbase_hatch )
    p1 = ax.bar([8, 9, 10], begin_times,  alpha=1, color='b', align='center',hatch=begin_hatch)



    # ax.text(4, ylimit-5, txt[0], fontsize=myfonsize)
    # ax.text(0, ylimit-5, txt[1], fontsize=myfonsize)

    plt.xticks([0,1,2,4,5,6,8,9,10], [originalOmidLabel, lorraGenericLabel, lorraFPLabel,originalOmidLabel, lorraGenericLabel, lorraFPLabel,originalOmidLabel, lorraGenericLabel, lorraFPLabel], fontsize=myfonsize-9)


    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    plt.annotate('Write', (0, 0), (60, -70), xycoords='axes fraction', textcoords='offset points', va='top',
                 fontsize=myfonsize)

    plt.annotate('Read', (0, 0), (260, -70), xycoords='axes fraction', textcoords='offset points', va='top',
                 fontsize=myfonsize)

    plt.annotate('BRWC', (0, 0), (460, -70), xycoords='axes fraction', textcoords='offset points', va='top',
                 fontsize=myfonsize)



    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Latency [msec]", fontsize=myfonsize)

    plt.xlim(-1,12)
    plt.ylim(0,15)
    #lgd = plt.legend(loc=7, fontsize=myfonsize)
    lgd = plt.legend( prop={'size':20},ncol=3,loc=9, fontsize=myfonsize)
    plt.title(s, fontsize=myfonsize)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2,top=0.9)

    #plt.show()

def singlebreakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,ylimit,txt):

    begin_times = [GEToriginalOmid[0], GETlorraGeneric[0], GETlorraFP[0]]
    hbase_times = [GEToriginalOmid[1], GETlorraGeneric[1], GETlorraFP[1]]
    commit_times = [GEToriginalOmid[2], GETlorraGeneric[2], GETlorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    lorraGenericLabel = 'Vanilla\nFragola'
    lorraFPLabel = 'FP\nFragola'

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
    lgd = plt.legend(loc=1, fontsize=myfonsize)
    #lgd = plt.legend(prop={'size': 20}, ncol=3, loc=9, fontsize=myfonsize)
    plt.title("Transaction Size 10", fontsize=myfonsize)
    plt.tight_layout()
    #plt.savefig("latency_" +txt[2] + ".pdf", bbox_inches='tight',bbox_extra_artists=(lgd,))
    #plt.show()



#----------------------------------------------------------------------------

TX12phOmid = [4.51,	4.02	,4.22	,4.55]
TX1lorraGeneric = [4.06,	3.53	,4.47	,9.57]
TX1lorraFP = [2.38	,2.09,	1.99	,2.77]

draw_throughput_latency(TX12phOmid, TX1lorraGeneric, TX1lorraFP, 1,10)

TX12phOmid = [25.10	,23.07,	23.70,	31.21]
TX1lorraGeneric = [21.09,	20.83	,22.45,	25.79]
TX1lorraFP = [24.51	,23.28,	23.93,	30.13]

draw_throughput_latency(TX12phOmid, TX1lorraGeneric, TX1lorraFP, 3,40)

#----------------------------------------------------------------------------

PUToriginalOmid = [0.55,0.03,5.56]
PUTlorraGeneric = [0.48,1.96,3.11]
PUTlorraFP = [0,2.63,0]
#breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,0)

GEToriginalOmid = [0.55,1.66,0.47]
GETlorraGeneric = [0.48,1.53,0.42]
GETlorraFP = [0,1.45,0]
#breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP)

RMWoriginalOmid = [0.55,1.67,4.53]
RMWlorraGeneric = [0.48,3.48,2.46]
RMWlorraFP = [0,4.4,0]

new_breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,"Low Throughput",['Single read','Single write','PUTGET'])

#----------------------------------------------------------------------------

PUToriginalOmid = [0.39	,0.01,	5.94]
PUTlorraGeneric = [3.24,1.75,5.94]
PUTlorraFP = [0.00	,2.79,	0.00]
#breakdown(PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,0)

GEToriginalOmid = [0.39	,1.53	,0.32]
GETlorraGeneric = [3.24	,1.45	,3.15]
GETlorraFP = [0.00,	1.78	,0.00]
#breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP)

RMWoriginalOmid = [0.39,	1.55,	4.87]
RMWlorraGeneric = [3.24	,3.21,	5.31]
RMWlorraFP = [0.00	,3.30	,0.00]

new_breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,"High Throughput",['Single read','Single write','PUTGET'])
#----------------------------------------------------------------------------

TX5originalOmid = [0.55	,8.37	,16.83]
TX5lorraGeneric = [0.48	,17.38,	3.15]
TX5lorraFP = [0.60	,22.40,	2.88]
#breakdown(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,2)

TX10originalOmid = [0.39,	7.72	,21.89]
TX10lorraGeneric =  [3.24,	16.01	,6.07]
TX10lorraFP = [3.43	,25.28	,5.46]
#breakdown(TX10originalOmid,TX10lorraGeneric,TX10lorraFP,3)

singlebreakdown(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,TX10originalOmid,TX10lorraGeneric,TX10lorraFP,60,['Low','High','5_10'])





plt.show()