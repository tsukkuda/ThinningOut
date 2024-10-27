import os
import random
import shutil
from datetime import datetime
from tqdm import tqdm
from logMaker import logMaker0,logMaker1,logMaker2
from SubMain import SubMain


###*ここからパス関連の部分###
# 成型済みデータフォルダ
source_dir = 'E:\Data\data_formed\hachi_15s'
# 成型済みデータフォルダ #*サブ
subSource_dir = ''
mixFlag=False

# 大元の出力先
base_dir = 'E:\Result_UsedData'
# 現在の時刻
current_datetime = datetime.now().strftime('%Y-%m-%d-%Hh%Mm%Ss')
# 学習用と検証用
learning_dir='\車両追跡データ'
validation_dir='\検証用車両追跡データ\ADV比率3割'

# 出力先パス(2種類)
result_path1=base_dir+'/'+current_datetime+'/usedData'+learning_dir
result_path2=base_dir+'/'+current_datetime+'/usedData'+validation_dir
# 出力先フォルダ作成
os.makedirs(result_path1,exist_ok=True)
os.makedirs(result_path2,exist_ok=True)
###*ここまでパス関連の部分###


###*ここから間引き関連###
#! 各フォルダから間引くファイルの数
split_num = 1000  # 学習用各フォルダからこの数をランダムに選択

#! 間引く際の乱数seed値
seed1=random.randint(1,9999) #学習用
seed2=random.randint(1,9999) #検証用
# seed1=42    #*手動で設定する場合
# seed2=78    

#! 学習用データのフォルダ数(seed数*日数)
learning_num=30

#! 学習用データのフォルダ数(seed数*日数) 2
subLearning_num=30

#! 検証用データのフォルダ数(seed数*日数)
validation_num=30
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

start_time=datetime.now() #開始時間
###*ここまで記録関連###


###*ここから学習データ間引き###
print("Now thinning out csv files for learning data...")

random.seed(seed1)  #*seed設定

# 各サブフォルダ内のファイルを処理
for i,foldername in enumerate(tqdm(os.listdir(source_dir),position=0)):
    if i >= learning_num:
        break
    
    tqdm.write(f"Now processing : {foldername}", end="")
    
    #フォルダ名記録
    learning_foldersAp(foldername)
    
    #大量のcsvファイルが置いてあるパス
    folder_path = os.path.join(source_dir, foldername) + '/Type0'

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


###*ここから検証データ間引き###
print("Now thinning out csv files for validation data...")

random.seed(seed2)  #*seed設定

#逆順にフォルダ名取得
file_rev_list = sorted(os.listdir(source_dir), reverse=True)
# 各サブフォルダ内のファイルを処理
for i, foldername in enumerate(tqdm(file_rev_list,position=0)):
    if i >= validation_num:
        break
    
    tqdm.write(f"Now processing : {foldername}", end="")
    
    #フォルダ名記録
    validation_foldersAp(foldername)
    
    #大量のcsvファイルが置いてあるパス
    folder_path = os.path.join(source_dir, foldername) + '/Type0'

    # サブフォルダであるか確認
    if os.path.isdir(folder_path):
        # サブフォルダ内のすべてのファイルを取得
        all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        whole_data2Ap(len(all_files))    # カウント

        # ファイルが間引く数より多い場合はランダムに選択
        if len(all_files) > split_num:
            selected_files = random.sample(all_files, split_num)
        else:
            selected_files = all_files  # ファイル数が少ない場合はそのまま選択
        after_data2Ap(len(selected_files))   #カウント

        # 選択したファイルをターゲットディレクトリにコピー
        for file in selected_files:
            shutil.copy(file, result_path2)
    
    tqdm.write(f"\rprocessed : {foldername} :  {whole_data2[-1]:>5} -> {after_data2[-1]:>5}")

print("thined out csv files for validation data.")
print()
###*ここまで検証データ間引き###

###*ここからログ生成###
print("------------")
log_path=base_dir+'/'+current_datetime+'/usedData'  #ログ出力先
#全体ログ
logMaker0(log_path,current_datetime,split_num,source_dir,
             learning_num,seed1,whole_data1,after_data1,    #学習データ
             validation_num,seed2,whole_data2,after_data2) #検証データ
#学習データ詳細ログ
logMaker1(log_path,current_datetime,
             learning_num,seed1,learning_folders,whole_data1,after_data1)
#検証データ詳細ログ
logMaker2(log_path,current_datetime,
             validation_num,seed2,validation_folders,whole_data2,after_data2)
print("------------")
###*ここまでログ作成###

###*ここからmix###
if mixFlag:
    SubMain(subSource_dir,current_datetime,split_num,subLearning_num,result_path1)
###*ここまでmix###

end_time=datetime.now() #終了時間

print()
print("------------")
print(f"total data BEFORE processing : {sum(whole_data1)+sum(whole_data2)}")
print(f"total data AFTER processing : {sum(after_data1)+sum(after_data2)}")
print(f"processing time : {end_time - start_time}")
print("------------")
print()

print("Done! thx for waiting:)")
