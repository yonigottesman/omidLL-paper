import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import FuncFormatter
import datetime


marksize=10
my_linewidth = 5
originalOmidLabel = 'Omid'
lorraGenericLabel = 'Omid LL'
lorraFPLabel = 'Omid FP'
lorra2PhLabel = 'Omid 2PC'


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


throughputs = [31.62	,63.08	,97.04	,129.67,	158.14	,229.04	,229.65,	377.96	,561.57]
txsize = ['0','1','5','10']
def draw_throughput_latency(originalOmid,lorraGeneric,lorraFP,lorra2phase,pltnum,ylim=50):

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    plt.plot(throughputs, originalOmid, linestyle='-', label=originalOmidLabel, marker='^', color=tableau20[6],
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)

    plt.plot(throughputs, lorraGeneric, marker='o', linestyle='-', color=tableau20[0], label=lorraGenericLabel,
             linewidth=my_linewidth, markersize=marksize, markeredgewidth=2)

    plt.plot(throughputs, lorra2phase, label=lorra2PhLabel, marker='x', linestyle='-', color=tableau20[4],
             linewidth=my_linewidth-1, markersize=marksize, markeredgewidth=1)

    plt.plot(throughputs, lorraFP, label=lorraFPLabel, marker='s', linestyle='-', color=tableau20[2], linewidth=my_linewidth,
             markersize=marksize, markeredgewidth=2)




    plt.ylabel("Latency [msec]",fontsize=myfonsize)
    plt.xlim((30,550))
    plt.ylim(0,ylim)
    plt.grid(True)
    #plt.legend(loc=0)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xlabel("Throughput (tps * 1000)", fontsize=myfonsize)
    plt.yticks(fontsize=myfonsize)
    plt.xticks(fontsize=myfonsize)
    #plt.title("Transaction Size "+ txsize[pltnum],fontsize=myfonsize)
    plt.tight_layout()

    plt.legend(loc=1,fontsize=myfonsize)
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

    # lorraGenericLabel = 'Omid LL'
    # lorraFPLabel = 'Fragola'

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

