#-------------------------------------------------------------
# ARGOSTrackingTool.py
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Modified by Xiaoge Zhang 
# Date:   Fall 2022
#--------------------------------------------------------------


#Create a variable pointing to the data file
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line = file_object.readline()

# for line in line_list:
#     if line[0] in ('#', 'u'):
#         continue
#     line_split = line.split()
#     record_id = line_split[0]
#     obs_date = line_split[2]
#     obs_lc = line_split[4]
#     obs_lat = line_split[6]
#     obs_lon = line_split[7]

while line:
    if line[0] in ('#', 'u'):
        line = file_object.readline()
        continue
    line_split = line.split()
    record_id = line_split[0]
    obs_date = line_split[2]
    obs_lc = line_split[4]
    obs_lat = line_split[6]
    obs_lon = line_split[7]

#Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")