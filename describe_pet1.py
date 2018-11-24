def get_formatted_name(first_name, last_name):
  full_name = first_name + ' ' + last_name
  return full_name.title()

while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")
  
  f_name = input("First name: ")
  if f_name == 'q':
    break
  l_name = input("Last name: ")
  if l_name == 'q':
    break
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")

def make_album(artist_name, album_title):
  artist = { 'name': artist_name, 'album': album_title }
  return artist

my_album = make_album('madonna', 'world tour')
my_album1 = make_album('billy joel', 'tour of force')
my_album2 = make_album('hendrix', 'purple haze')
print(my_album, my_album1, my_album2)
