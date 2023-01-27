# Final Project
# CS 111, Reckinger
# TODO: Comment here

import turtle
import random
import image

## Write your code here.  


def loading_data(file_name):
  file= open(file_name)
  player_list= file.readlines()
  myDict = {}
  for i in range(len(player_list)):
    player_list[i] = player_list[i].strip("\n")
  for i in range(len(player_list)):
    templist = player_list[i].split() 
    x = templist[0] + " " +templist[1]
    myDict[x] = [templist[2]+ " " +templist[3], templist[4], templist[5], templist[6], templist[7]]
  for v in myDict.values():
    for i in range(len(v)):
      v[i] = v[i].strip(",")
  return myDict

def west_or_east(Dict):
  West_Conference = ["Houston Rockets", "Los_Angeles Lakers","Los_Angeles Clippers","Denver Nuggets", "Utah Jazz", "Oklohoma_City Thunders", "Dallas Mavericks", "Memphis Grizzlies", "Portland Trailblazers", "New_Orleans Pelicans", "San_Antonio Spurs", "Phoenix Suns", "Minnesota Timberwolves", "Golden_State Warriors"]
  East_Conference = ["Boston Celtics","Brooklyn Nets","Indiana Pacers","Miami Heat","Milwuakee Bucks","Orlando Magic","Philadelphia 76ers","Toronto Raptors","Washington Wizards"]
  player_choice= input("What Conference does your player play for? (West or East)")
  player_choice = player_choice.lower()
  new_dictionary= {}
  if player_choice == "west":
    for k , v in Dict.items():
      if v[0] in West_Conference:
        new_dictionary[k] = v
  elif player_choice == "east":
    for k , v in Dict.items():
      if v[0] in East_Conference:
        new_dictionary[k] = v
  if not new_dictionary:
    print("There is no player with those stats!")
    quit()
  check_single_player(new_dictionary)
  return new_dictionary

def point_averages(Dict):
  point_average = float(random.randrange(10, 20))
  player_choice =input("Did your player average over {p} points per game? (Yes or No)".format(p = point_average))
  player_choice = player_choice.lower()
  new_dictionary = {}
  if player_choice == "yes":
    for k , v in Dict.items():
      if (float(v[2])) > point_average:
        new_dictionary[k] = v
  elif player_choice == "no":
    for k, v in Dict.items():
      if (float(v[2])) < point_average:
        new_dictionary[k] = v
  if not new_dictionary:
    print("There is no player with those stats!")
    quit()
  check_single_player(new_dictionary)
  return new_dictionary

def injury_replacement(Dict):
  player_choice = input("Was your player selected as an injury replacement? (Yes or No)")   
  player_choice = player_choice.lower()
  new_dictionary = {}
  if player_choice == "yes":
    for k , v in Dict.items():
      if k[-2] == "*":
        new_dictionary[k] = v
  elif player_choice == "no":
    for k , v in Dict.items():
      if k[-2] != "*":
        new_dictionary[k] = v
  if not new_dictionary:
    print("There is no player with those stats!")
    quit()
  check_single_player(new_dictionary)
  return new_dictionary

def position_classification(Dict):
  positions = ["Forward", "Guard", "Center"]
  picked_position = random.choice(positions)
  new_dictionary = {}
  if picked_position == "Forward":
    specific_attributes = ["F-C", "C-F", "F", "G-F", "F-G"]
    player_choice = input("Does your player traditionally play Small Forward/ Power Forward? (Yes or No)")
  elif picked_position == "Guard":
    specific_attributes = ["G-F", "F-G", "G"]
    player_choice = input("Does your player traditionally play Point Guard/ Shooting Guard? (Yes or No)")
  else:
    specific_attributes = ["F-C", "C-F", "C"]
    player_choice = input("Does your player traditionally play Center (Yes or No)")
  player_choice = player_choice.lower()
  if player_choice == "yes":
    for k, v in Dict.items():
      if v[1] in specific_attributes:
        new_dictionary[k] = v
  elif player_choice == "no":
    for k, v in Dict.items():
      if v[1] not in specific_attributes:
        new_dictionary[k] = v
  if not new_dictionary:
    print("There is no player with those stats!")
    quit()
  check_single_player(new_dictionary)
  return new_dictionary

def rebound_averages(Dict):
  rebound_average = float(random.randrange(5,8))
  player_choice =input("Did your player average over {r} rebounds per game? (Yes or No)".format(r = rebound_average))
  player_choice = player_choice.lower()
  new_dictionary = {}
  if player_choice == "yes":
    for k , v in Dict.items():
      if (float(v[4])) > rebound_average:
        new_dictionary[k] = v
  elif player_choice == "no":
    for k, v in Dict.items():
      if (float(v[4])) < rebound_average:
        new_dictionary[k] = v
  if not new_dictionary:
    print("There is no player with those stats!")
    quit()
  check_single_player(new_dictionary)
  return new_dictionary

