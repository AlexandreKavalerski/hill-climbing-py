import hill_climbing as hc
import codecs

file_name = 'dj38'


def main():
    log = ''
    for i in range(1, 11):
        solution, distance = hc.index(file_name, i)
        log += '[loop n-{}]\n{}\nDistancia: {}\n---\n'.format(i, solution, distance)

    f = codecs.open('../results/log_' + file_name + '.txt', 'w', 'utf-8')
    f.write(log)
    f.close()
    print('finalizado.')


if __name__ == '__main__':
    main()
