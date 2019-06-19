import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt



def play(x1, y1, x2, y2):
    fig = plt.figure()
    ax = plt.axes(xlim=(-3,3), ylim=(-5,5))
    line1, = ax.plot([], [], color='red')
    line2, = ax.plot([], [], marker='o', color='red', markersize=10)
    line3, = ax.plot([], [], color='blue')
    line4, = ax.plot([], [], marker='o', color='blue', markersize=10)
    lines = [line1, line2, line3, line4]

    plt.xlabel('x', fontsize=10)
    plt.ylabel('v', fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    frames = x1.shape[0]

    # x = np.arange(100)
    # y = np.sin(x)

    def init():
        for line in lines:
            line.set_data([], [])

        return lines

    def animate(i):
        line1.set_data(x1[0:i+1], y1[0:i+1])
        line2.set_data(x1[i], y1[i])

        line3.set_data(x2[0:i+1], y2[0:i+1])
        line4.set_data(x2[i], y2[i])

        ax.set_title('Frame %d' %i, fontsize=10)

        return lines

    anim = animation.FuncAnimation(fig, animate,
                                   init_func=init,
                                   frames=frames,
                                   interval=50,
                                   blit=False)

    anim.save('video.mp4', writer='ffmpeg')
    return anim
