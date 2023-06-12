import multiprocessing
import time
import numpy as np
import io
import L1, L2

z = "01111101101101010101110101011000010011111111011011001000000111101110101100000000011101101001110100000010100000010001101010000010010000011110011001111100001000011110111010000011110110100010110100001001010001111001001011111000010000110111011011010101100100000001000001111110000101101111110110011101100011001010100101101101111000110110001100001110111110101011110110000011000111001010000101010100111101000101100111111001100011010110111101111111001010110010101001010111001110110000111001010111011110101110111011011011011110000010110011111110101110001111010110010101111100000101110010011111001001010110010010011111011000110101100001100111101111111011110010000100001000011000000100000000101110111101111010010000011101010101110010011101110111111100110010011111011010001111000010110010111001110000100100011010011000110011100000000100010010001000101100110011001001000000001101011111000110110100101100011010101010110111110010000000111000100010001001010001010110010000111111010110011110000010111110101010110111101011100010011010100101000010011111001011011110100001011010000111010110111011010101110111100101101111101100111100000010000001101001101101000010110000100111110111001000101100011000010110100010000100000101011011010001011001110111100011100000001100001111100110001101010100010001001000100100010100011100100011111100001111111100011111000110110011001111101011101110100101000101101011000110011011001110001000011111001111010110000010110111000111010101001100011101011111100100111010011000000101110011110001100100010100110001100000111111111001111001110001100011101110111110111011010011101110000110110100000000000010010101001101110011010010000101111110010111000100110110110100100110010010011100010000101010001110110101001101100000010101010101110001100110000110110011000010110110111110010110010000101011010000111111000001111011000101000110000110000110000100011100000111001100100001010110110111010100101111000101110010111001101001011110111011011011111111010111011001110010000001000000110010010001001000110011001110001100010000001110010110111010011100111110001010"

t_b27 = 5.662698
n3 = 27

if __name__ == '__main__':

    timer = time.time()

    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=L1.calc_L1, args=(z, queue))
    p1.start()

    p2 = multiprocessing.Process(target=L2.calc_L2, args=(z, queue))
    p2.start()

    print(f"size:{queue.qsize()}")

    p1.join()
    p2.join()

    print("hi!")
    print(f"size:{queue.qsize()}")

    print(time.time() - timer)