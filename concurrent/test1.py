#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
线程测试
'''

import time
from threading import Thread
import queue

class Consumer(Thread):
	def __init__(self , queue):
		Thread.__init__(self)
		self._queue = queue

	def run(self):
		while True:
			# 从队列里取数据
			msg = self._queue.get()
			# 如果数据为quit，跳出循环
			if(isinstance(msg , str) and msg=='quit'):
				break

			print("I am a thread , and I received %s" % msg)
		print("end")

def Producer():
	q = queue.Queue()

	# 实例化一个线程，并启动线程
	worker = Consumer(q)
	worker.start()

	start_time = time.time()

	# 连着五秒，往队列里塞一条数据，用time.sleep阻塞一秒
	while time.time()-start_time < 5:
		q.put("something at %s" % time.time())
		time.sleep(1)

	q.put('quit')
	worker.join()

if __name__ == '__main__':
	Producer()