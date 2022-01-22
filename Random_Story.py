import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On the 20th of January']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Jeff', 'Bob','Adam', 'Mrs. Isitt', 'Piyush']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['a movie', 'a university','a seminar', 'a school', 'to an underground palace']
happened = ['made a lot of friends','ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']
x=1
while x <= 5:
    x += 1
    print(random.choice(when) + ', ' + random.choice(who) + ' who lived in ' + random.choice(residence) + ', went to ' + random.choice(went) + ', and ' + random.choice(happened) + '!')
    print()
