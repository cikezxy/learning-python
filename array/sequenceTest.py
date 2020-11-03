import array

# 列表推导
symbols = '$¢£¥€¤'

codes = []
codes = [ord(symbol) for symbol in symbols]
print(codes)
codes = [ord(symbol) for symbol in symbols if ord(symbol) < 127]
print(codes)

#笛卡尔积
colors = ['white','black']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors
            for size in sizes]
print(tshirts)

# 生成器表达式
t = tuple(ord(symbol) for symbol in symbols)
print(t) #(36, 162, 163, 165, 8364, 164)

a = array.array('I',(ord(symbol) for symbol in symbols))
print(a) #array('I', [36, 162, 163, 165, 8364, 164])
