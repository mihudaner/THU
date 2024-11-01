import json
import os

# 要存储的配置数据
config = {
    "path1": "/path/to/file1",
    "path2": "/path/to/file2",
    "path3": "/path/to/file3"
}

# 写入 JSON 文件
with open('../new_thu/resource/config.json', 'w') as json_file:
    json.dump(config, json_file, indent=4)

# 读取 JSON 文件
with open('../new_thu/resource/config.json', 'r') as json_file:
    loaded_config = json.load(json_file)

print(loaded_config)
