import concurrent.futures
import time

def worker(thread_number):
    # Crie uma lista de números
    lista = [i for i in range(1, 6)]

    # Imprima a lista
    print(f"Thread {thread_number}: {lista}")

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):  # Neste exemplo, usaremos 3 threads
            executor.submit(worker, i)
            time.sleep(2)  # Espera por 2 segundos antes de criar a próxima thread

if __name__ == "__main__":
    main()
