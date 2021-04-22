from matplotlib import pyplot as plt

def logistic_map(x, r):
    return r*x*(1 - x)

def get_bifurcation_diagram_data(x0, n_from, n_to, r_from, r_to, r_step):
    x_data = []
    y_data = []

    r = r_from
    while r <= r_to:
        x = x0
        for n in range(n_to + 1):
            x = logistic_map(x, r)
            if n >= n_from:
                x_data.append(r)
                y_data.append(x)
        r += r_step

    return (x_data, y_data)

def main():
    x_data, y_data = get_bifurcation_diagram_data(
        x0=0.5,
        n_from=0,
        n_to=512,
        r_from=0,
        r_to=4,
        r_step=0.0005
    )

    plt.scatter(x_data, y_data, marker='.', s=0.1, linewidths=0, alpha=0.06)
    plt.autoscale(enable=True, axis='both', tight=True)
    plt.xlabel("r")
    plt.ylabel("x")
    plt.show()

if __name__ == "__main__":
    main()