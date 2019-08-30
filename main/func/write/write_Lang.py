def write_Lang(ls, basepath, createtab):
    print("Write Lang")
    with open(basepath + R"\resources\assets\fcbm\lang\en_us.lang", "w") as f:
        f.write("itemGroup.rgb_tab=%s\n"%createtab)
        for s in ls:
            f.write("tile.%s.name=RGB %s\n"%(s,s.split('_')[1].upper()))
