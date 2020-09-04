import os
import shutil
try:
    shutil.rmtree("./database")
    print("数据库删除成功，准备重置")
except:
    print("database删除失败")
try:
    os.remove("recorded_data.npy")
    print("日志文件成功删除，准备重置")
except:
    print("日志文件删除失败")
try:
    os.mkdir("./database")
    print("建立数据库目录成功")
except:
    print("建立数据库目录失败")
print("建立数据库")
os.system("python generate_database_from_categories.py")
