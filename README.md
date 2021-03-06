# Marekt Driven Career Dashboard for Lebanese Students
Selecting the right career is one of the most important decisions students have to make. With the increase in the number of career paths and opportunities, making this decision have become quite difficult. The purpose of this project is to do a job market analysis in Lebanon to provide information about different job trends in Lebanon up-to-date to Lebanese students, so they could form better career choices. Since many Lebanese students don’t know which major to choose and which job position is highly demanded in Lebanon, this project guides them in their career choice.  The problem in Lebanon is that there’s no available data about the job market in Lebanon. Thus,  I scrapped different websites to get information about job market trends in Lebanon and information about job professions as well. The design and methodology and methodology of this project is to scrape data about all job positions in Lebanon on LinkedIn, then clean and preprocess the data, turn it into a csv file then present it as visual graphs on a dashboard on Streamlit WebApp. Next, scrape data about job professions from O*net website to get information about different job professions. Then, clean and preprocess the data and present it as visual graphs on Streamlit WebApp. The major findings of this project were that the most demanded job position in Lebanon are manager and software engineer, the top hiring company is Toptal and Agoda, the city with the most job openings is Beirut. This project doesn’t only benefit Lebanese students and help them choose the right career for them, but also, it helps Lebanon’s economy. When worker’s skills and qualifications fit demanded jobs in the country then that increases productivity and boosts economic growth.   


Here's the link for the Streamlit WebApp: https://share.streamlit.io/lunabaalbaki/career-guide-dashboard-for-lebanese-students/main/final_capstone.py

Infromation about the above files:

**Luna Baalbaki - MSBA Capstone Final Report - 201802512.pdf**
is a detailed report about the whole "Marekt Driven Career Dashboard for Lebanese Students" project. It contains introduction, background infromation, methedology, resutls, discussion and conclusion. 

**final_capstone.py:** 
is the python file for the Streamlit WebApp. It is the file that I used for the public deployment. 

**preprocessed_linkedin_jobs_25_08_21.csv**
is the CSV file that contains data that I scrapped from LinkedIn about date, location, job title, company of all job positions in Lebanon. Guide on how I scrapped this data is found in linkedin_jobs_in_lebanon_21.ipynb notebook. 

**tasks.csv**
is the CSV file that I scrapped from O*net website about tasks of different professions: https://www.onetonline.org/

**detailed_work_activities.csv:**
is the CSV file that I scrapped from O*net website about detailed work activities of different professions: https://www.onetonline.org/

**skill_importance.csv**
is the CSV file that I scrapped from O*net website about skills of different professions: https://www.onetonline.org/

**bright_outlook_onet.csv**
is the CSV file that I scrapped from O*net website about bright outlook of different professions: https://www.onetonline.org/

**header1.jpg**
is a picture used as a header in the Streamlit WebApp

**line_seperator**
is a picture used as a header in the Streamlit WebApp

**README.md**
is a description of the "Marekt Driven Career Dashboard for Lebanese Students" GitHub project. 

**requirements.txt**
is a txt file that contains the library used. 

