#!/usr/bin/env python
# coding=utf-8

cmn = "cmn_test_gold.tab"
eng = "eng_test_gold.tab"
spa = "spa_test_gold.tab"
gold = "test_gold.tab"

fcmn = open(cmn,'w')
feng = open(eng,'w')
fspa = open(spa,'w')

with open(gold,'r') as fo:
    lines = fo.readlines()
    for line in lines:
        print line
        if "CMN" in line:
            fcmn.write(line)
        elif "ENG" in line:
            feng.write(line)
        else: 
            fspa.write(line)

fo.close()
fcmn.close()
feng.close()
fspa.close()
