import numpy as np
import matplotlib.pyplot as plt

plt.style.use('./Gui/tmp/rose-pine.mplstyle')

def create_subplots():
    """
    Creates a 2x2 grid of subplots with different types of plots.
    """
    np.random.seed(0)
    fig, ax = plt.subplots(2, 2, figsize=(11, 8))
    
    # Bar plot
    x = np.arange(10)
    y = np.random.rand(10)
    ax[0, 0].bar(x, y)

    # Scatter plot
    x = np.random.rand(100)
    y = np.random.rand(100)
    ax[0, 1].scatter(x, y, s=100)

    # Line plot
    ax[1, 0].plot(np.random.randn(30))

    # Boxplot
    data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']
    bplot1 = ax[1, 1].boxplot(data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks

    colors = [ 'lightblue', 'lightgreen', 'pink']
    for patch, color in zip(bplot1['boxes'], colors):
        patch.set_facecolor(color)
        
def main():
    create_subplots()


if __name__ == '__main__':
    main()
plt.show()