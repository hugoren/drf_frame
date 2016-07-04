#coding:utf-8

from multiprocessing.dummy import Pool as ThreadPool
def threads(functions,queue):

    # 创建一个工作者线程池
    pool = ThreadPool(3)
    # 在各个线程中打开url，并返回结果
    results = pool.map(functions,queue)
    # 关闭线程池，等待工作结束
    pool.close()
    pool.join()
    return results
