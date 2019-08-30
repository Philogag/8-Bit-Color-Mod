"""
本脚本通过读取材质包中的每种材质并为其注册方块
默认 为 清除所有材质后 构造256色 纯色 材质
运行完后 可通过IDEA测试是否正常
"""

import os
import sys

from func.write.write_MakeBlockList import write_MakeBlockList
from func.write.write_Lang import write_Lang
from func.write.write_blockstates import write_blockstates
from func.write.write_models_block import write_models_block
from func.write.write_models_item import write_models_item

from func.clear.cleardir import cleardir

#######################################
# 颜色生成器，最多启用一种
# 256色生成器，共216种颜色
from func.color.color256 import makeColor

# 24位色生成器，共 1.6e7 种颜色，根本没法用
# from func.color.color24 import makeColor
#######################################


basepath = R"D:\ModCreate\FullColorMod-forge-1.12.2-14.23.5.2783-idea\src\main"
objectname = "fcbm"

#######################################
# 清空历史
print("Clear Old Data")
cleardir(basepath + R"\resources\assets\fcbm\blockstates")
cleardir(basepath + R"\resources\assets\fcbm\models\block")
cleardir(basepath + R"\resources\assets\fcbm\models\item")
# 清空材质包
# 如想通过自定义材质定义方块，请注释该语句
cleardir(basepath + R"\resources\assets\fcbm\textures\blocks")
#######################################

#######################################
# 构造颜色 // 非必要
# 可以通过自定义 makeColor函数 实现不同配色
print("Make Color")
makeColor(basepath)
#######################################

#######################################
# 遍历材质包
k = os.listdir(basepath + R"\resources\assets\fcbm\textures\blocks")
ls = []
for f in k:
    ls.append(f.split('.')[0])
#######################################

#######################################
# 注册方块
write_MakeBlockList(ls, basepath)
#######################################

#######################################
# 注册语言包
# 创造背包栏名称
CreativeTabName = "8 Bit Color (256 Color)"
write_Lang(ls, basepath, CreativeTabName)
#######################################

#######################################
# 设置方块结构
write_blockstates(ls, basepath)
#######################################

#######################################
# 设置方块模型
write_models_block(ls, basepath)
#######################################

#######################################
# 设置方块物品模型
write_models_item(ls, basepath)
#######################################

print("Over")