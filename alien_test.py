alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('Just earned ' + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
      
for i in range(3):
    for j in range(3):
        print("*", end = " ")
    print(" ")




    

