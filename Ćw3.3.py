slownik = {'cukier': 'kg','mleko': 'opakowanie','lizak': 'szt',}

odwrocony_slownik = {value: key for key, value in slownik.items()}

print('Oryginalny słownik:')

print(slownik)



print('Odwrócony słownik:')

print(odwrocony_slownik)