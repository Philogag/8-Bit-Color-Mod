def write_blockstates(ls, basepath):
    print("Write Blockstates")
    for s in ls:
        with open(basepath + R"\resources\assets\fcbm\blockstates\%s.json"%(s), 'w') as f:
            f.write("""{
  "variants": {
    "normal":{ "model": "fcbm:%s" }
  }
}""" % s)
