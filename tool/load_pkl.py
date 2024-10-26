import pickle

# 打开.pkl文件
with open('E:\Work\THU\code\THU_Project_project\data\zivid_labels/2024-04-03-13-32-05.pkl', 'rb') as f:
    # 使用pickle.load()函数加载数据
    data = pickle.load(f)

# 打印数据
print(data)