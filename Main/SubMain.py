
#* Main.pyとは異なる形成データからも抽出を行うプログラム．
#* Main.pyの18行目のmixFlag=Trueのとき動作する．

import os
import random
import shutil
from datetime import datetime
from tqdm import tqdm
from logMaker import logMaker0,logMaker1,logMaker2


###*ここからパス関連の部分###
# 大元の出力先
base_dir = 'E:\Result_UsedData'
###*ここまでパス関連の部分###


###*ここから間引き関連###
#! 間引く際の乱数seed値
seed1=random.randint(1,9999) #学習用
seed2=random.randint(1,9999) #検証用
# seed1=42    #*手動で設定する場合
# seed2=78    

validation_num=-1
###*ここまで間引き関連###


###*ここから記録関連###
#学習データ
whole_data1=[] #各フォルダで間引く前のファイル数
whole_data1Ap=whole_data1.append
after_data1=[] #各フォルダで間引いた後のファイル数
after_data1Ap=after_data1.append
learning_folders=[] #学習データ抽出元フォルダ名
learning_foldersAp=learning_folders.append

#検証データ
whole_data2=[] #各フォルダで間引く前のファイル数
whole_data2Ap=whole_data2.append
after_data2=[] #各フォルダで間引いた後のファイル数
after_data2Ap=after_data2.append
validation_folders=[] #検証データ抽出元フォルダ名
validation_foldersAp=validation_folders.append
###*ここまで記録関連###

def SubMain(subSource_dir,current_datetime,split_num,learning_num,result_path1):
    ###*ここから学習データ間引き###
    print("\n\n#####Start SUB section#####")
    print("Now thinning out csv files for learning data...")

    random.seed(seed1)  #*seed設定

    # 各サブフォルダ内のファイルを処理
    for i,foldername in enumerate(tqdm(os.listdir(subSource_dir),position=0)):
        if i >= learning_num:
            break
        
        tqdm.write(f"Now processing : {foldername}", end="")

        #フォルダ名記録
        learning_foldersAp(foldername)

        #大量のcsvファイルが置いてあるパス
        folder_path = os.path.join(subSource_dir, foldername) + '/Type0'

        # サブフォルダであるか確認
        if os.path.isdir(folder_path):
            # サブフォルダ内のすべてのファイルを取得
            all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            whole_data1Ap(len(all_files))    # カウント

            # ファイルが間引く数より多い場合はランダムに選択
            if len(all_files) > split_num:
                selected_files = random.sample(all_files, split_num)
            else:
                selected_files = all_files  # ファイル数が少ない場合はそのまま選択
            after_data1Ap(len(selected_files))   #カウント

            # 選択したファイルをターゲットディレクトリにコピー
            for file in selected_files:
                shutil.copy(file, result_path1)

        tqdm.write(f"\rprocessed : {foldername} :  {whole_data1[-1]:>5} -> {after_data1[-1]:>5}")

    print("thined out csv files for learning data.")
    print()
    ###*ここまで学習データ間引き###

    ###*ここからログ生成###
    print("------------")
    log_path=base_dir+'/'+current_datetime+'/usedData/subMixLog'  #ログ出力先
    os.makedirs(log_path,exist_ok=True)
    #全体ログ
    logMaker0(log_path,current_datetime,split_num,subSource_dir,
                 learning_num,seed1,whole_data1,after_data1,    #学習データ
                 validation_num,seed2,whole_data2,after_data2
                 ) #検証データ
    #学習データ詳細ログ
    logMaker1(log_path,current_datetime,
                 learning_num,seed1,learning_folders,whole_data1,after_data1)
    print("------------")
    ###*ここまでログ作成###
    
    print("\n#####Done SUB section#####")