def breakdownHighTX(originalOmid,lorraGeneric,lorraFP,pltnum):

    begin_times = [originalOmid[0],lorraGeneric[0],lorraFP[0]]
    hbase_times = [originalOmid[1], lorraGeneric[1], lorraFP[1]]
    commit_times = [originalOmid[2], lorraGeneric[2], lorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    # lorraGenericLabel = 'Omid LL'
    # lorraFPLabel = 'Fragola'

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



def singlebreakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,two_phase5,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,two_phase10,ylimit,txt):

    begin_times = [GEToriginalOmid[0], GETlorraGeneric[0],two_phase5[0], GETlorraFP[0]]
    hbase_times = [GEToriginalOmid[1], GETlorraGeneric[1],two_phase5[1], GETlorraFP[1]]
    commit_times = [GEToriginalOmid[2], GETlorraGeneric[2],two_phase5[2], GETlorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    # lorraGenericLabel = 'Omid LL'
    # lorraFPLabel = 'Fragola'
    # lorra2PhLabel = 'Omid 2PC'

    p3 = ax.bar([5,6,7,8],commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                label='Commit', alpha=0.5, color='g', align='center')
    p2 = ax.bar([5,6,7,8], hbase_times, bottom=begin_times, label=operation_names[2], alpha=1,
                color='r', align='center', )
    p1 = ax.bar([5,6,7,8], begin_times, label='Begin', alpha=1, color='b', align='center')

    begin_times = [PUToriginalOmid[0], PUTlorraGeneric[0],two_phase10[0], PUTlorraFP[0]]
    hbase_times = [PUToriginalOmid[1], PUTlorraGeneric[1],two_phase10[1], PUTlorraFP[1]]
    commit_times = [PUToriginalOmid[2], PUTlorraGeneric[2],two_phase10[2], PUTlorraFP[2]]

    p3 = ax.bar([0, 1, 2,3], commit_times, bottom=np.array(begin_times) + np.array(hbase_times), alpha=0.5, color='g', align='center')
    p2 = ax.bar([0, 1, 2,3], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center', )
    p1 = ax.bar([0, 1, 2,3], begin_times,  alpha=1, color='b', align='center')

    ax.text(4, ylimit-5, txt[0], fontsize=myfonsize)
    ax.text(0, ylimit-5, txt[1], fontsize=myfonsize)

    plt.xticks([0,1,2,3,5,6,7,8], [originalOmidLabel, lorraGenericLabel,lorra2PhLabel, lorraFPLabel,originalOmidLabel, lorraGenericLabel,lorra2PhLabel, lorraFPLabel], fontsize=myfonsize)

    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Latency [msec]", fontsize=myfonsize)

    plt.xlim(-1,9)
    plt.ylim(0,ylimit)
    lgd = plt.legend(loc=7, fontsize=myfonsize)


    plt.tight_layout()
    plt.savefig("latency_" +txt[2] + ".pdf",
                bbox_inches='tight',bbox_extra_artists=(lgd,))
    #plt.show()



def new_breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,GET2phase,PUT2phase,RMW2phase,s,txt):

    commit_hatch = ""
    hbase_hatch = ""
    begin_hatch = ""

    omid_color='g'
    generic_colot='r'
    fp_color='b'

    begin_times = [GEToriginalOmid[0], GETlorraGeneric[0],GET2phase[0], GETlorraFP[0]]
    hbase_times = [GEToriginalOmid[1], GETlorraGeneric[1],GET2phase[1], GETlorraFP[1]]
    commit_times = [GEToriginalOmid[2], GETlorraGeneric[2],GET2phase[2], GETlorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)

    # lorraGenericLabel = 'Vanilla\nFragola'
    # lorraFPLabel = 'FP\nFragola'

    # lorraGenericLabel = 'Omid LL'
    # lorraFPLabel = 'Fragola'
    # lorra2PhLabel = 'Omid 2PC'

    p3 = ax.bar([5,6,7,8],commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                label='Commit', alpha=0.5, color='g', align='center',hatch=commit_hatch)

    p2 = ax.bar([5,6,7,8], hbase_times, bottom=begin_times, label=operation_names[2], alpha=1,
                color='r', align='center', hatch=hbase_hatch)
    p1 = ax.bar([5,6,7,8], begin_times, label='Begin', alpha=1, color='b', align='center',hatch=begin_hatch)

    begin_times = [PUToriginalOmid[0], PUTlorraGeneric[0],PUT2phase[0], PUTlorraFP[0]]
    hbase_times = [PUToriginalOmid[1], PUTlorraGeneric[1],PUT2phase[1], PUTlorraFP[1]]
    commit_times = [PUToriginalOmid[2], PUTlorraGeneric[2],PUT2phase[2], PUTlorraFP[2]]

    p3 = ax.bar([0, 1, 2,3], commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                alpha=0.5, color='g', align='center',hatch=commit_hatch)
    p2 = ax.bar([0, 1, 2,3], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center',hatch=hbase_hatch )
    p1 = ax.bar([0, 1, 2,3], begin_times,  alpha=1, color='b', align='center',hatch=begin_hatch)

    begin_times = [RMWoriginalOmid[0], RMWlorraGeneric[0],RMW2phase[0], RMWlorraFP[0]]
    hbase_times = [RMWoriginalOmid[1], RMWlorraGeneric[1],RMW2phase[1], RMWlorraFP[1]]
    commit_times = [RMWoriginalOmid[2], RMWlorraGeneric[2],RMW2phase[2], RMWlorraFP[2]]

    p3 = ax.bar([10,11,12,13], commit_times, bottom=np.array(begin_times) + np.array(hbase_times), alpha=0.5, color='g', align='center',hatch=commit_hatch)
    p2 = ax.bar([10,11,12,13], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center',hatch=hbase_hatch )
    p1 = ax.bar([10,11,12,13], begin_times,  alpha=1, color='b', align='center',hatch=begin_hatch)



    # ax.text(4, ylimit-5, txt[0], fontsize=myfonsize)
    # ax.text(0, ylimit-5, txt[1], fontsize=myfonsize)

    plt.xticks([0,1,2,3,5,6,7,8,10,11,12,13], [originalOmidLabel, lorraGenericLabel,lorra2PhLabel, lorraFPLabel,originalOmidLabel, lorraGenericLabel,lorra2PhLabel, lorraFPLabel,originalOmidLabel, lorraGenericLabel,lorra2PhLabel, lorraFPLabel], fontsize=myfonsize-9)


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

    plt.xlim(-1,14)
    plt.ylim(0,40)
#    lgd = plt.legend(loc=1, fontsize=myfonsize)


    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2,top=0.9)

    plt.savefig("latency_all" +txt[2] + ".pdf",
                bbox_inches='')
    #plt.show()





def singlebreakdownHigh(GETlorraGeneric,GETlorraFP,GET2phase,PUTlorraGeneric,PUTlorraFP,PUT2phase,RMWlorraGeneric,RMWlorraFP,RMW2phase,ylimit,txt):

    begin_times = [GETlorraGeneric[0],GET2phase[0], GETlorraFP[0]]
    hbase_times = [GETlorraGeneric[1],GET2phase[1], GETlorraFP[1]]
    commit_times = [GETlorraGeneric[2],GET2phase[2], GETlorraFP[2]]

    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)


    # lorraGenericLabel = 'Vanilla\nFragola'
    # lorraFPLabel = 'FP\nFragola'

    # lorraGenericLabel = 'Omid LL'
    # lorraFPLabel = 'Fragola'
    # lorra2PhLabel = 'Omid 2PC'

    p3 = ax.bar([4,5,6],commit_times, bottom=np.array(begin_times) + np.array(hbase_times),
                label='Commit', alpha=0.5, color='g', align='center')
    p2 = ax.bar([4,5,6], hbase_times, bottom=begin_times, label=operation_names[2], alpha=1,
                color='r', align='center', )
    p1 = ax.bar([4,5,6], begin_times, label='Begin', alpha=1, color='b', align='center')

    begin_times = [PUTlorraGeneric[0],PUT2phase[0], PUTlorraFP[0]]
    hbase_times = [PUTlorraGeneric[1],PUT2phase[1], PUTlorraFP[1]]
    commit_times = [PUTlorraGeneric[2],PUT2phase[2], PUTlorraFP[2]]

    p3 = ax.bar([0, 1,2], commit_times, bottom=np.array(begin_times) + np.array(hbase_times), alpha=0.5, color='g', align='center')
    p2 = ax.bar([0, 1,2], hbase_times, bottom=begin_times,  alpha=1, color='r', align='center', )
    p1 = ax.bar([0, 1,2], begin_times,  alpha=1, color='b', align='center')

    begin_times = [RMWlorraGenericHigh[0],RMW2phase[0], RMWlorraFPHigh[0]]
    hbase_times = [RMWlorraGenericHigh[1],RMW2phase[1], RMWlorraFPHigh[1]]
    commit_times = [RMWlorraGenericHigh[2],RMW2phase[2], RMWlorraFPHigh[2]]

    p3 = ax.bar([8,9,10], commit_times, bottom=np.array(begin_times) + np.array(hbase_times), alpha=0.5, color='g',
                align='center')
    p2 = ax.bar([8,9,10], hbase_times, bottom=begin_times, alpha=1, color='r', align='center', )
    p1 = ax.bar([8,9,10], begin_times, alpha=1, color='b', align='center')

    plt.xticks([0,1,2,4,5,6,8,9,10], [lorraGenericLabel,  lorra2PhLabel,lorraFPLabel,lorraGenericLabel, lorra2PhLabel,lorraFPLabel,lorraGenericLabel, lorra2PhLabel,lorraFPLabel], fontsize=myfonsize-9)

    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Latency [msec]", fontsize=myfonsize)

    plt.xlim(-1,11)
    plt.ylim(0,ylimit)
    lgd = plt.legend( prop={'size':20},ncol=3,loc=9, fontsize=myfonsize)

    plt.annotate('Write', (0, 0), (60, -70), xycoords='axes fraction', textcoords='offset points', va='top',
                 fontsize=myfonsize)

    plt.annotate('Read', (0, 0), (260, -70), xycoords='axes fraction', textcoords='offset points', va='top',
                 fontsize=myfonsize)

    plt.annotate('BRWC', (0, 0), (460, -70), xycoords='axes fraction', textcoords='offset points', va='top',
                 fontsize=myfonsize)


    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2, top=0.9)

    plt.savefig("latencyHighThrough_" +txt[3] + ".pdf")





