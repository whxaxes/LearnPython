#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
多线程处理web页面
'''

import time
from threading import Thread
import queue
from urllib import request

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

			res = request.urlopen(msg)
			print("visited %s" % msg)
		print("end")


def Producer():
	urls = [
		'http://www.bilibili.com',
		'http://www.python.org',
		'http://www.wanghx.cn',
		'http://appled.cc/board/price',
		'http://www.bilibili.com',
		'http://www.python.org',
		'http://www.wanghx.cn',
	]

	q = queue.Queue()
	workers = build_worker_pool(q , 4)
	start_time = time.time()

	# 输入urls
	for url in urls:
		q.put(url)
	# 输入停止指令
	for _ in workers:
		q.put("quit")
	# 运行线程
	for i,u in enumerate(urls):
		ni = i%len(workers)
		workers[ni].join()

	# for worker in workers:
	# 	worker.join()

	print("Done !!! Time taken : %s" % (time.time()-start_time))

def build_worker_pool(queue , size):
	workers = []
	for _ in range(size):
		worker = Consumer(queue)
		worker.start()
		workers.append(worker)
	return workers

if __name__ == '__main__':
	Producer()
