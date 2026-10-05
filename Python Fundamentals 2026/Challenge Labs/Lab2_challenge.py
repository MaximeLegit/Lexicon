speakers = ["Anna", "Max", "Eren", "Lola", "Jean"]
rooms = set(["alpha", "beta", "gamma", "delta"])
participants = ["Annie", "Bobby", "Clara", "Damon", "Eren", "Fanny", "Grace", "Holly", "Inde", "Jolene"]
topics = ["Intro", "Applying principles in real life", "AES256", "Data theft prevention", "Advanced module"]

sessions = [{"session title":"Privacy", "speaker": speakers[0], "room": "alpha", "schedule": ("08.00", 50), "topic" : topics[0], "participants" : participants[0:8]},
            {"session title":"Cryptography", "speaker": speakers[1], "room": "beta", "schedule": ("09.00", 45), "topic" : topics[1], "participants" : participants[0:5]},
            {"session title":"Security", "speaker": speakers[2], "room": "gamma", "schedule": ("10.00", 50), "topic" : topics[2], "participants" : participants[2:6]},
            {"session title":"Obfuscation", "speaker": speakers[3], "room": "delta", "schedule": ("11.00", 45), "topic" : topics[3], "participants" : participants[4:9]},
            {"session title":"Encryption", "speaker": speakers[4], "room":"alpha", "schedule": ("13.00", 55), "topic" : topics[4], "participants" : participants[0:8]},
            {"session title":"Sniffing", "speaker": speakers[0], "room": "beta", "schedule": ("14.00", 40), "topic" : topics[0], "participants" : participants[1:3]},
            {"session title":"Packet Capture", "speaker": speakers[1], "room": "gamma", "schedule": ("15.00", 40), "topic" : topics[1],  "participants" : participants[5:8]},
            {"session title":"User Sessions", "speaker": speakers[2], "room": "delta", "schedule": ("15.45", 45), "topic" : topics[2], "participants" : participants[1:4]}]

conference = {"Session" : sessions,  "Speakers" : speakers,  "Rooms:" : rooms, "Participants:" : participants, "Topics:" : topics}
#print(conference)


# Part 2 Working with schedule


#print("First Session:", sessions[0]["session title"], "Speaker of the 3rd session", sessions[2]["speaker"], "Last session Room: ", sessions[-1]["room"])
#print("Information about one selected session: ", sessions[1])
#print(f"First three sessions: \n{sessions[0]} \n{sessions[1]} \n{sessions[2]}")
#print(f"Last two sessions: \n{sessions[-2]} \n{sessions[-1]}")


reversed_schedule = sessions[::-1]
#reversed_schedule = sorted(sessions, key = lambda session : session["schedule"], reverse=True)
#print("Reversed schedule", reversed_schedule)

copied_session = sessions[0:4].copy()
#print("Copied Sessions:\n",copied_session)


# Part 3 Modifications


sessions[0]["room"] = "epsilon"
#print("First Sessions modified room:", sessions[0]["room"])

sessions[1]["speaker"] = "Morgan"
#print("Second Sessions modified speaker:", sessions[1]["speaker"])

new_session = {"session title":"Recap", "speaker": "Devon", "room": "zeta", "start time":"16.00.00","duration":15, "topic" : "Recap", "participants" : "3"}
sessions.append(new_session)
#print(sessions)

sessions.pop(2)
#print("Security session should be removed now:\n", sessions)

# As my data structure did not have participants in it, now I am modifying it to add them from my list. 

sessions[0]["participant"] = participants[0]
#print("\n", sessions[0])

sessions[0].pop("participant")
#print("\n", sessions[0])

difficulties = ["Beginner", "Intermediate", "Advanced"]
#print("\nSession 3 untouched:", sessions[2])
sessions[2]["difficulty"] = difficulties[2]

#print("\nSession 3 altered:", sessions[2])


# Part 4 Unique conference information

unique_conference_topics = set(conference["Topics:"])
#print(unique_conference_topics)

unique_technical_skills = conference.get("Unique Skills")
#print("Since unique skills were not present per any teacher nor a requirement, unique skills of teacher are:", unique_technical_skills)
#print("If this had to be done, I would just add a section, then call set(conference[\"Unique Skills\"]) as it would return me a set that I could print")


#print("Participants regirestered to both session 1 and 2", set(sessions[0]["participants"]) | set(sessions[1]["participants"]))

participants_in_both_sessions = set(sessions[0]["participants"]) & set(sessions[1]["participants"])
if participants_in_both_sessions:
    print("Participants in both session 1 and 2 are: ", participants_in_both_sessions)


#print("Participants regirestered to", sessions[0]["session title"], "are", sessions[0]["participants"])
#print("Whilst participants registere to", sessions[1]["session title"],"are", sessions[1]["participants"])


# Part 5 Unique conference information

conference_dates = [{"Year": 2026, "Month" : "September", "Day" : "Monday, the 22nd"},
                    {"Year": 2026, "Month" : "September", "Day" : "Wednesday, the 24th"},
                    {"Year": 2026, "Month" : "September", "Day" : "Friday, the 26th"}]

room_coordinates = [{"Wing": 'A', "Floor" : 5, "Room" : "F-6"},
                    {"Wing": 'B', "Floor" : 4, "Room" : "E-16"},
                    {"Wing": 'D', "Floor" : 3, "Room" : "G-26"}]

