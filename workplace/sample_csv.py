import shutil
import random
import csv
import os

basic_path = '../data/docs/'
sample_path = '../data/sample_docs2/'
file_size_thres = 5120


def random_sample_files(total_size, target_sample_size=300):
    is_finished = False
    num_sampled = 0
    while True:
        for alphabet in os.listdir(basic_path):
            alphabet_path = basic_path + alphabet + '/'
            for csv_file in os.listdir(alphabet_path):
                if os.path.getsize(alphabet_path + csv_file) < file_size_thres:
                    continue
                if random.randint(1,total_size) > target_sample_size:
                    continue
                if os.path.exists(sample_path + csv_file):
                    continue
                num_sampled += 1
                shutil.copyfile(alphabet_path + csv_file, sample_path + csv_file)
                if num_sampled >= target_sample_size:
                    is_finished = True
                    break
            if is_finished:
                break
        if is_finished:
            break

random_sample_files(total_size=20970, target_sample_size=300)



