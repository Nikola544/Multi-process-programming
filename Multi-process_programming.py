import time
from multiprocessing import Pool


def read_info(name):

    all_data = []
    try:
        with open(name, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {name} не найден!")
    return all_data


def measure_time(func, *args):

    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time


def linear_execution(filenames):

    for filename in filenames:
        read_info(filename)


def parallel_execution(filenames):

    with Pool() as pool:
        pool.map(read_info, filenames)


if __name__ == "__main__":

    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

    print("Линейное выполнение:")
    linear_time = measure_time(linear_execution, filenames)
    print(f"Время выполнения: {linear_time:.6f} секунд")

    print("\nМногопроцессное выполнение:")
    parallel_time = measure_time(parallel_execution, filenames)
    print(f"Время выполнения: {parallel_time:.6f} секунд")
