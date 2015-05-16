# by Ian Garrett and Connor Mathias (PARTNER PROGRAMMING)
# Lab 9
# NOTE: One extra credit function (ends with) is included
def read_names(file_name):
          with open(file_name, "r") as my_file:
                    name_list = []
                    for line in my_file:
                               line = line.strip()
                               line_list = line.split(",")

                               name = line_list[0].lower()
                               #name = name.lower()
                               sex = line_list[1]
                               count = int(line_list[2])

                               line_list[0] = name
                               line_list[2] = count
                               name_list.append(line_list)
                    return name_list

def clean_input(name):
          cleaned_input = name.lower()
          return cleaned_input

full_names=[]
spacer = "-------------------------------"

name_list = read_names("yob1996.txt")
print ("U.S. Baby Name Data From 1996")
print (spacer)
flag = 1
while flag == 1:
          question = "q"
          if question == "q":
                    print ()
                    x =input("What kind of search?\nF Full match\nB Begins with\nE Ends with\nX Exit:")
                    x = x.lower()
                    print()
          if x != "f" and x != "b" and x != "e" and x != "x":
                    print()
                    print ("Invalid response,  please try again")
                    q = "q"

          if x == "f":
                    print()
                    name = input("Type a name: ")
                    clean_name = clean_input(name)
                    female_name_count = 0
                    male_name_count = 0
                    number_of_names = 0
                    for substring in name_list:
                              if clean_name == substring[0] :
                                        number_of_names += 1
                                        if substring[1] == "F":
                                                  female_name_count += int(substring[2])
                                        else:
                                                  male_name_count += int(substring[2])
                    total_names = female_name_count + male_name_count
                    print(name,("\t"*2) + "F" + "\t", str(female_name_count)+"\n"+ name, ("\t"*2) + "M" + "\t", str(male_name_count) + "\n"+ spacer + "\n" + "Total names" + ("\t"*2)+ str(number_of_names) +"\n" + "Total with name" + ("\t"*2) +str( total_names))
                    print()
                    question = "q"

          if x =="b":
                    print()
                    begins_with = input("Type a name: ")
                    begins_with = begins_with.lower()
                    female_names = 0
                    male_names = 0
                    f_begins_with = []
                    m_begins_with = []
                    distinct_names = 0
                    total_names = 0

                    for substring in name_list:
                              if substring[0].startswith(begins_with) and substring[1] == "F":
                                        f_begins_with.append(substring)
                                        distinct_names += 1
                                        total_names += int(substring[2])
                              if substring[0].startswith(begins_with) and substring[1] == "M":
                                        m_begins_with.append(substring)
                                        distinct_names += 1
                                        total_names += int(substring[2])
                    
                    for i in f_begins_with:
                              print (i[0] + "\t" + "F" + "\t" + str(i[2]))
                    print(spacer)
                    for i in m_begins_with:
                              print (i[0] + "\t" + "M" + "\t" + str(i[2]))
                    print(spacer)
                    print("Distinct Names\t" + str(distinct_names))
                    print("Total names\t" + str(total_names))
                    print()
                    question = "q"

          if x =="e":
                    print()
                    ends_with = input("Type a name: ")
                    ends_with = ends_with.lower()
                    female_names = 0
                    male_names = 0
                    f_ends_with = []
                    m_ends_with = []
                    distinct_names = 0
                    total_names = 0

                    for substring in name_list:
                              if substring[0].endswith(ends_with) and substring[1] == "F":
                                        f_ends_with.append(substring)
                                        distinct_names += 1
                                        total_names += int(substring[2])
                              if substring[0].endswith(ends_with) and substring[1] == "M":
                                        m_ends_with.append(substring)
                                        distinct_names += 1
                                        total_names += int(substring[2])
                    
                    for i in f_ends_with:
                              print (i[0] + "\t" + "F" + "\t" + str(i[2]))
                    print(spacer)
                    for i in m_ends_with:
                              print (i[0] + "\t" + "M" + "\t" + str(i[2]))
                    print(spacer)
                    print("Distinct Names\t" + str(distinct_names))
                    print("Total names\t" + str(total_names))
                    print()
                    question = "q"
          if x== "x":
                    flag = 0
print (spacer)
print ("Thank you for using the U.S. Baby Names database")
                                        
                               
