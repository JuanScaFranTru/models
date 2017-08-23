from models.positive_models import PositiveLinearRegression
from models.utils import load_data, plot, stats, show


if __name__ == '__main__':
    data_len, weeks, ts, xs = load_data()

    linear_model = PositiveLinearRegression()
    linear_model.fit(xs, ts)

    means, std_devs = [], []
    values = list(range(5, 200, 5))
    for i in values:
        _, mean, std_dev = stats(xs, ts, linear_model, n_splits=i)
        means.append(mean)
        std_devs.append(std_dev)
    plot(values, means)
    plot(values, std_devs)
    show()



