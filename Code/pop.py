import numpy as np
import pandas as pd
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="calculate item popularity")

    parser.add_argument('--data', nargs='?', default='data',
                        help='data directory')
    return parser.parse_args()


if __name__ == '__main__':
    # Network parameters
    args = parse_args()

    data_directory = args.data
    replay_buffer_behavior = pd.read_pickle(os.path.join(data_directory, 'sampled_sessions.df'))
    total_actions=replay_buffer_behavior.shape[0]
    pop_dict={}
    for index, row in replay_buffer_behavior.iterrows():
        action=row['item_id']
        if action in pop_dict:
            pop_dict[action]+=1
        else:
            pop_dict[action]=1
        if index%100000==0:
            print (index/100000)
    for key in pop_dict:
        pop_dict[key]=float(pop_dict[key])/float(total_actions)
    f = open('pop_dict.txt', 'w')
    f.write(str(pop_dict))
    f.close()