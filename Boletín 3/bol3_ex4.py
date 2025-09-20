persoa1 = {
    'nome': 'Pablo',
    'peso': 66, }

persoa2 = {
    'nome': 'Eva',
    'peso': 75, }

if int(persoa1['peso']) > int(persoa2['peso']):
    print(f"{persoa1['nome']} pesa {persoa1['peso']}.")
elif int(persoa2['peso']) > int(persoa1['peso']):
    print(f"{persoa2['nome']} pesa {persoa2['peso']}.")

print(f"A diferenza entre o peso de {persoa1['nome']} e {persoa2['nome']} é de {max(int(persoa1['peso']), int(persoa2['peso'])) - min(int(persoa1['peso']), int(persoa2['peso']))}.")