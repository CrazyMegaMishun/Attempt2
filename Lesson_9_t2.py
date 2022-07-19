import argparse


parser = argparse.ArgumentParser(description='Приховуємо частину имейлу')
parser.add_argument('email', type=str, help='Е-мейл, котрий ховаємо')
args = parser.parse_args()


def hide_email(e) -> str:
    x = e.split(sep='@')
    for i in range(len(x[0])-2):
        x[0] = x[0].replace(x[0][i], '*')

    return '{}@{}'.format(x[0], x[1])


print(hide_email(args.email))
