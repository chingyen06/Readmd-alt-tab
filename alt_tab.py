def addTab(path):
    try:
        # 讀取文件內容
        with open(path, 'r', encoding='utf-8') as file:
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

path = "alttab.txt"
addTab(path)