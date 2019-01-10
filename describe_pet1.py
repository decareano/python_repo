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

def make_album(artist_name, album_title, tracks=11):
  # artist = { 'name': artist_name, 'album': album_title, 'number': tracks }
  artist = artist_name + ' ' +  album_title
  
  return artist

my_album1 = make_album('madonna', 'world tour')
my_album2 = make_album('billy joel', 'tour of force', 14)
my_album3 = make_album('hendrix', 'purple haze')
print(my_album1, my_album2, my_album3)

while True:
  print("\nPlease pick an album: ")
  print("(enter 'q' to quit)")
 
  i_artist = input("artist: ")
  if i_artist == 'q':
    break

  i_album = input("album: ")
  if i_album == 'q':
    break

format_name = make_album(i_artist, i_album)
print("\nHello, " + format_name +  "!")

