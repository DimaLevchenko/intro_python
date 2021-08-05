# Написать функцию которая будет частично скрывать e-mail, пример:
# hide_email(somebody_email@gmail.com) -> em***@**il.com

email = input('Input email - ')


def hide_email(mail):
    part1, part = mail.split('@')
    part2, part3 = part.split('.')
    return f'{part1[:4]}***@**{part2[-3:]}.{part3}'


print('Hidden email -', hide_email(email))
