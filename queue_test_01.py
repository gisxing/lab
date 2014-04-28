#-*- coding: utf-8 -*-
import Queue,threading,time,random

'''
这种情况下，快速消费者在get时需要阻塞（否则返回了这线程就结束了～）因此对于停止整个程序，使用的是None标记，让子线程遇到None便返回结束。

因为消费速度大于产生速度，因此先运行子线程等待队列加入新的元素，然后再慢速地添加任务。

注意最后put（None）三次，是因为每个线程返回都会取出一个None，都要这样做才可以使三个线程全部停止。当然有种更简单粗暴的方法，就是把子线程设置为deamon，一但生产完成，开始que.join()阻塞直至队列空就结束主线程，子线程虽然在阻塞等待队列也会因为deamon属性而被强制关闭。。。。
''' 

class consumer(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self)
        self.daemon = False
        self.queue = que
    def run(self):
        while True:
            item = self.queue.get()
            if item == None:
                break
            #processing the item
            print self.name,item
            self.queue.task_done()
        self.queue.task_done()
        return
que = Queue.Queue()

consumers = [consumer(que) for x in range(3)]
for c in consumers:
    c.start()

for x in range(10):
    item = random.random() * 1
    time.sleep(item)
    # 慢速生产者
    que.put(item, True, None)


que.put(None)
que.put(None)
que.put(None)
que.join()
