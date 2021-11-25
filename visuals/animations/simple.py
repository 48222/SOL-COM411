import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.plot(range(frame), range(frame))


def run():
    global fig
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    s_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
    plt.show()


run()
