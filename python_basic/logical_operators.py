if True:
    print('Indeed,true')

is_admin = True
if is_admin:
    print('admin is true')


selected_character = input()

if selected_character == 'Protos':
    print('Protos is the most powerful race')
elif selected_character == 'Zerg':
    print('Zerg is the most weak race but it spreads like a plague')
elif selected_character == 'Terrain':
    print('Terrain is a race balanced between Z and P')
else:
    print('Hmm... it seems we have a new race')