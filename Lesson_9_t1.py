import argparse


parser = argparse.ArgumentParser(description='Рахуємо очки')
parser.add_argument('-w', '--win', type=int, help='Кількість перемог, 3 балли за кожну')
parser.add_argument('-d', '--draw', type=int, help='Кількість нічей, 1 балл за кожну')
parser.add_argument('-l', '--loss', type=int, help='Кількість поразок, -1 балл за кожну')
args = parser.parse_args()


def count_points(win, draw, loss) -> int:
    return (win*3) + draw - loss


print(count_points(args.win, args.draw, args.loss))
