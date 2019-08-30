def write_MakeBlockList(ls, basepath):
    print("Write MakeBlockList")
    with open(basepath + R"\java\com\philogag\fcbm\register\MakeBlockList.java",'w') as f:
        f.write(R"""package com.philogag.fcbm.register;

import com.philogag.fcbm.block.RGB_BLOCK;
import net.minecraft.block.Block;

import java.util.ArrayList;

public class MakeBlockList {
    public static ArrayList<Block> list = new ArrayList<>();
    public MakeBlockList(){
""")
        for s in ls:
            f.write("        this.list.add(new RGB_BLOCK(\"%s\"));\n"% s)
        f.write("""    }
}""")
