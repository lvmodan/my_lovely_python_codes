

import time


def cost_time(f):
    def inner(*arg,**kwarg):
        s_time = time.time()
        res = f(*arg,**kwarg)
        e_time = time.time()
        print('耗时：{}秒'.format(e_time - s_time))
        return res
    return inner

class NumUtil:
    def __init__(self):
        pass

    @cost_time
    def is_prime_number(self, start_num=0, end_num=0):
        # 质数（英文名：Primenumber）又称素数，是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
        if end_num == 0:
            end_num = start_num
        if end_num < start_num:
            raise Exception("end_num must greater than start_num")
        is_prime_number = dict()
        for n in range(start_num, end_num+1):
            is_divisible_list = list()
            if n < 2:
                is_prime_number[n] = False
                continue
            for i in range(1,n+1):
                is_divisible = n % i
                is_divisible_list.append(is_divisible)
            zero_count = is_divisible_list.count(0)
            if zero_count == 2:
                is_prime_number[n] = True
            else:
                is_prime_number[n] = False
            
        return is_prime_number
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='num to check prime num')
    parser.add_argument('-sn', '--start_num', type=int, default=0, help='num to check prime num')
    parser.add_argument('-en', '--end_num', type=int, default=0, help='num to check prime num')
    args = parser.parse_args()
    s_num = args.start_num
    e_num = args.end_num
    nu = NumUtil()
    is_prime_number = nu.is_prime_number(s_num,e_num)
    # for k,v in is_prime_number.items():
    #     if v:
    #         print(f"{k} is {v} prime number")
