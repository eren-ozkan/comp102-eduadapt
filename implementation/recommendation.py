levels_example = ["F" , "E" , "D" , "C" , "B" , "A"]

def recommend_next_course(quiz_score, current_level):
    if quiz_score >= 85:
        if current_level == "A":
            return "Upcoming course level: " + current_level
        else:   
            current_level = levels_example[levels_example.index(current_level) + 1]
            return "Upcoming course level: " + current_level
    elif quiz_score < 60:
        return "Review material shown"
    else:
        return "Upcoming course level: " + current_level

#Example input: recommend_next_course(86 , "C")
#Output: Upcoming course level: B

def check_inactivity(days_inactive_consecutively):
    if days_inactive_consecutively >= 3:
        return "Notification sent to the user"
    else:
        return "No notification needed"
    
#Example input: check_inactivity(4)
#Output: Notification sent to the user