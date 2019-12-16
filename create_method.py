#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import trans_type
from random_word import random_one


class methodObject:
    """方法的类"""
    def __init__(self, methodName, needRetuen, returnType, params, fName):
        self.methodName = methodName
        self.needRetuen = needRetuen
        self.returnType = returnType
        self.params = params
        self.fName = fName

class paramObject:
    def __init__(self, cont, param, paramOutType, paramInType, hadNum):
        self.cont = cont
        self.param = param
        self.paramOutType = paramOutType #输出的类型
        self.paramInType = paramInType #输入的类型
        self.hadNum = hadNum

    def cont(self, index):
        #在这里替换占位符
        print index

class paramsToParam:
    def __init__(self, cont, param, paramOutType):
        self.cont = cont
        self.paramOutType = paramOutType #输出的类型
        self.param = param

classArray = ['NSString*','int', 'long']

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

def handle_methodcpp(returnType):
    res = ''
    i = random.randint(1, 12)
    if i == 1:
        res += '\tint firstNumber = ' + str(random.randint(1, 300)) + ', secondNumber = ' + str(random.randint(1, 300)) + ', sumOfTwoNumbers;\n'
        res += '\tsumOfTwoNumbers = firstNumber + secondNumber;\n'
        res += '\tcout << firstNumber << " + " <<  secondNumber << " = " << sumOfTwoNumbers;\n'
    elif i == 2:
        res += '\tint n1 = ' + str(random.randint(1, 300)) + ', n2 = ' + str(random.randint(1, 300)) + ', max;\n'
        res += '\t// 获取最大的数\n'
        res += '\tmax = (n1 > n2) ? n1 : n2;\n'
        res += '\tdo {\n'
        res += '\t\tif (max % n1 == 0 && max % n2 == 0) {\n'
        res += '\t\t\tcout << "LCM = " << max;\n'
        res += '\t\t\tbreak;\n'
        res += '\t\t}\n'
        res += '\t\telse\n'
        res += '\t\t\t++max;\n'
        res += '\t} while (true);\n'
    elif i == 3:
        res += '\tint year = ' + str(random.randint(1979, 2030)) + ';\n'
        res += '\tif (year % 4 == 0) {\n'
        res += '\t\tif (year % 100 == 0) {\n'
        res += '\t\t\t//这里如果被 400 整数是闰年\n'
        res += '\t\t\tif (year % 400 == 0)\n'
        res += '\t\t\t\tcout << year << " 是闰年";\n'
        res += '\t\t\telse\n'
        res += '\t\t\t\tcout << year << " 不是闰年";\n'
        res += '\t\t}\n'
        res += '\t\telse\n'
        res += '\t\t\tcout << year << " 是闰年";\n'
        res += '\t}\n'
        res += '\telse\n'
        res += '\t\tcout << year << " 不是闰年";\n'
    elif i == 4:
        res += '\tint n1 = ' + str(random.randint(1, 300)) + ', n2 = ' + str(random.randint(1, 300)) + ';\n'
        res += '\twhile(n1 != n2) {\n'
        res += '\t\tif(n1 > n2)\n'
        res += '\t\t\tn1 -= n2;\n'
        res += '\t\telse\n'
        res += '\t\t\tn2 -= n1;\n'
        res += '\t}\n'
        res += '\tcout << "HCF = " << n1;\n'
    elif i == 5:
        res += '\tint rows = ' + str(random.randint(6, 30)) + ';\n'
        res += '\tfor(int i = 1; i <= rows; ++i) {\n'
        res += '\t\tfor(int j = 1; j <= i; ++j) {\n'
        res += '\t\t\tcout << "* ";\n'
        res += '\t\t}\n'
        res += '\t\tcout << "\\n";\n'
        res += '\t}\n'
    elif i == 6:
        res += '\tfloat a = ' + str(random.randint(1, 300)) + ', b = ' + str(random.randint(1, 300)) + ', c = ' + str(random.randint(1, 300)) + ';\n'
        res += '\tfloat x1, x2, discriminant, realPart, imaginaryPart;\n'
        res += '\tdiscriminant = b*b - 4*a*c;\n'
        res += '\tif (discriminant > 0) {\n'
        res += '\t\tx1 = (-b + sqrt(discriminant)) / (2*a);\n'
        res += '\t\tx2 = (-b - sqrt(discriminant)) / (2*a);\n'
        res += '\t\tcout << "Roots are real and different." << endl;\n'
        res += '\t\tcout << "x1 = " << x1 << endl;\n'
        res += '\t\tcout << "x2 = " << x2 << endl;\n'
        res += '\t}\n'
        res += '\telse if (discriminant == 0) {\n'
        res += '\t\tcout << "实根相同：" << endl;\n'
        res += '\t\tx1 = (-b + sqrt(discriminant)) / (2*a);\n'
        res += '\t\tcout << "x1 = x2 =" << x1 << endl;\n'
        res += '\t}\n'
        res += '\telse {\n'
        res += '\t\trealPart = -b/(2*a);\n'
        res += '\t\timaginaryPart =sqrt(-discriminant)/(2*a);\n'
        res += '\t\tcout << "实根不同："  << endl;\n'
        res += '\t\tcout << "x1 = " << realPart << "+" << imaginaryPart << "i" << endl;\n'
        res += '\t\tcout << "x2 = " << realPart << "-" << imaginaryPart << "i" << endl;\n'
        res += '\t}\n'
    elif i == 7:
        res += '\tint iMale = ' + str(random.randint(6, 30)) + ';\n'
        res += '\tint iFemale = ' + str(random.randint(6, 30)) + ';\n'
        res += '\tint iTotalMoney = ' + str(random.randint(1000, 30000)) + ';\n'
        res += '\tfloat fMaleTicketMoney = ' + str(random.randint(30, 100)) + ';\n'
        res += '\tfloat fFemaleTicketMoney = fMaleTicketMoney/2;\n'
        res += '\tfloat fRemainMoney = 0;\n'
        res += '\tint iMaleRemain = 0;\n'
        res += '\tfRemainMoney = iTotalMoney - (fMaleTicketMoney * iMale + fFemaleTicketMoney * iFemale);\n'
        res += '\tiMaleRemain = (int)(fRemainMoney/fMaleTicketMoney);\n'
        res += '\tcout << "最后剩的钱是：" << fRemainMoney << endl;\n'
        res += '\tcout << "剩的钱够几位男士看电影" << iMaleRemain << endl;\n'
    elif i == 8:
        res += '\tint shu = ' + str(random.randint(6, 300)) + ';\n'
        res += '\tint *zhen_yinzi = new int[shu];//不知道真因子有多少个，所以用指针指向\n'
        res += '\tint index = 0;//个数索引变量，初始化为0\n'
        res += '\tint sum = 0;//所有真因子的总和\n'
        res += '\tzhen_yinzi[0] = 1;//所有数字都有一个真因子为1\n'
        res += '\tfor (int i = 2; i < shu; i++) {//循环找所有因子\n'
        res += '\t\tif(shu % i == 0) {//表示该因子为真因子\n'
        res += '\t\t\tindex ++;\n'
        res += '\t\t\tzhen_yinzi[index] = i;\n'
        res += '\t\t}\n'
        res += '\t}\n'
        res += '\tfor(int j = 0; j <= index; j++){//将所有真因子加和\n'
        res += '\t\tsum += zhen_yinzi[j];\n'
        res += '\t}\n'
        res += '\tdelete[] zhen_yinzi;//释放内存\n'
        res += '\tzhen_yinzi = NULL;\n'
        res += '\tif(sum == shu)//如果真因子之和等于数字本身，即为完数\n'
        res += '\t\tcout<<"数字"<<shu<<"是完数"<<endl;\n'
        res += '\telse\n'
        res += '\t\tcout<<"数字"<<shu<<"不是完数"<<endl;\n'
    elif i == 9:
        res += '\tint migong[5][5]={{0,0,1,1,1},{1,0,0,1,1},{1,1,0,1,1},{1,1,0,0,1},{1,1,1,0,2}};//迷宫\n'
        res += '\tint row,column;//行列\n'
        res += '\tint path_row[25];//通行路径的行\n'
        res += '\tint path_column[25];//通行路径的列\n'
        res += '\tfor(int i=0;i<25;i++)//初始化\n'
        res += '\t\tpath_row[i]=path_column[i]=0;\n'
        res += '\trow=0;\n'
        res += '\tcolumn=0;\n'
        res += '\tint count=0;//次数\n'
        res += '\tdo//按行循环，先处理，后判断\n'
        res += '\t{\n'
        res += '\t\tcolumn = 0;\n'
        res += '\t\tdo//按列循环，先处理，后判断\n'
        res += '\t\t{\n'
        res += '\t\t\tswitch(migong[row][column])\n'
        res += '\t\t\t{\n'
        res += '\t\t\t\tcase 0://可以通行\n'
        res += '\t\t\t\t\tpath_row[count]=row;\n'
        res += '\t\t\t\t\tpath_column[count]=column;\n'
        res += '\t\t\t\t\tcout<<"加油，快要找到出口了"<<endl;\n'
        res += '\t\t\t\t\tcount++;\n'
        res += '\t\t\t\t\tbreak;\n'
        res += '\t\t\t\tcase 1:\n'
        res += '\t\t\t\t\tcout<<"不可通行"<<endl;\n'
        res += '\t\t\t\t\tbreak;\n'
        res += '\t\t\t\tcase 2:\n'
        res += '\t\t\t\t\tpath_row[count]=row;\n'
        res += '\t\t\t\t\tpath_column[count]=column;\n'
        res += '\t\t\t\t\tcout<<"到达出口"<<endl;\n'
        res += '\t\t\t\t\tcount++;\n'
        res += '\t\t\t\t\tbreak;\n'
        res += '\t\t\t}\n'
        res += '\t\t\tcolumn += 1;\n'
        res += '\t\t}while(column<5);\n'
        res += '\t\trow += 1;\n'
        res += '\t}while(row<5);\n'
        res += '\tcout<<"到达出口的路径为:"<<endl;\n'
        res += '\tfor(int j=0;j<count;j++)//输出出口路径\n'
        res += '\t{\n'
        res += '\t\tcout<<"("<<path_row[j]<<","<<path_column[j]<<")->";\n'
        res += '\t}\n'
        res += '\tcout<<endl;\n'
    elif i == 10:
        res += '\tint i,result;\n'
        res += '\tsrand((int)time(0));//利用系统时间产生随机序列的种子值\n'
        res += '\tint count[6]={0};//1-6的统计个数\n'
        res += '\tfor(i=0;i<10000;i++)\n'
        res += '\t{\n'
        res += '\t\tresult=1+(int)(6.0*rand()/(RAND_MAX+1.0));//设置出现1-6之间的整数\n'
        res += '\t\tswitch(result)\n'
        res += '\t\t{\n'
        res += '\t\t\tcase 1:\n'
        res += '\t\t\t\tcount[0]++;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t\tcase 2:\n'
        res += '\t\t\t\tcount[1]++;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t\tcase 3:\n'
        res += '\t\t\t\tcount[2]++;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t\tcase 4:\n'
        res += '\t\t\t\tcount[3]++;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t\tcase 5:\n'
        res += '\t\t\t\tcount[4]++;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t\tcase 6:\n'
        res += '\t\t\t\tcount[5]++;\n'
        res += '\t\t\t\tbreak;\n'
        res += '\t\t}\n'
        res += '\t}\n'
        res += '\tcout<<"1-6点的出现概率依次为：";\n'
        res += '\tfor(int k =0;k<6;k++)//打印每点出现的概率\n'
        res += '\t\tcout<<count[k]/10000.0<<",";\n'
        res += '\tcout<<endl;\n'
    elif i == 11:
        res += '\tint src[10] = {' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + '};//一维数组中包含10个整数\n'
        res += '\t//从大到小排序\n'
        res += '\tfor(int i = 0; i < 10; i++)\n'
        res += '\t{\n'
        res += '\t\tfor(int j = i+1; j < 10; j++)\n'
        res += '\t\t{\n'
        res += '\t\t\tif(src[i]<src[j]){//如果前一个元素小于后一个元素\n'
        res += '\t\t\t\tint temp;//临时变量\n'
        res += '\t\t\t\ttemp = src[i];\n'
        res += '\t\t\t\tsrc[i] = src[j];//大的元素到前一个位置\n'
        res += '\t\t\t\tsrc[j] = temp;//小的元素到后一个位置\n'
        res += '\t\t\t}\n'
        res += '\t\t}\n'
        res += '\t}\n'
        res += '\tfor(int k = 0; k < 10; k++)\n'
        res += '\t\tcout<<src[k]<<endl;\n'
    else:
        res += '\tint all[30];//所有人编号\n'
        res += '\tint yijiao[15];//异教徒编号\n'
        res += '\tint jidu[15];//基督徒编号\n'
        res += '\tint i,k,yijiao_count,yijiao_index,jidu_count;\n'
        res += '\tfor (i=0;i<30;i++)\n'
        res += '\t\tall[i]=i+1;  //每人编号\n'
        res += '\ti=0;  //i为每次循环时计数变量\n'
        res += '\tk=0;  //k为按1，2...9报数时计数变量\n'
        res += '\tyijiao_count=0;  //投入海人数\n'
        res += '\tyijiao_index=0;  //存被投入海者数组的下标\n'
        res += '\tjidu_count=0;  //存在船上人编号数组的下标\n'
        res += '\twhile (yijiao_count<15)//有15个投入海\n'
        res += '\t{\n'
        res += '\t\tif (all[i]!=0)//没被丢入海\n'
        res += '\t\t\tk++;\n'
        res += '\t\tif (k==9)\n'
        res += '\t\t{\n'
        res += '\t\t\tyijiao[yijiao_index]=all[i];\n'
        res += '\t\t\tyijiao_index++;\n'
        res += '\t\t\tall[i]=0;//被丢入海标志\n'
        res += '\t\t\tk=0;\n'
        res += '\t\t\tyijiao_count++;\n'
        res += '\t\t}\n'
        res += '\t\ti++;\n'
        res += '\t\tif (i==30)//到边界\n'
        res += '\t\t\ti=0;\n'
        res += '\t}\n'
        res += '\tfor(i=0;i<30;i++)\n'
        res += '\t{\n'
        res += '\t\tif (all[i]!=0) {\n'
        res += '\t\t\tjidu[jidu_count]=all[i];\n'
        res += '\t\t\tjidu_count++;\n'
        res += '\t\t}\n'
        res += '\t}\n'
        res += '\tcout<<"被投入海的序号为："<<endl;\n'
        res += '\tfor(i=0;i<15;i++)\n'
        res += '\t{\n'
        res += '\t\tcout<<yijiao[i]<<"  ";\n'
        res += '\t}\n'
        res += '\tcout<<endl<<"留在船上的序号为："<<endl;\n'
        res += '\tfor(i=0;i<15;i++)\n'
        res += '\t\tcout<<jidu[i]<<"  ";\n'
        res += '\tcout<<endl;\n'
    if returnType == 'string':
        res += '\tstring same = "ok了";\n'
        res += '\treturn same;\n'
    elif returnType == 'int':
        res += '\tint same = ' + str(random.randint(0, 100)) + ';\n'
        res += '\treturn same;\n'
    elif returnType == 'bool':
        u = random.randint(0, 1)
        if u == 0:
            res += '\tbool same = false;\n'
        else:
            res += '\tbool same = true;\n'
        res += '\treturn same;\n'
    elif returnType == 'long':
        res += '\tlong same = ' + str(random.randint(0, 100)) + ';\n'
        res += '\treturn same;\n'
    return res


