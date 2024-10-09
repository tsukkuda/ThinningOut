import os

#概要ログ
def logMaker0(log_path,current_datetime,split_num,
             learning_num,seed1,whole_data1,after_data1,    #学習データ
             validation_num,seed2,whole_data2,after_data2): #検証データ
    file_name=current_datetime+"_log.txt"
    
    print("Now making log...", end="")
    
    with open(os.path.join(log_path, file_name), "w") as file:
        #日付
        file.write(f"---Log of {current_datetime}---\n")
        
        #1フォルダあたりのファイル数
        file.write(f"{split_num} files per 1 sim folder\n")
        
        #学習データ情報
        file.write(f"learning : {learning_num} sims, seed value {seed1}, min {min(whole_data1)}\n")
        
        #検証データ情報
        file.write(f"validation : {validation_num} sims, seed value {seed2}\n")
        
        #総データ数
        file.write(f"total files : {sum(whole_data1)+sum(whole_data2)} -> {sum(after_data1)+sum(after_data2)}\n\n")
        
        file.write("Remainder intentionally left blank")
    
    print(" Done!")



#学習データの詳細ログ
def logMaker1(log_path,current_datetime,
             learning_num,seed1,learning_folders,whole_data1,after_data1):
    file_name=current_datetime+"_learning_log.txt"
    
    print("Now making detail log of learning data...", end="")
    
    with open(os.path.join(log_path, file_name), "w") as file:
        #日付
        file.write(f"---Log of {current_datetime}---\n")
        
        #学習データ情報
        file.write(f"learning : {learning_num} sims, seed value {seed1}\n")
        
        #総データ数
        file.write(f"total files : {sum(whole_data1)} -> {sum(after_data1)}\n\n")
        
        #データ詳細(フォルダ名、ファイル数)
        file.write("***Detail of learning data***\n")
        for i,val in enumerate(whole_data1):
            file.write(f"{learning_folders[i]} : {val} -> {after_data1[i]}\n")
        file.write("\nRemainder intentionally left blank")
    
    print(" Done!")



#検証データの詳細ログ
def logMaker2(log_path,current_datetime,
             validation_num,seed2,validation_folders,whole_data2,after_data2):
    file_name=current_datetime+"_validation_log.txt"
    
    print("Now making detail log of validation data...",end="")
    
    with open(os.path.join(log_path, file_name), "w") as file:
        #日付
        file.write(f"---Log of {current_datetime}---\n")
        
        #検証データ情報
        file.write(f"validation : {validation_num} sims, seed value {seed2}\n")
        
        #総データ数
        file.write(f"total files : {sum(whole_data2)} -> {sum(after_data2)}\n\n")
        
        #データ詳細(フォルダ名、ファイル数)
        file.write("***Detail of validation data***\n")
        for i,val in enumerate(whole_data2):
            file.write(f"{validation_folders[i]} : {val} -> {after_data2[i]}\n")
        file.write("\nRemainder intentionally left blank")
    
    print(" Done!")