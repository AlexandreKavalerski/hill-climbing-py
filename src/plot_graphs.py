import matplotlib.pyplot as plt


def plot_cities(problem):
    coords = list(problem.node_coords.values())
    fig, ax = plt.subplots()
    ax.set_title('Cidades')
    for i in range(len(coords)):
        ax.scatter(coords[i][0], coords[i][1])
    plt.show()


def plot_path(problem, state, distance, path_description, file_name, num_exec):
    coords = list(problem.node_coords.values())
    fig, ax = plt.subplots(2)
    ax[0].set_title('Cidades')
    ax[1].set_title('Tour - ' + path_description)
    for i in range(len(coords)):
        ax[0].scatter(coords[i][0], coords[i][1])
        ax[1].scatter(coords[i][0], coords[i][1])

    for i in range(len(state)-1):
        ax[1].annotate("",
                       xy=problem.node_coords[state[i]], xycoords='data',
                       xytext=problem.node_coords[state[i+1]], textcoords='data',
                       arrowprops=dict(arrowstyle="->",
                                       connectionstyle="arc3"))

    textstr = 'Nº nós: {}\nDistância total: {}'.format(len(state), distance)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax[1].text(0.05, 0.95, textstr, transform=ax[1].transAxes, fontsize=14,  # Textbox
               verticalalignment='top', bbox=props)
    to_save = '../results/graph_{}_{}_{}.pdf'.format(path_description, file_name, num_exec)
    plt.savefig(to_save, dpi=400)
    plt.tight_layout()
    plt.show()