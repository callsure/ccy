#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random


class methodObject:
    """方法的类"""
    def __init__(self, methodName, needRetuen, returnType, params, fName):
        self.methodName = methodName
        self.needRetuen = needRetuen
        self.returnType = returnType
        self.params = params
        self.fName = fName

classArray = ['NSString*','int', 'long']

#创建方法
def create_method(methodName):
    methodObject_1 = methodObject()
    needRetuen = random.randint(0, 1)
    if needRetuen == 0:
        #不需要返回值
        methodObject_1.needRetuen = False
        methodObject_1.returnType = ''
    else:
        methodObject_1.needRetuen = True
        methodObject_1.returnType = random.choice(classArray)
    number = random.randint(0, 5)
    methodObject_1.numParam = number
    methodObject_1.methodName = methodName
    return methodObject_1

#随机一个类型
def randomType():
    strs = random.choice(classArray)
    return strs

#实现简单的逻辑操作
def handle_method(returnType, params):
    res =''
    # param = ''
    # if params:
    #     param = random.choice(params)
    # else:
    #     pass
    if returnType == 'NSString*':
        res += '\tNSString *same = @"ok了";\n'
        res += handle_param(returnType)
        res += '\treturn same;\n'
    elif returnType == 'int':
        res += '\tint same = ' + str(random.randint(0, 100)) + ';\n'
        res += handle_param(returnType)
        res += '\treturn same;\n'
    elif returnType == 'NSInteger*':
        pass
    elif returnType == 'long':
        res += '\tlong same = ' + str(random.randint(0, 100)) + ';\n'
        res += handle_param(returnType)
        res += '\treturn same;\n'
    else:
        res += handle_param(returnType)
    return res

