
# 導入相關聯的包
import os
from kaggle.api.kaggle_api_extended import KaggleApi

try:
    # 實例KaggleApi,并且進行登錄驗證
    api = KaggleApi()
    api.authenticate()

    # 存儲的路徑，如果已經存在就忽略，不存在就創建
    save_path = r"D:\Jasper\Learning\data\kaggle"
    os.makedirs(save_path, exist_ok=True)

    # 下載指定的數據集
    api.dataset_download_files(
        dataset='ruchikakumbhar/uber-dataset',  # 指定下載數據集名稱
        path=save_path,                         # 指定保存的路徑
        unzip=True                              # 默認解壓文件
    )

    print("資料已經下載成功!")

except Exception as e:
    print(f"下載數據失敗：{e}")
