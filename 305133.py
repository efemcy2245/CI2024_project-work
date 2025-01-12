import numpy as np


def f1(x):
    return np.sin(x[0])
    # (sin x0)

def f2(x):
    return np.divide(np.divide(x[0], x[1]), x[1])
    # ((x0 divide x1) divide x1)

def f3(x):
    return np.power(1.4671024929992713,np.subtract(4.65966493119525, np.add(x[0], x[1])))
    # (1.4671024929992713 power (4.65966493119525 subtract (x0 add x1)))

def f4(x):
    return np.multiply( np.cos(np.divide(x[1], 2.0567915909182988)), 1.5513136700495078)
    # ((cos (x1 divide 2.0567915909182988)) multiply 1.5513136700495078)

def f5(x):
    return np.power(np.cos(np.cos(x[1])), np.divide(np.cos(0.47558864290304415), np.subtract(x[1], x[1])))
    # ((cos (cos x1)) power ((cos 0.47558864290304415) divide (x1 subtract x1)))

def f6(x):
    return np.add(x[1], np.add(np.sin(np.divide(-4.311029808626657, np.add(x[1], x[0]))), x[1]))
    # (x1 add ((sin (-4.311029808626657 divide (x1 add x0))) add x1))

def f7(x):
    return np.add(np.divide(np.multiply(x[1], np.multiply(x[1], 1.6272853311901954)), np.cos(0.9723828327625101)), np.multiply(x[1], np.subtract(np.add(np.add(x[1], x[0]), x[0]), -1.5039106323170328)))
    # (((x1 multiply (x1 multiply 1.6272853311901954)) divide (cos 0.9723828327625101)) add (x1 multiply (((x1 add x0) add x0) subtract -1.5039106323170328)))

def f8(x):
    return np.multiply(np.multiply(x[4], x[4]), np.add(x[1], x[4]))
    # ((x5 multiply x5) multiply (x1 add x5))