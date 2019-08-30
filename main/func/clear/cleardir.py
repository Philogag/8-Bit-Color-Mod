import os
def cleardir(dirpath):
    if not os.path.exists(dirpath):
        return
    ls = os.listdir(dirpath)
    for i in ls:
        os.remove(dirpath + "\\" + i)


if __name__ == "__main__":
    cleardir(R"D:\ModCreate\FullColorMod-forge-1.12.2-14.23.5.2783-idea\src\main\resources\assets\fcbm\models\block")