def handle_methodcpp2(returnType, params):
    #对params多参数转成单参数
    i = 0 #这个是参数递增
    paramsToParam = trans_params(params, i) #转换为单一参数 cc_i
    i = i + 10
    res = paramsToParam.cont
    lastType = paramsToParam.paramOutType
    param = paramsToParam.param
    upParam = paramsToParam.param
    hadNum = []
    for n in range(2):
        #代码片段
        pObject = random_code(hadNum, i, i - 10, lastType)
        #判断是否需要转换
        if pObject.paramInType != lastType:
            res += select_method(lastType, pObject.paramInType, i, param)
            i = i + 10
        i = i + 10
        res += pObject.cont
        lastType = pObject.paramOutType
        param = pObject.param
        hadNum = pObject.hadNum

    if returnType != '':
        if returnType != lastType:
            res += select_method(lastType, returnType, i, param)
            res += 'return cc_' + str(i) + ';\n'
        else:
            res += 'return cc_' + str(i - 10) + ';\n'
    return res


def trans_params(params, index):
    start = index
    index = index + 1
    res = ''
    sum = ''
    for param in params:
        if param == 'string':
            res += 'int cc_' + str(index) + ' = param' + str(index - 1) + '.length();\n'
            sum += 'cc_' + str(index) + random.choice(marks)
            index = index + 1
        elif param == 'int':
            res += 'int cc_' + str(index) + ' = param' + str(index - 1) + ';\n'
            sum += 'cc_' + str(index) + random.choice(marks)
            index = index + 1
        elif param == 'long':
            res += 'long cc_' + str(index) + ' = param' + str(index - 1) + ' / ' + str(random.randint(1000, 3000)) + ';\n'
            sum += 'cc_' + str(index) + random.choice(marks)
            index = index + 1
        elif param == 'bool':
            res += 'int cc_' + str(index) + ' = param' + str(index - 1) + '?1:0;\n'
            sum += 'cc_' + str(index) + random.choice(marks)
            index = index + 1
    sum = 'int cc_' + str(start) + '=' + sum + '1;\n'
    res += sum
    pa = 'cc_' + str(start)
    return paramsToParam(res, pa, 'int')

