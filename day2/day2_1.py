# 英寸厘米互换
# value = float(input('请输入长度： '))
# unit = input('请输入单位： ')
# if unit == 'in' or unit == '英寸':
#     print('%.1f英寸 = %.1f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%.1f厘米 = %.1f英寸' % (value, value / 2.54))
# else:
#     print('请输入正确的数据')

# 百分制转化成等级制
"""
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
"""
# score = float(input('请输入分数： '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# elif score > 0:
#     grade = 'E'
# else:
#     print('请输入正确的数据')
#
# print('您的分数是： %.1f\n您的等级是: % s' % (score, grade))

# 练习3：输入三条边长，如果能构成三角形就计算周长和面积。

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2  # 海伦公式
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('\n三角形的周长是： %.1f\n三角形的面积是： %.1f' % (2 * p, area))
else:
    print('\n不是三角形')
