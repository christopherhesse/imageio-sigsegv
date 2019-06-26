# import imageio
# import concurrent.futures
# from glob import glob
# import sys
# import os


# def make_iterator(uris):
#     while True:
#         for uri in uris:
#             r = imageio.get_reader(uri=uri, format="ffmpeg")
#             yield r.get_next_data()


# def main():
#     uris = glob(os.path.join(sys.argv[1], "*/*.mp4"))
#     its = [make_iterator(uris) for _ in range(9)]
#     with concurrent.futures.ThreadPoolExecutor(max_workers=len(its)) as executor:
#         for i in range(100000):
#             print(i, len(list(executor.map(next, its))))
    
import imageio
import queue
import threading


def make_iterator(q):
    while True:
        # doesn't crash
        q.put(imageio.imread('imageio:chelsea.png'))
        # crashes
        r = imageio.get_reader(uri="imageio:cockatoo.mp4", format="ffmpeg")
        q.put(r.get_next_data())

def main():
    num_threads = 16

    q = queue.Queue()
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=make_iterator, args=(q,))
        t.daemon = True
        t.start()
        threads.append(t)

    for i in range(100000):
        print(i)
        q.get()


if __name__ == "__main__":
    main()