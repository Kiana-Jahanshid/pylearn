import os 
import imageio

file_list = sorted(os.listdir("Assignment_8/images"))
Images = []
for file_name in file_list :
    print(file_name)
    file_path = "Assignment_8/images/" + file_name
    #print(file_path)
    image =imageio.imread(file_path)
    Images.append(image)

print(file_list)  
imageio.mimsave("Assignment_8/output.gif" , Images , fps = 5) 
