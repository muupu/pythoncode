def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #生成器c调用send(None)相当于执行next()，consumer()便执行到yield表达式。因此这里相当于启动生成器。
    n = 0
    while n < 5:
        n = n + 1 #生产了一个东西
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 生成器c调用send(n)设置yield表达式的值为n，然后执行到下一个yield表达式，获得r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer() #创建了一个生成器
produce(c)