conference_contact_information = [ {"Person" : "Max Svensson", "Occupation" : "Chairman", "Contact" : "Max@conference.com"},
                                  {"Person" : "Husam Bowling", "Occupation" : "Secondary advisor", "Contact" : "Husam@conference.com"},
                                  {"Person" : "Ishtar Wise", "Occupation" : "Logistics expert", "Contact" : "Ishtar@conference.com"}]


separate_variable_for_max = conference_contact_information[0]["Person"]

#print(f"The conference is being held on {conference_dates[1]["Month"]}, {conference_dates[1]["Day"]} in the following location: {room_coordinates[2]}.")
#print(f"Should anyone require any additional information, please reach out to: {conference_contact_information[0]["Person"]}, at {conference_contact_information[0]["Contact"]}")


# Part 6 The shared-reference problem

#backup_participants = participants.copy()
#print("Copied data for backup_participants: ", backup_participants[2])
#backup_participants[2] = "Husam"
#print("Modified data for backup_participants", backup_participants[2])
#print("Original data for backup_participants", participants[2])

# Explanation. If one does not use .copy() when referencing the list, what python does is that it changes the values in both data structure.
# However, if one does use copy, then, in my understanding, we copy the values and keep the original list untouched. Hence, in this case, it is better to use .copy() to be safe.
# Or, in some cases, if we have a list of lists, we should use deepcopy(). Also, in this case, I used .copy() originally. If I remove it, then anything done to the 
# backup_participants is reflected on the participants data structure.


# Part 7 Restructure

better_structure_hopefully = [{"session_title" : "Python for AI", "speaker" : "Ada", "room" : "Room A"},
                    {"session_title" : "Building APIs", "speaker" : "Grace", "room" : "Room B"},
                    {"session_title" : "Introduction to LLMs", "speaker" : "Alan", "room" : "Room C"}]
#print("Second Session title:", better_structure_hopefully[1]["session_title"], "Speaker:", better_structure_hopefully[1]["speaker"], "Room:", better_structure_hopefully[1]["room"])
#print("Alternatively, we can print out the whole shabang:", better_structure_hopefully[1])


# Part Final Challenge

# For this given part, I beleive I can use everything I have define in the beginning of the file, my sessions, speakers, rooms, participants etc.
# For example, printing different things from my conference.

#print(f"Conference has this many rooms: {len(conference["Rooms:"])} and they are: {conference["Rooms:"]}")
#print(f"Session 2 title is: {conference["Session"][2]["session title"]} and its topic for today is {conference["Session"][2]["topic"]}")
#print("\n\n")
#print(f"Conference speakers are: {conference["Speakers"]}")
#print(f"Conference speaker for the session that starts at : {conference["Session"][2]["schedule"][0]} is {conference["Session"][2]["speaker"]}")
#print(f"Conference participants for session: {conference["Session"][4]["session title"]} are {conference["Session"][4]["participants"]}")

conference["Session"][4]["participants"] = participants[5:8]
#print(f"Now for session: {conference["Session"][4]["session title"]} I am changing participants to: {conference["Session"][4]["participants"]}")

#print(f"Similarly, conference session that starts at {conference["Session"][2]["schedule"][0]} will be changed to..")
conference["Session"][2]["schedule"] = ("17.00", 30)
#print(f"New start time for session {conference["Session"][2]["session title"]} is {conference["Session"][2]["schedule"][0]}")

print("\n\n")
conference.pop("Rooms:")
#print("Now the conference structure is missing the list of rooms, however, they are displayed in the session information.",conference)
#print("\nThis means the given operation should return us false/none", conference.get("Rooms:"), "which it does. Beautiful.")

#print("\n\n")
conference.update({"Rooms:":rooms})

print("\nNow rooms have been added back, however, do note that when using an update or append, added items go back to the end of the structure\n",conference)


# Design explanation
# 10. I used lists in pretty much every structure since when making a massice data set, it is easier to "glue" different elements together
# with their designated name. Suitable since room names should be unique.

# 11. Dictionary I used for conference, since it is easier to combine many elements under a "key" so to say. Same for session data,
# I made a list of dictionaries. It was suitable so that later on when i need to edit or get data, it would make things easier.

# 12. I used tuple on time and duration. To be honest, I really did not want it but sicne it was a requirement, I made them together.
# It was suitable since you combine both the time, and the duration. Initially, in my original commit, I had it separate, but now I got to this section
# so I had to change it :) 

# 13. Set I put pon the rooms. They are unique. I could put it on topics too but I thought having rooms is enough. Suitable due to I do not want to have duplicates.

# 14. Primary lists and dictionaries are mutable since we had to do changes there.

# 15. Rooms, or schedules. Even though I modified it, but the modification was a full replace, not one specific element of that tuple right. Hence the code compiled.

# 16. Nested collections are good to keep data sorted I would say. If you need something, you can quickly loop through, which we were not allowed to do here, to get what you need.

# 17. I think in our case since conference had sessions which was a list of dictionaries, it becomes quite messy if you are working loopless, or accessing elements like
# I did here - conference["Session"][2]["schedule"][0] - this is definitely a bit of ugly code. I think I would get a -1 on this for review. 

# 18. Ah, good question! When you assining one list to another, both of your variables point to the same place in memory, hence, when doign a change,
# both the original and the "copy" is altered. When copying, you modify only one data type, that has been copied, the original stays in tact.

# 19. Let me use loops to remove some of the nested sections. Lambda function, I used it but commented it out, line 29. of course, it would be better to introduce methods here,
# and eventually a class, to keep things straight.