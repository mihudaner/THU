import os

def generate_project_structure(path, indent=0):
    """递归生成目录结构图"""
    if not os.path.exists(path):
        print(f"路径 '{path}' 不存在")
        return

    items = os.listdir(path)
    items.sort()
    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print("│   " * indent + f"├── {item}/")
            generate_project_structure(full_path, indent + 1)
        # 只生成py ,ui,txt文件的结构
        elif item.endswith(('.py', '.ui', '.txt')):
            print("│   " * indent + f"├── {item}")

def main():
    project_path = "../"  # 替换为你的项目路径
    print(f"{os.path.basename(project_path)}/")
    generate_project_structure(project_path)

if __name__ == "__main__":
    main()