def assist_averages(Dict):
  assist_average = float(random.randrange(5,10))
  player_choice =input("Did your player average over {a} assists per game? (Yes or No)".format(a = assist_average))
  player_choice = player_choice.lower()
  new_dictionary = {}
  if player_choice == "yes":
    for k , v in Dict.items():
      if (float(v[3])) > assist_average:
        new_dictionary[k] = v
  elif player_choice == "no":
    for k, v in Dict.items():
      if (float(v[3])) < assist_average:
        new_dictionary[k] = v
  if not new_dictionary:
    print("There is no player with those stats!")
    quit()
  check_single_player(new_dictionary)
  return new_dictionary

def random_function_call(x):
  a = loading_data(x)
  function_list = [west_or_east, point_averages, injury_replacement, position_classification, rebound_averages, assist_averages]
  random.shuffle(function_list)
  b = function_list[-1](a)
  function_list.pop()
  random.shuffle(function_list)
  c = function_list[-1](b)
  function_list.pop()
  random.shuffle(function_list)
  d = function_list[-1](c)
  function_list.pop()
  random.shuffle(function_list)
  e = function_list[-1](d)
  function_list.pop()
  random.shuffle(function_list)
  f = function_list[-1](e)
  function_list.pop()
  random.shuffle(function_list)
  g = function_list[-1](f)
  return g

def check_single_player(Dict):
  if len(Dict) == 1:
    print("\n")
    for k, v in Dict.items():
      player_name = k.strip(",")
      stats = v
      if player_name[-1] == "*":
        player_name = player_name.strip("*")
    print("******************************")
    print("The player you were thinking of was {a}!".format(a= player_name))
    print("\n")
    print("{a} currently plays for the {b}".format(a = player_name, b= stats[0]))
    print("\n")
    print("{a} averaged the following stats for the {b} season: ".format(a = player_name, b= choice))
    print("******************************")
    print(stats[2], "Points Per Game")
    print(stats[3], "Assists Per Game")
    print(stats[4], "Rebounds Per Game")
    print("******************************")
    print("\n")
    print("Thank you for playing!")
    s = turtle.getscreen()
    t= turtle.Turtle()
    s.colormode(255)
    t.shape("classic")
    t.speed("fastest")

    filename = "NBA.gif"
    img = image.FileImage(filename)
    width = img.get_width()
    height = img.get_height()
    # For loop that runs through each 5th pixel of the row and height of the GIF image, grabs the RGB values of the GIF Image
    # and set the turtle to stamp that specific pixel but makes all blue RGB values set to 0
    for row in range(0,height, 10):
      for col in range(0,width, 10):
        pixel = img.get_pixel(col, row)
        x= col - (width/2)
        y= -row + (height/2)
        t.goto(x,y)
        r = pixel.red
        g = pixel.green
        b= pixel.blue
        t.pencolor(r,g,b)
        t.fillcolor(r,g,b)
        t.stamp()
          
    turtle.mainloop() # uncomment once you start doing turtle drawing
    quit()

if __name__ == "__main__":
  print("Welcome to the NBA-All Star Akinator!")
  print("The Rosters of the 2020, 2021, and 2022 All-Star Players can be found here:")
  print("2020: https://www.nba.com/allstar/2020/draft")
  print("2021: https://www.nba.com/2021-all-star-roster")
  print("2022: https://www.nba.com/allstar/2022/all-star-roster")
  print("\n")
  print("Data for the stats of the All-Star Players stats were imported and can be looked up here:")
  print("https://www.statmuse.com/")
  print("\n")
  choice = input("What year of the NBA All-Stars Would you like to play? (2020,2021, or 2022)")

  if choice == "2020":
    g = random_function_call("2020_All_Star_Players.txt")
  elif choice == "2021":
    g = random_function_call("2021_All_Star_Players.txt")
  else:
    g = random_function_call("2022_All_Star_Players.txt")
  
  if len(g) > 1:
    player_amount = len(g)
    print("There are only {a} players with those stats".format(a= player_amount))
    print("\n")
    last_dictionary = {}
    for i in range(len(g)):
      for k, v in g.items():
        k = k.strip(",")
        second_choice = input("Is {a} The player that you are thinking of (Yes or No)?".format(a= k))
        second_choice = second_choice.lower()
        if second_choice == "yes":
          last_dictionary[k] = v
          check_single_player(last_dictionary)
        else:
          continue