def high_summery():
    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)
    speedup = [170,	121,	150,	-20,-25,]

    ax.plot([-1,0,1,2,3,4,5],[0,0,0,0,0,0,0],linestyle='-', color='black',linewidth = 4)
    xloc = [0,1,2,3,4]
    p1 = ax.bar(xloc, speedup, alpha=1, color=tableau20[0], align='center')
    plt.xticks(xloc ,['Write','Read','BRWC','Tx of\nsize 5','Tx of\nsize 10'],fontsize=myfonsize)
    plt.ylim(-50, 180)
    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Speedup", fontsize=myfonsize)
    formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
    ax.yaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.savefig("high_speedup.pdf",
                bbox_inches='tight')

    #plt.show()


def low_summery():
    plt.figure(figsize=(10, 7))
    ax = plt.subplot(1, 1, 1)
    speedup = [133,	68,	63,	-8,-13,]

    ax.plot([-1,0,1,2,3,4,5],[0,0,0,0,0,0,0],linestyle='-', color='black',linewidth = 4)
    xloc = [0,1,2,3,4]
    p1 = ax.bar(xloc, speedup, alpha=1, color=tableau20[0], align='center')
    plt.xticks(xloc ,['Write','Read','BRWC','Tx of\nsize 5','Tx of\nsize 10'],fontsize=myfonsize)
    plt.ylim(-50, 150)
    plt.grid(True)
    plt.yticks(fontsize=myfonsize)

    plt.ylabel("Speedup", fontsize=myfonsize)
    formatter = FuncFormatter(lambda y, pos: "%d%%" % (y))
    ax.yaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.savefig("low_speedup.pdf",
                bbox_inches='tight')







