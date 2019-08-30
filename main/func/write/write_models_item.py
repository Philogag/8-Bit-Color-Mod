def write_models_item(ls, basepath):
    print("Write Models Item")
    for s in ls:
        with open(basepath + R"\resources\assets\fcbm\models\item\%s.json" % s, 'w') as f:
            f.write("""{
  "parent": "fcbm:block/%s"
}"""%s)