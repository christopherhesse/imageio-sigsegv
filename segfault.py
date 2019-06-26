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
