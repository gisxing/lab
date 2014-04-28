#-*- coding: utf-8 -*-
import Queue,threading,time,random
# python 中 list , dict 都是非线程安全的，而 Queue是线程安全的
'''
代码的功能是产生10个随机数（0～10范围），sleep相应时间后输出数字和线程名称

这段代码里，是一个快速生产者（产生10个随机数），3个慢速消费者的情况。

在这种情况下，先让三个consumers跑起来，然后主线程用que.join()阻塞。

当三个线程发现队列都空时，各自的run函数返回，三个线程结束。同时主线程的阻塞打开，全部程序结束。
'''

class consumer(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self)
        #self.daemon = False  # 如果使用非 daemon 模式，需要在run 中判定queue.empty()来手动break
        self.daemon = True    # daemon模式 ，queue.tark_done 则自动退出
        self.queue = que
    def run(self):
        while True:
            #if self.queue.empty():
            #    break
            item = self.queue.get()
            #processing the item
            time.sleep(item)
            print self.name,item
            self.queue.task_done()
        return

que = Queue.Queue()


for x in range(10):
    que.put(random.random() * 1, True, None)

consumers = [consumer(que) for x in range(3)]
for c in consumers:
    c.start()

que.join()
