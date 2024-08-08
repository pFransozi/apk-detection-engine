import pandas as pd
from urllib.request import urlopen
import random
import os
import threading

hash_list = []

def download_and_save_apk(hash256_list, apk_class):

    apk_dir = "../../apks/goodware/" if apk_class == 0 else "../../apks/malware/"
    api_key = ""
    
    for hash in hash256_list:

        url = f"https://androzoo.uni.lu/api/download?apikey={api_key}&sha256={hash}"
        filename = f"{apk_dir}{hash}.apk"

        with urlopen(url) as file:
            try:
                content = file.read()
                print(f"{filename} - {apk_class}")
                with open(filename, "wb") as download:
                    download.write(content)

            except Exception as error:
                print(f"{filename} - {apk_class} - error: {error}")


hash256_goodware = []
hash256_malware = []
threads = []
random_seed = 67_777
thread_step = 1_000
apk_list_size = 20_000


for df in pd.read_csv("./latest.csv", iterator=True, chunksize=10_000):

    df.vt_scan_date = pd.to_datetime(df.vt_scan_date, format='ISO8601')

    df = df[(df['vt_scan_date'].dt.strftime('%Y-%m-%d') >= '2023-02-27') & 
                    (df['vt_scan_date'].dt.strftime('%Y-%m-%d') <= '2023-09-31') & 
                    (df['apk_size'] > 500_001) & (df['apk_size'] < 80_000_001)]

    hash256_goodware += df.query('vt_detection == 0')['sha256'].to_list()
    hash256_malware += df.query('vt_detection > 1')['sha256'].to_list()

random.seed(random_seed)
hash256_goodware = random.choices(hash256_goodware, k=apk_list_size)
hash256_malware = random.choices(hash256_malware, k=apk_list_size)

for start_range in range(0, apk_list_size, thread_step):

    threads.append(threading.Thread(target=download_and_save_apk, args=(
                                                    hash256_goodware[start_range:start_range + thread_step]
                                                    ,0)))
    threads.append(threading.Thread(target=download_and_save_apk, args=(
                                                    hash256_malware[start_range:start_range + thread_step]
                                                    , 1)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()