marks = ['+', '-', '*', '/']
def handle_param(returnType):
    res = ''
    i = random.randint(1, 21)
    if i == 1:
        res += '\tNSString* strType = @"i love apple";\n\tNSLog(@"输出了：%@",strType);\n'
    elif i == 2:
        res += '\tint price = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tint num = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tint rate = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tint sum = price ' + random.choice(marks) + ' num ' + random.choice(marks) + ' rate;\n'
        res += '\tNSLog(@"商品的总值：%d",sum);\n'
    elif i == 3:
        res += '\tlong times = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tint count = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tlong sum = times ' + random.choice(marks) + ' count;\n'
        res += '\tNSLog(@"价格的倍数的总值：%ld",sum);\n'
    elif i == 4:
        res += '\tNSString *shareType = @"0";\n'
        res += '\t// 分享ID，32位MD5字符串；生成规则=MD5(createTime+shareType+groupId+userId+”jeagine” 注：jeagine固定写)\n'
        res += '\tNSString *groupId = @"771";\n'
        res += '\tNSString * userId = @"5058";\n'
        res += '\tNSDateFormatter *formatter = [[NSDateFormatter alloc] init];\n'
        res += '\t[formatter setDateStyle:NSDateFormatterMediumStyle];\n'
        res += '\t[formatter setTimeStyle:NSDateFormatterShortStyle];\n'
        res += '\t[formatter setDateFormat:@"YYYY-MM-dd HH:mm:ss SSS"];\n'
        res += '\tNSTimeZone* timeZone = [NSTimeZone timeZoneWithName:@"Asia/Beijing"];\n'
        res += '\t[formatter setTimeZone:timeZone];\n'
        res += '\tNSDate *datenow = [NSDate date];\n'
        res += '\tNSString *timestamp = [NSString stringWithFormat:@"%ld", (long)([datenow timeIntervalSince1970] * 1000)];\n'
        res += '\tNSString * tempStr = [NSString stringWithFormat:@"%@%@%@%@ffff", timestamp, shareType, groupId, userId];\n'
        res += '\tconst char *original_str = [tempStr UTF8String];\n'
        res += '\tunsigned char result[CC_MD5_DIGEST_LENGTH];\n'
        res += '\tCC_MD5(original_str, strlen(original_str), result);\n'
        res += '\tNSMutableString *hash = [NSMutableString string];\n'
        res += '\tfor (int i = 0; i < CC_MD5_DIGEST_LENGTH; i++)\n'
        res += '\t\t[hash appendFormat:@"%02x", result[i]];\n'
        res += '\tNSString *idString = [hash lowercaseString];\n'
        res += '\tNSDictionary *dic = @{@"userId":userId, @"groupId":groupId, @"shareType":shareType, @"createTime":timestamp, @"id":idString};\n'
        res += '\tNSLog(@"%@",dic);\n'
    elif i == 5:
        res += '\tint count = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tfor (int i = 0; i < 101; i++){\n'
        res += '\t\tif (i == count) {\n'
        res += '\t\t\tNSLog(@"count：%d",i);\n'
        res += '\t\t}\n'
        res += '\t}\n'
    elif i == 6:
        res += '\tint len = ' + str(random.randint(1, 100)) + ';\n'
        res += '\tchar ch[len];\n'
        res += '\tfor (int index=0; index<len; index++) {\n'
        res += '\t\tint num = arc4random_uniform(58)+65;\n'
        res += '\t\tif (num>90 && num<97) { num = num%90+65; }\n'
        res += '\t\tch[index] = num;\n'
        res += '\t}\n'
    elif i == 7:
        hh = ''
        lens = random.randint(10, 50)
        for i in range(lens):
            hh += '@' + str(random.randint(1, 100)) + ','
        hh = hh[:len(hh) - 1]
        res += '\tNSMutableArray *array = @[' + hh + '].mutableCopy;\n'
        res += '\tint low = 0;\n'
        res += '\tint high = ' + str(lens - 1) + ';\n'
        res += '\tif(array == nil || array.count == 0){\n'
        if returnType == 'NSString*':
            res += '\t\treturn @"";\n'
        elif returnType == 'int':
            res += '\t\treturn 0;\n'
        elif returnType == 'long':
            res += '\t\treturn 0;\n'
        else:
            res += '\t\treturn;\n'
        res += '\t}\n'
        res += '\tif (low >= high) {\n'
        if returnType == 'NSString*':
            res += '\t\treturn @"";\n'
        elif returnType == 'int':
            res += '\t\treturn 0;\n'
        elif returnType == 'long':
            res += '\t\treturn 0;\n'
        else:
            res += '\t\treturn;\n'
        res += '\t}\n'
        res += '\t//取中值\n'
        res += '\tint middle = low + (high - low)/2;\n'
        res += '\tNSNumber *prmt = array[middle];\n'
        res += '\tint i = low;\n'
        res += '\tint j = high;\n'
        res += '\t//开始排序，使得left<prmt 同时right>prmt\n'
        res += '\twhile (i <= j) {\n'
        res += '\t\t//while ([array[i] compare:prmt] == NSOrderedAscending) {  该行与下一行作用相同\n'
        res += '\t\twhile ([array[i] intValue] < [prmt intValue]) {\n'
        res += '\t\t\ti++;\n'
        res += '\t\t}\n'
        res += '\t\t//while ([array[j] compare:prmt] == NSOrderedDescending) { 该行与下一行作用相同\n'
        res += '\t\twhile ([array[j] intValue] > [prmt intValue]) {\n'
        res += '\t\t\tj--;'
        res += '\t\t}\n'
        res += '\t\tif(i <= j){\n'
        res += '\t\t\t[array exchangeObjectAtIndex:i withObjectAtIndex:j];\n'
        res += '\t\t\ti++;\n'
        res += '\t\t\tj--;\n'
        res += '\t\t}\n'
        res += '\t\tprintf("排序中:");\n'
        res += '\t}\n'
    elif i == 8:
        hh = ''
        lens = random.randint(10, 50)
        for i in range(lens):
            hh += '@' + str(random.randint(1, 100)) + ','
        hh = hh[:len(hh) - 1]
        res += '\tNSMutableArray *array = @[' + hh + '].mutableCopy;\n'
        res += '\tif(array == nil || array.count == 0){\n'
        if returnType == 'NSString*':
            res += '\t\treturn @"";\n'
        elif returnType == 'int':
            res += '\t\treturn 0;\n'
        elif returnType == 'long':
            res += '\t\treturn 0;\n'
        else:
            res += '\t\treturn;\n'
        res += '\t}\n'
        res += '\tfor (int i = 1; i < array.count; i++) {\n'
        res += '\t\tfor (int j = 0; j < array.count - i; j++) {\n'
        res += '\t\t\tif ([array[j] compare:array[j+1]] == NSOrderedDescending) {\n'
        res += '\t\t\t\t[array exchangeObjectAtIndex:j withObjectAtIndex:j+1];\n'
        res += '\t\t\t}\n'
        res += '\t\t\tprintf("排序中:");\n'
        res += '\t\t}\n'
        res += '\t}\n'
    elif i == 9:
        hh = ''
        lens = random.randint(10, 50)
        for i in range(lens):
            hh += '@' + str(random.randint(1, 100)) + ','
        hh = hh[:len(hh) - 1]
        res += '\tNSMutableArray *array = @[' + hh + '].mutableCopy;\n'
        res += '\tif(array == nil || array.count == 0){\n'
        if returnType == 'NSString*':
            res += '\t\treturn @"";\n'
        elif returnType == 'int':
            res += '\t\treturn 0;\n'
        elif returnType == 'long':
            res += '\t\treturn 0;\n'
        else:
            res += '\t\treturn;\n'
        res += '\t}\n'
        res += '\tint min_index;\n'
        res += '\tfor (int i = 0; i < array.count; i++) {\n'
        res += '\t\tmin_index = i;\n'
        res += '\t\tfor (int j = i + 1; j<array.count; j++) {\n'
        res += '\t\t\tif ([array[j] compare:array[min_index]] == NSOrderedAscending) {\n'
        res += '\t\t\t\t[array exchangeObjectAtIndex:j withObjectAtIndex:min_index];\n'
        res += '\t\t\t}\n'
        res += '\t\t\tprintf("排序中:");\n'
        res += '\t\t}\n'
        res += '\t}\n'
    elif i == 10:
        hh = ''
        lens = random.randint(10, 50)
        for i in range(lens):
            hh += '@' + str(random.randint(1, 100)) + ','
        hh = hh[:len(hh) - 1]
        res += '\tNSMutableArray *array = @[' + hh + '].mutableCopy;\n'
        res += '\tif(array == nil || array.count == 0){\n'
        if returnType == 'NSString*':
            res += '\t\treturn @"";\n'
        elif returnType == 'int':
            res += '\t\treturn 0;\n'
        elif returnType == 'long':
            res += '\t\treturn 0;\n'
        else:
            res += '\t\treturn;\n'
        res += '\t}\n'
        res += '\tfor (int i = 0; i < array.count; i++) {\n'
        res += '\t\tNSNumber *temp = array[i];\n'
        res += '\t\tint j = i-1;\n'
        res += '\t\twhile (j >= 0 && [array[j] compare:temp] == NSOrderedDescending) {\n'
        res += '\t\t\t[array replaceObjectAtIndex:j+1 withObject:array[j]];\n'
        res += '\t\t\tj--;\n'
        res += '\t\t\tprintf("排序中:");\n'
        res += '\t\t}\n'
        res += '\t[array replaceObjectAtIndex:j+1 withObject:temp];\n'
        res += '\t}\n'
    elif i == 11:
        res += '\tint count = 0;\n'
        res += '\tint leng = ' + str(random.randint(200, 300)) + ';\n'
        res += '\tfor (int i = 101; i < leng; i+=2) {\n'
        res += '\t\tbool flag = true;\n'
        res += '\t\tfor(int j = 2; j <= sqrt(i); j++) {\n'
        res += '\t\t\tif(i%j == 0) {\n'
        res += '\t\t\t\tflag = false;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t\t}\n'
        res += '\t\t}\n'
        res += '\t\tif (flag == true) {\n'
        res += '\t\t\tcount++;\n'
        res += '\t\t\tNSLog(@"ss:%d", i);\n'
        res += '\t\t}\n'
        res += '\t}\n'
    elif i == 12:
        res += '\tint n = ' + str(random.randint(100, 300)) + ';\n'
        res += '\tint k= 2;\n'
        res += '\twhile (n >= k) {\n'
        res += '\t\tif (n == k) {\n'
        res += '\t\t\tNSLog(@"k：%d",k);\n'
        res += '\t\t\tbreak;\n'
        res += '\t\t} else if (n % k == 0) {\n'
        res += '\t\t\tNSLog(@"k：%d",k);\n'
        res += '\t\t\tn = n / k;\n'
        res += '\t\t} else {\n'
        res += '\t\t\tk++;\n'
        res += '\t\t}\n'
        res += '\t}\n'
    elif i == 13:
        res += '\tint a = ' + str(random.randint(1, 300)) + ';\n'
        res += '\tint b = ' + str(random.randint(1, 300)) + ';\n'
        res += '\tif (a < b) {\n'
        res += '\t\tint t = b;\n'
        res += '\t\tb = a;\n'
        res += '\t\ta = t;\n'
        res += '\t}\n'
        res += '\twhile (b != 0) {\n'
        res += '\t\tif (a == b) {\n'
        res += '\t\t\tbreak;\n'
        res += '\t\t}\n'
        res += '\t\tint x = b;\n'
        res += '\t\tb = a % b;\n'
        res += '\t\ta = x;\n'
        res += '\t}\n'
        res += '\tNSLog(@"最小公因数：%d",a);\n'
    elif i == 14:
        res += '\tint a = ' + str(random.randint(1, 80)) + ';\n'
        res += '\tint n = ' + str(random.randint(1, 20)) + ';\n'
        res += '\tint sum = 0, b = 0;\n'
        res += '\tfor (int i=0; i<n; i++) {\n'
        res += '\t\tb += a;\n'
        res += '\t\tsum += b;\n'
        res += '\t\ta = a * 10;\n'
        res += '\t}\n'
        res += '\tNSLog(@"sum：%d",sum);\n'
    elif i == 15:
        res += '\tint count = 0;\n'
        res += '\tfor (int i=1; i<5; i++) {\n'
        res += '\t\tfor (int j=1; j<5; j++) {\n'
        res += '\t\t\tfor (int k=1; k<5; k++) {\n'
        res += '\t\t\t\tif (i != j && j != k && i != k) {\n'
        res += '\t\t\t\t\tcount++;\n'
        res += '\t\t\t\t\tNSLog(@"k：%d",i*100+j*10+k);\n'
        res += '\t\t\t\t}\n'
        res += '\t\t\t}\n'
        res += '\t\t}\n'
        res += '\t}\n'
        res += '\tNSLog(@"count：%d",count);\n'
    elif i == 16:
        res += '\tint x = ' + str(random.randint(1, 300)) + ';\n'
        res += '\tint y = ' + str(random.randint(1, 500)) + ';\n'
        res += '\tint z = ' + str(random.randint(1, 1000)) + ';\n'
        res += '\tint t = 0;\n'
        res += '\tif (x > y) {\n'
        res += '\t\tt = x;\n'
        res += '\t\tx = y;\n'
        res += '\t\ty = t;\n'
        res += '\t}\n'
        res += '\tif (y > z) {\n'
        res += '\t\tt = z;\n'
        res += '\t\tz = y;\n'
        res += '\t\ty = t;\n'
        res += '\t}\n'
        res += '\tif (x > y) {\n'
        res += '\t\tt = x;\n'
        res += '\t\tx = y;\n'
        res += '\t\ty = t;\n'
        res += '\t}\n'
        res += '\tNSLog(@"x,y,z：%d,%d,%d",x,y,z);\n'
    elif i == 17:
        res += '\tint n = ' + str(random.randint(1, 300)) + ';\n'
        res += '\tdouble sum = 0;\n'
        res += '\tif (n%2 == 0) {\n'
        res += '\t\tfor (int i=2; i<=n; i+=2) {\n'
        res += '\t\t\tsum += (double)1/i;\n'
        res += '\t\t}\n'
        res += '\t} else {\n'
        res += '\t\tfor (int i=1; i<=n; i+=2) {\n'
        res += '\t\t\tsum += (double)1/i;\n'
        res += '\t\t}\n'
        res += '\t}\n'
        res += '\tNSLog(@"sum：%f",sum);\n'
    elif i == 18:
        res += '\tint i,m,j=0,k,count;\n'
        res += '\tfor(i=4;i<10000;i+=4) {\n'
        res += '\t\tcount=0;\n'
        res += '\t\tm=i;\n'
        res += '\t\tfor(k=0;k<5;k++){\n'
        res += '\t\t\tj=i/4*5+1;\n'
        res += '\t\t\ti=j;\n'
        res += '\t\t\tif(j%4==0)\n'
        res += '\t\t\t\tcount++;\n'
        res += '\t\t\telse break;\n'
        res += '\t\t}\n'
        res += '\t\ti=m;\n'
        res += '\t\tif(count==4) {\n'
        res += '\t\t\tNSLog(@"桃子：%d",j);\n'
        res += '\t\t\tbreak;\n'
        res += '\t\t}\n'
        res += '\t}\n'
    elif i == 19:
        res += '\tint H = 7, W = 7;\n'
        res += '\tfor(int i=0; i<(H+1) / 2; i++) {\n'
        res += '\t\tfor(int j=0; j<W/2-i; j++) {\n'
        res += '\t\t\tprintf(" ");\n'
        res += '\t\t}\n'
        res += '\t\tfor(int k=1; k<(i+1)*2; k++) {\n'
        res += '\t\t\tprintf("*");\n'
        res += '\t\t}\n'
        res += '\t\tprintf("\\n");\n'
        res += '\t}\n'
        res += '\tfor(int i=1; i<=H/2; i++) {\n'
        res += '\t\tfor(int j=1; j<=i; j++) {\n'
        res += '\t\t\tprintf(" ");\n'
        res += '\t\t}\n'
        res += '\t\tfor(int k=1; k<=W-2*i; k++) {\n'
        res += '\t\t\tprintf("*");\n'
        res += '\t\t}\n'
        res += '\t\tprintf("\\n");\n'
        res += '\t}\n'
    else:
        res += '\tfor (int i=1; i<10; i++) {\n'
        res += '\t\tfor (int j=1; j<=i; j++) {\n'
        res += '\t\t\tNSLog(@"%d*%d=%d",i,j,i*j);\n'
        res += '\t\t}\n'
        res += '\t}\n'
    return res
