a="hello"
print (a)

b="""asdfgg asddghjrkk
sghdjkhfkcbhvfkjf
fhdbnkjnknlk"""
print(b)

c='''dafgsfwtyduhjg gfhjbjf
dghfkjdgjdlk
djbfrghnkjl fuurhf'''
print(c)

d="hello pp2"
print(d[5])

e="wonderful day"
print(e[5:7])

f="just try"
print(f[-3:-1])

g="beautiful thing"
print(len(g))

h="   best friend   "
print(h.strip())

i="LIKE you"
print(i.lower())

j="microphone"
print(j.upper())

k="my sister"
print(k.replace("my", "sister"))

l="my brother"
print(l.split(","))

txt="the most important think"
x="important" in txt
print(x)

m="i like my village"
x="thank" not in m
print(x)

n="I"
o="like"
p="book"
q=n + " " + o + " " + p
print(q)

age=125
mass=125
children=125
txt="""my turtle is {} years old, 
it weighs {} kilo,
she has {} children """
print(txt.format(age, mass,children))


txt="я хочу быть сильной как \"брат\""
print(txt)