def add_record():
    """添加一条学习记录"""
    date = input("输入日期（比如 2024-03-18）：")
    content = input("输入今天学了什么：")
    with open(r"C:\Users\Etern\Desktop\study_records.txt", 'a', encoding='utf-8') as f:
        f.write(f"{date}|{content}\n")
    print("✅ 记录成功！")

def show_record():
    """显示所有学习记录"""
    try:
        with open(r"C:\Users\Etern\Desktop\study_records.txt", 'r', encoding='utf-8') as f:
            records = f.readlines()
        
        print("\n=== 学习记录 ===")
        if not records:
            print("📭 还没有记录")
        else:
            for record in records:
                date, content = record.strip().split("|")
                print(f"📅 {date}: {content}")
    except FileNotFoundError:
        print("📭 还没有记录哦，先添加一条吧")

def delete_record():
    """清空所有学习记录"""
    confirm = input("⚠️ 确定要清空所有记录吗？(y/n): ")
    if confirm.lower() == 'y':
        with open(r"C:\Users\Etern\Desktop\study_records.txt", 'w', encoding='utf-8') as f:
            f.write("")  # 写入空字符串，清空文件
        print("🗑️ 所有记录已清空！")
    else:
        print("取消操作")

# 主程序
while True:
    print("\n" + "="*20)
    print("📝 学习记录本")
    print("1. 添加记录")
    print("2. 查看记录")
    print("3. 清空记录")
    print("4. 退出")
    print("="*20)
    
    option = input("请选择操作 (1/2/3/4): ")  # 这里要改成4个选项
    
    if option == '1':
        add_record()
    elif option == '2':
        show_record()
    elif option == '3':
        delete_record()
    elif option == '4':
        print("👋 再见！")
        break
    else:
        print("❌ 输入错误，请输入 1-4")