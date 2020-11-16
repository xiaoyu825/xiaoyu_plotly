import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import sys
import re


def parse_plain_log(log_file, flag):

    score = []
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # a = r'\* Acc@1'
            # a = r'\[10000\/'
            a = r'acc@1'

            if re.findall(a, line):
                print(line.split())
                if flag == 'VA':  # val acc
                    score.append(float(line.split()[-3]))
                elif flag == 'TA':  # train acc
                    score.append(float(line.split()[-5][:-1]))
                elif flag == 'TL':  # train loss
                    score.append(float(line.split()[-9][1:-1]))
                elif flag == 'VL':  # val loss
                    score.append(float(line.split()[8]))

    x_score = np.arange(len(score))
    return [x_score, score]


def plot_logs(logs, keys):
    assert len(logs) == len(keys)
    valid_acc_traces = []
    loss_traces = []
    for log, key in zip(logs, keys):
        valid_acc_log = log
        print('{}'.format(key))
        valid_acc_traces.append(go.Scatter(x=valid_acc_log[0],
                                           y=valid_acc_log[1],
                                           mode='lines',
                                           name='{}'.format(key)))
    return valid_acc_traces


if __name__ == '__main__':
    chart_studio.tools.set_credentials_file(username='xiaoyu825', api_key='fAK5zFzk0DOt9xsDG6hD')

    desc_file = sys.argv[1]
    logs = []
    keys = []
    with open(desc_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            # print(line)
            _, log_dir, log_name, log_key, flag, *_ = line.strip().split()
            if 'VA' in flag:
                log = parse_plain_log(f'./logs/{log_name}', 'VA')
                logs.append(log)
                keys.append(log_key+'_'+'VA')
            if 'TA' in flag:
                log = parse_plain_log(f'./logs/{log_name}', 'TA')
                logs.append(log)
                keys.append(log_key+'_' + 'TA')
            if 'VL' in flag:
                log = parse_plain_log(f'./logs/{log_name}', 'VL')
                logs.append(log)
                keys.append(log_key+'_' + 'VL')
            if 'TL' in flag:
                log = parse_plain_log(f'./logs/{log_name}', 'TL')
                logs.append(log)
                keys.append(log_key+'_' + 'TL')

    valid_acc_traces = plot_logs(logs, keys)
    py.plot(valid_acc_traces, filename=sys.argv[1]+'_'+flag)

