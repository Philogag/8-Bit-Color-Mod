def write_models_block(ls, basepath):
    print("Write Models Block")
    for s in ls:
        with open(basepath + R"\resources\assets\fcbm\models\block\%s.json" % s, 'w') as f:
            f.write("""{
  "parent": "block/cube_all",
  "textures": {
    "all": "fcbm:blocks/%s"
  }
}"""%s)