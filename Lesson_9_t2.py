import argparse


parser = argparse.ArgumentParser(description='Приховуємо частину имейлу')
parser.add_argument('email', type=str, help='Е-мейл, котрий ховаємо')
args = parser.parse_args()


def hide_email(e) -> str:
    x = e.split(sep='@')
    print(x[0][len(x[0]) - 2])
    '''x[0].replace(x[len(x[0])-2], '*')'''


hide_email(args.email)
