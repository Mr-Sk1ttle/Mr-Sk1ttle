# pip install scratchclient in the terminal
from scratchclient import ScratchSession # import the scratch module (If you would like to you can put "from scratchclient import *" instead)

s = ScratchSession("scratch username here", "scratch password here") # This is how you sign into your scratch profile
i = 0 # set i to 0 to setup a forever loop
pID = "Your Scratch Project ID here" This is where you put the project ID of your scratch project
p = s.get_project(pID) # This is just simplifying "get_project(pID)" so you don't have to retype the whole thing everytime (You don't necassarily need this line)
c = s.create_cloud_connection(pID) # This is just simplifying "create_cloud_connection(pID)" same thing as above
set_ = c.set_cloud_variable # This is just simplifying "set_cloud_variable" same thing as above
while i > -1: # This is how I do my forever loops because they seem to work better
  hearts = p.love_count # getting the data for how many hearts your project has
  stars = p.favorite_count # getting the data for how many stars your project has
  remixes = p.remix_count # getting the data for how many remixes your project has
  views = p.view_count # getting the data for how many views your project has
  title = f"This Project Has {views} Views!" # This is setting a variable to be the title when we need to put what we want the title to be
  set_("Hearts", hearts) # This is setting a global scratch variable to the hearts python variable. You will need to create a global scratch variable named "Hearts"
  set_("Stars", stars) # This is setting a global scratch variable to the stars python variable. You will need to create a global scratch variable named "Stars"
  set_("Remixes", remixes) # This is setting a global scratch variable to the remixes python variable. You will need to create a global scratch variable named "Remixes"
  set_("Views", views) # This is setting a global scratch variable to the views python variable. You will need to create a global scratch variable named "Views"
  p.set_title(title) # This is setting your scratch project's title to the title python variable

MAKE SURE TO USE WITH CREDIT IF YOU ARE GOING TO USE THIS FOR A SCRATCH PROJECT! CREDIT @MysticalSk1ttle IF YOU DO YOU USE THIS CODE AND MAKE SURE TO LINK THIS
GITHUB PAGE AS WELL! THANK YOU!
