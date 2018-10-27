# -*- coding: utf-8 -*-

# import asyncio
#
# async def TestAsync(x):
#     print('start %s' % x)
#     # print(x)
#     await asyncio.sleep(10)
#     print('end %s' % x)
#
# if __name__ == '__main__':
#
#     task1 = TestAsync(1)
#     task2 = TestAsync(2)
#     task3 = TestAsync(3)
#
#     tasks = [
#         asyncio.ensure_future(task1),
#         asyncio.ensure_future(task2),
#         asyncio.ensure_future(task3),
#     ]
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#
#     for item in tasks:
#         print(item.result())


from SSO import SSOVerifyUrl_Client

print(SSOVerifyUrl_Client.main('https://www.qq.com','adf84108d85211e89864559b0a5fbe9b'))