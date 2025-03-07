import os

def addTab(path):
    try:
        # 讀取 alt_tab.py 位置
        file_path = os.path.dirname(os.path.abspath(__file__))
        print("目前所在的資料夾：", file_path)

        # 將 alt_tab.txt 位置修正
        txt_path = os.path.join(file_path, path)
        print("alt_tab.txt 的正確位置：", txt_path)

        # 讀取文件內容
        with open(txt_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 在每行後添加兩個空格
        updated = list()

        for line in lines:
            updated.append(line.rstrip() + '  \n')
        
        # 寫回文件
        with open(path, 'w', encoding='utf-8') as file:
            file.writelines(updated)
        
        print("已成功在每行結尾添加兩個空格：", path)
    except Exception as e:
        print("發生錯誤：", e)

path = "alt_tab.txt"
addTab(path)