high_summery()
low_summery()

PUToriginalOmid = [18.60,1.89,16.50]
PUTlorraGeneric = [0.48,2.00,3.17]
PUTlorraFP = [0.00,2.43,0.00]
PUT2phase = [0.60,0.03,5.29]

GEToriginalOmid = [18.60,1.47,0.39]
GETlorraGeneric = [0.48,1.59,0.39]
GETlorraFP = [0.00,1.46,0.00]
GET2phase = [0.60,1.60,0.46]

RMWoriginalOmid = [18.60,3.36,15.61]
RMWlorraGeneric = [0.48,3.57,2.43]
RMWlorraFP = [0.00,3.97,0.00]
RMW2phase = [0.60,1.62,4.85]


new_breakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,GET2phase,PUT2phase,RMW2phase,40,['Single read','Single write','PUTGET'])



#breakdown(RMWoriginalOmid,RMWlorraGeneric,RMWlorraFP,4)


#singlebreakdown(GEToriginalOmid,GETlorraGeneric,GETlorraFP,PUToriginalOmid,PUTlorraGeneric,PUTlorraFP,40,['Single read','Single write','PUTGET'])

TX5originalOmid = [18.60,8.40,18.64]
TX5lorraGeneric = [0.48,8.92,3.24]
TX5lorraFP = [0.48,10.81,2.51]
TX52phase = [0.60,4.05,10.43]

TX10originalOmid = [18.60,16.80,17.33]
TX10lorraGeneric = [0.48,17.85,3.32]
TX10lorraFP = [0.48,21.62,2.65]
TX102phase = [0.60,8.09,16.87]


singlebreakdown(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,TX52phase,TX10originalOmid,TX10lorraGeneric,TX10lorraFP,TX102phase,60,['TX size 5','TX size 10','5_10'])





TX1originalOmid = [21.91	,23.32,	28.57,	30.00,	34.57	,50.00	,70.05,None,None]
TX1lorraGeneric = [4.00	,4.00	,4.00	,4.47	,4.00,	3.86,	3.90	,3.91	,5.48]
TX1lorraFP = [ 2.00,	2.00,	2.00,	2.26,	2.06,	2.06	,2.21	,2.21	,2.50]
TX12phase = [4.00	,4.00,	4.00	,4.29,	4.00,	3.96	,4.0,	4.77	,4.70]
draw_throughput_latency(TX1originalOmid,TX1lorraGeneric,TX1lorraFP,TX12phase,1)



TX5originalOmid = [33.52,	38.56	,43.39	,50.00,	52.93,	100.00,	111.64,None,None]
TX5lorraGeneric = [12.00,	12.00	,12.00	,12.26,	12.00,	11.80,	11.80	,11.14,	13.64]
TX5lorraFP = [13.00	,13.00	,13.00,	13.66,	13.79,	13.79	,14.00,	14.23,	16.52]
TX52phase = [15.00,	15.00	,15.00,	15.41	,15.00	,13.46	,14.00	,13.69,14.77]
draw_throughput_latency(TX5originalOmid,TX5lorraGeneric,TX5lorraFP,TX52phase,2)


TX10originalOmid =[44.08	,48.24,	48.28,	55.00,	62.73	,80.00	,101.00,None,None]
TX10lorraGeneric = [19.00	,19.00	,19.00	,23.66,	20.00	,19.89	,19.00,	18.51	,20.81]
TX10lorraFP =[24.00	,24.00,	24.00,	24.36,	24.00	,23.24,	25.00	,25.44,	27.99]
TX102phase = [25.00	,25.00,	25.00,	25.51	,25.00,	24.30	,25.50,	25.50,	27.94]
draw_throughput_latency(TX10originalOmid,TX10lorraGeneric,TX10lorraFP,TX102phase,3,100)


#High Throughput


PUTlorraGenericHigh = [1.11,1.78,4.02]
PUTlorraFPHigh = [0.00,2.56,0.00]
PUT2phaseFPHigh = [0.52,0.01,6.08]


GETlorraGenericHigh = [1.11,1.51,1.04]
GETlorraFPHigh = [0.00,1.65,0.00]
GET2phaseFPHigh = [0.52,1.63,0.46]

RMWlorraGenericHigh = [1.11,3.29,3.21]
RMWlorraFPHigh = [0.00,3.04,0.00]
RMW2phaseFPHigh = [0.52,1.65,5.04]

singlebreakdownHigh(GETlorraGenericHigh,GETlorraFPHigh,GET2phaseFPHigh, PUTlorraGenericHigh,PUTlorraFPHigh,PUT2phaseFPHigh,RMWlorraGenericHigh,RMWlorraFPHigh,RMW2phaseFPHigh,15,['Single read','Single write','BRWC','PUTGETRMW'])


plt.show()
sys.exit()

