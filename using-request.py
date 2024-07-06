from datetime import date

the_beatles= [{'nombre': 'Jhon', 'apellido': 'Lennon', 'fecha': date(1940, 10, 9)},
              {'nombre': 'Paul', 'apellido': 'MacKarnney', 'fecha': date(1942, 6, 18)},
              {'nombre': 'George', 'apellido': 'Harrison', 'fecha': date(1943, 2, 25)},
              {'nombre': 'Ringo', 'apellido': 'Start', 'fecha': date(1940, 7, 7)}]

the_beatles.sort(key=lambda ele: ele['fecha'])

print(the_beatles)