# 练习1华氏转摄氏 C = (F - 32) / 1.8
# f = float(input('please input f\n'))
# c = (f - 32) / 1.8
# print('输入的华氏度为： %.1f\n对应的摄氏度是： %.1f'%(f, c))
# print(f'输入的华氏度为：{f:.1f}\n对应的摄氏度是：{c:.1f}')


# 练习2输入圆的半径输出圆的周长和面积

# r = float(input('please input r\n'))
# c = 3.1416 * r
# s = 3.1316 * r * r
# print(f'半径是：{r:.1f}\n周长是：{c:.1f}\n面积是：{s:.1f}')

# 练习3输入年份是不是闰年

year = int(input('请输入年份\n'))

if year % 4 == 0 and year % 100 != 0 or \
        year % 400 == 0:
    print('是闰年')
else:
    print('不是闰年')
