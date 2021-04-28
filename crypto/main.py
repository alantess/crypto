from env import cryptoEnv

import numpy as np
if __name__ == '__main__':
    dataset = "/media/alan/seagate/Downloads/Binance_LTCUSDT_minute.csv"
    env = cryptoEnv(dataset, 1000)
    s = env.reset()
    print(env.price)
    s_, r, d, _ = env.step(11)
    print(s_)
    print(r)
