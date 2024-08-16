lista_convidados = ['Draco Malfoy', 'Hermione Granger', 'Crookshanks']
print(f'Ilustre Sr.{lista_convidados[0]}, você está convidado para jantar hoje, às 19 horas.')
print(f'Ilustre Srta.{lista_convidados[1]}, você está convidada para jantar hoje, às 19 horas.')
print(f'Ilustre Sr.{lista_convidados[2]}, você está convidado para jantar hoje, às 19 horas.')
print(f'Infelizmente, o Sr. {lista_convidados[2]} não poderá comparecer.')  

del lista_convidados[2]
lista_convidados.insert(2, 'Harry Potter')
print(f'Ilustre Sr.{lista_convidados[0]}, você está convidado para jantar hoje, às 19 horas.')
print(f'Ilustre Srta.{lista_convidados[1]}, você está convidada para jantar hoje, às 19 horas.')
print(f'Ilustre Sr.{lista_convidados[2]}, você está convidado para jantar hoje, às 19 horas.')
