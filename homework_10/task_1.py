# Написать функцию которая посчитает количество очков футбольной команды.
# Победа дает 3 очка, ничья 1 очко, поражение 0 очков.
# Функция принимает три аргумента - win, draw, loss.
# Пример : count_points(3, 2, 2) -> 11

win = input('How many times has the football team won - ')
draw = input('How many times has the football team tied - ')
loss = input('How many times has the football team loss - ')


def count_point(w, d, lo):
    w, d, lo = map(int, [w, d, lo])
    count = sum([w*3, d*1, lo*0])
    return count


print('Team points -', count_point(win, draw, loss))
