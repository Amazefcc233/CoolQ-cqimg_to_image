# -*- coding: utf8 -*-
import cqimg
import tmpedit
import nulledit

while (True):
    print ("1: cqimg转正常格式文件")
    print ("2: tmp转jpg（批量修改后缀名）")
    print ("3: null转jpg（批量修改后缀名）")
    print ("4: 退出")
    select=int(input("请选择: "))
    if select == 1:
        cqimg.main()
    elif select == 2:
        tmpedit.main()
    elif select == 3:
        nulledit.main()
    elif select == 4:
        print ("告辞！")
        break