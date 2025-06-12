# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: w2051819 (20231068)
# Date: 11/12/2023


from graphics import *

count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0
quit_continue = "y"
list_of_results = []  # List to append data --> part 2

def histogram(count_list):
    win = GraphWin("Histogram", 500, 500)
    win.setBackground("mint cream")

    heading = Text(Point(120, 30), "Histogram Results")  # Heading
    heading.setStyle("bold")
    heading.setSize(16)
    heading.draw(win)

    ln = Line(Point(40, 430), Point(450, 430))  # draw the bottom line
    ln.draw(win)

    txt_end = Text(Point(100, 470), str(sum(count_list)) + " outcomes in total.")  # last text
    txt_end.draw(win)

    count_max = max(count_list)  # maximum value in count_list

    rect_01 = Rectangle(Point(60, 430 - (count_progress / count_max * 300)), Point(150, 430))  # design the progress bar
    rect_01.setFill("pale green")
    rect_01.draw(win)

    rect_02 = Rectangle(Point(155, 430 - (count_trailer / count_max * 300)), Point(245, 430))  # design the trailer bar
    rect_02.setFill("yellow green")
    rect_02.draw(win)

    rect_03 = Rectangle(Point(250, 430 - (count_retriever / count_max * 300)), Point(340, 430))  # design the retriever bar
    rect_03.setFill("olive")
    rect_03.draw(win)

    rect_04 = Rectangle(Point(345, 430 - (count_exclude / count_max * 300)), Point(435, 430))  # design the exclude bar
    rect_04.setFill("thistle")
    rect_04.draw(win)

    txt_01 = Text(Point(105, 440), "Progress")  # "Progress" under the progress bar
    txt_01.draw(win)

    txt_02 = Text(Point(200, 440), "Trailer")  # "Trailer" under the trailer bar
    txt_02.draw(win)

    txt_03 = Text(Point(295, 440), "Retriever")  # "Retriever" under the retriever bar
    txt_03.draw(win)

    txt_04 = Text(Point(390, 440), "Excluded")  # "Excluded" under the exclude bar
    txt_04.draw(win)

    count_01 = Text(Point(105, 420 - (count_progress / count_max * 300)), count_progress)  # counts of credits above bars
    count_01.draw(win)

    count_02 = Text(Point(200, 420 - (count_trailer / count_max * 300)), count_trailer)
    count_02.draw(win)

    count_03 = Text(Point(295, 420 - (count_retriever / count_max * 300)), count_retriever)
    count_03.draw(win)

    count_04 = Text(Point(390, 420 - (count_exclude / count_max * 300)), count_exclude)
    count_04.draw(win)

    win.getMouse()  # when you click on the window it finishes the process
    win.close()

def calculate_progression(pass_credits, defer_credits, fail_credits):
    global count_progress, count_exclude, count_retriever,count_trailer

    total_credits = pass_credits + defer_credits + fail_credits
    if total_credits != 120:
        return "Total incorrect"
    if pass_credits == 120:
        count_progress += 1
        return "Progress"
    elif fail_credits >= 80:
        count_exclude += 1
        return "Exclude"
    elif (pass_credits == 100 and fail_credits == 20) or (pass_credits == 100 and defer_credits == 20):
        count_trailer += 1
        return "Progress (module trailer)"
    else:
        count_retriever+= 1
        return "Do not progress – module retriever"

def main():
    global quit_continue  # Declare quit_continue as global

    quit_continue = "y"  # Initialize quit_continue with a default value

    user_type = input("Are you a staff member or student? Enter 1 for student or 2 for staff: ")

    if user_type == "1":  # Student
          try:
            pass_credits = int(input("Enter the number of credits at pass: "))
            defer_credits = int(input("Enter the number of credits at defer: "))
            fail_credits = int(input("Enter the number of credits at fail: "))

            if 0 <= pass_credits <= 120 and 0 <= defer_credits <= 120 and 0 <= fail_credits <= 120:
                    outcome = calculate_progression(pass_credits, defer_credits, fail_credits)
                    print("Progression Outcome:", outcome)
                    list_of_results.extend([outcome, pass_credits, defer_credits, fail_credits])
            else:
                print("Invalid input. Credits should be between 0 and 120.")

          except ValueError:
                
                print("Invalid input. Please enter valid integers.")

     
    elif user_type == "2":  # Staff member
        while quit_continue.lower() == "y":
            try:
                pass_credits = int(input("Enter the number of credits at pass: "))
                defer_credits = int(input("Enter the number of credits at defer: "))
                fail_credits = int(input("Enter the number of credits at fail: "))

                if 0 <= pass_credits <= 120 and 0 <= defer_credits <= 120 and 0 <= fail_credits <= 120:
                    outcome = calculate_progression(pass_credits, defer_credits, fail_credits)
                    print("Progression Outcome:", outcome)
                    list_of_results.extend([outcome, pass_credits, defer_credits, fail_credits])
                else:
                    print("Invalid input. Credits should be between 0 and 120.")

            except ValueError:
                print("Invalid input. Please enter valid integers.")

            print("Would you like to enter another set of data? ")
            quit_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")

    outcomes = count_progress + count_trailer + count_retriever + count_exclude
    count_list = [count_progress, count_trailer, count_retriever, count_exclude]  # make a list for counts

    histogram(count_list)

    ### PART 02 ### LIST ###
    print("\nPart 2: ")
    for i in range(0, len(list_of_results), 4):
        print(list_of_results[i] + " - " + str(list_of_results[i + 1]) + ", " + str(list_of_results[i + 2]) + ", " + str(list_of_results[i + 3]))

    ### PART 03 ### FILE HANDLING ###
    print("\nPart 3: ")
    with open('test.txt', 'w') as file:  # write to the file
        for i in range(0, len(list_of_results), 4):
            file.write(list_of_results[i] + " - ")
            file.write(str(list_of_results[i + 1]) + ", ")
            file.write(str(list_of_results[i + 2]) + ", ")
            file.write(str(list_of_results[i + 3]) + "\n")

    with open('test.txt', 'r') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()