#随机代码片段
def random_code(hadNum, index, paramIndex, lastType):
    end = 39
    j = random.randint(1, end)
    while(j in hadNum):
        j = random.randint(1, end)
    hadNum.append(j)
    paramInType = ''
    paramOutType = ''
    param = ''
    upParam = ''
    cont = ''
    if j == 1:
        paramInType = 'int'
        paramOutType = 'string'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'string cc_' + str(index) + ' = to_string(cc_' + str(index + 1) + random.choice(marks) + str(random.randint(1, 30)) + ');\n'
        param = 'cc_' + str(index)
    elif j == 2:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = cc_' + str(index + 1) + ' % 2 == 0 ? true : false;\n'
        param = 'cc_' + str(index)
    elif j == 3:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index + 2) + ' = ' + str(random.randint(6, 300)) + ';\n'
        cont += 'int cc_' + str(index) + ' = (cc_' + str(index + 1) + ' > cc_' + str(index + 2) + ')?cc_' + str(index + 1) + ' : cc_' + str(index + 2) + ';\n'
        cont += 'do{\n'
        cont += 'if (cc_' + str(index) + ' % cc_' + str(index + 1) + ' == 0 && cc_' + str(index) + ' % cc_' + str(index + 2) + ' == 0) {\n'
        cont += 'break;\n'
        cont += '}\n'
        cont += 'else\n'
        cont += '++cc_' + str(index) + ';\n'
        cont += '} while (true);\n'
        param = 'cc_' + str(index)
    elif j == 4:
        paramInType = 'string'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'char cc_' + str(index + 2) + ' = cc_' + str(index + 1) + '[0];\n'
        cont += 'int cc_' + str(index + 3) + ',cc_' + str(index + 4) + ';\n'
        cont += 'bool cc_' + str(index) + ';'
        cont += "cc_" + str(index + 3) + " = (cc_" + str(index + 2) + " == 'a' || cc_" + str(index + 2) + " == 'e' || cc_" + str(index + 2) + " == 'i' || cc_" + str(index + 2) + " == 'o' || cc_" + str(index + 2) + " == 'u');\n"
        cont += "cc_" + str(index + 4) + " = (cc_" + str(index + 2) + " == 'A' || cc_" + str(index + 2) + " == 'E' || cc_" + str(index + 2) + " == 'I' || cc_" + str(index + 2) + " == 'O' || cc_" + str(index + 2) + " == 'U');\n"
        cont += 'if (cc_' + str(index + 3) + ' || cc_' + str(index + 4) + ')\n'
        cont += 'cc_' + str(index) + ' = true;\n'
        cont += 'else\n'
        cont += 'cc_' + str(index) + ' = false;\n'
        param = 'cc_' + str(index)
    elif j == 5:
        paramInType = 'int'
        paramOutType = 'string'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'string cc_' + str(index) + ' = "";\n'
        cont += 'cc_' + str(index) + ' = cc_' + str(index + 1) + ' >= 90?"A" : (cc_' + str(index + 1) + ' >= 60)?"B":"C";\n'
        param = 'cc_' + str(index)
    elif j == 6:
        paramInType = 'int'
        paramOutType = 'string'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'string cc_' + str(index) + ' = "";\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getMapValue(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 7:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'string cc_' + str(index + 2) + ' = "' + str(random.randint(3, 300)) + '";\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addMapValue(cc_' + str(index + 1) + ', const_cast<char*>(cc_' + str(index + 2) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 8:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->deleMapValue(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 9:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getMapSize(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 10:
        paramInType = 'bool'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'Singleton::Instance()->cleanMap(cc_' + str(index) + ');\n'
        param = 'cc_' + str(index)
    elif j == 11:
        paramInType = 'bool'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'Singleton::Instance()->cleanMapInt(cc_' + str(index) + ');\n'
        param = 'cc_' + str(index)
    elif j == 12:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getMapIntSize(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 13:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addMapIntValue(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 14:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->deleMapIntValue(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 15:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'int cc_' + str(index + 2) + ' = ' + str(random.randint(3, 300)) + ';\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addMapIntValue(cc_' + str(index + 1) + ', cc_' + str(index + 2) + ');\n'
        param = 'cc_' + str(index)
    elif j == 16:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getMapIntValue(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)

    elif j == 17:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 18:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 19:
        paramInType = 'bool'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getSetIntSize(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 20:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->deleteSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 21:
        paramInType = 'bool'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->cleanSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 22:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->findSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 23:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->countSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 24:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->lowerSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 25:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->upperSetInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)

    elif j == 26:
        paramInType = 'string'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 27:
        paramInType = 'string'
        paramOutType = 'string'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'string cc_' + str(index) + ' = "";\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 28:
        paramInType = 'bool'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getSetStringSize(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 29:
        paramInType = 'string'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->deleteSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 30:
        paramInType = 'bool'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->cleanSetString(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 31:
        paramInType = 'string'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->findSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 32:
        paramInType = 'string'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->countSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 33:
        paramInType = 'string'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->lowerSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 34:
        paramInType = 'string'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->upperSetString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)

    elif j == 35:
        paramInType = 'string'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addStackString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 36:
        paramInType = 'bool'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getStackStringSize(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 37:
        paramInType = 'string'
        paramOutType = 'string'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'string cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'string cc_' + str(index) + ' = "";\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->topStackString(const_cast<char*>(cc_' + str(index + 1) + '.data()));\n'
        param = 'cc_' + str(index)
    elif j == 38:
        paramInType = 'bool'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->popStackString(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 39:
        paramInType = 'bool'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'bool cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->popStackInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 40:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->topStackInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 41:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getStackIntSize(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 42:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->addStackInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 43:
        paramInType = 'int'
        paramOutType = 'bool'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'bool cc_' + str(index) + ' = false;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->setInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 44:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->getInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 45:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->sumInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 46:
        paramInType = 'long'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'long cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->multInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 47:
        paramInType = 'long'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->divisionInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    elif j == 48:
        paramInType = 'long'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'cc_' + str(index) + ' = Singleton::Instance()->modlInt(cc_' + str(index + 1) + ');\n'
        param = 'cc_' + str(index)
    else:
        paramInType = 'int'
        paramOutType = 'int'
        if paramInType != lastType:
            index = index + 10
            paramIndex = paramIndex + 10
        cont += 'int cc_' + str(index + 1) + ' = cc_' + str(paramIndex) + ';\n'
        cont += 'int cc_' + str(index + 2) + '[10] = {' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + ',' + str(random.randint(6, 300)) + '};//一维数组中包含10个整数\n'
        cont += 'int cc_' + str(index) + ' = 0;\n'
        cont += 'for(int i = 0; i < 10; i++){\n'
        cont += 'if (cc_' + str(index + 2) + '[i] < cc_' + str(index + 1) + ')\n'
        cont += 'cc_' + str(index) + '++;\n'
        cont += '}\n'
        param = 'cc_' + str(index)
    return paramObject(cont, param, paramOutType, paramInType, hadNum)
    

def select_method(inType, outType, index, param):
    if inType == 'string':
        if outType == 'int':
            return trans_type.transCpp_String_Int(index, param)
        elif outType == 'long':
            return trans_type.transCpp_String_Long(index, param)
        elif outType == 'bool':
            return trans_type.transCpp_String_Bool(index, param)
    elif inType == 'int':
        if outType == 'string':
            return trans_type.transCpp_Int_String(index, param)
        elif outType == 'long':
            return trans_type.transCpp_Int_Long(index, param)
        elif outType == 'bool':
            return trans_type.transCpp_Int_Bool(index, param)
    elif inType == 'long':
        if outType == 'int':
            return trans_type.transCpp_Long_Int(index, param)
        elif outType == 'string':
            return trans_type.transCpp_Long_String(index, param)
        elif outType == 'bool':
            return trans_type.transCpp_Long_Bool(index, param)
    elif inType == 'bool':
        if outType == 'int':
            return trans_type.transCpp_Bool_Int(index, param)
        elif outType == 'long':
            return trans_type.transCpp_Bool_Long(index, param)
        elif outType == 'string':
            return trans_type.transCpp_Bool_String(index, param)
    return ''