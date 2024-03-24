import spacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm')

rules = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    # "logo of spmvv":("Here is a logo of spmvv","spmvv-logo.jpg"),
    "Sri Padmavati Mahila Visvavidyalayam or Women's University or SPMVV": ["This is a women's university founded in 1983, accredited with four stars with 'Grade A+' by the National Assessment and Accreditation Council (NAAC) and International Certificate ISO."],
    "how are you": ["I am good, thank you!", "I am doing fine, thanks!"],
    "what courses do you or SPMVV offer or offered or offers": ["This year the University offers 59 variety of courses including Computer Science, Business, and Engineering."],
    "admissions": ["For admissions information, please visit our website or contact the admissions office."],
    "mca or computer science or applications": ["The Computer Science Department offers MCA Course since 1987. It also offers Ph.D./M.Phil. Research programme."],
    "computer science or applications or mca seats": ["Regular Seats: 44 and SelfFinance Seats: 66"],
    "computer science or applications or mca eligibility": ["Admissions are made through Integrated Common Entrance Test (ICET) conducted by A.P. State Council of Higher Education, Hyderabad."],
    "Applied Mathematics , M.Sc. or MSc Apllied Mathematics or Mathematics and duration and pattern": ["The department offers M.Sc. Applied Mathematics(2Years(4 Semesters)) programme since 1984.The curriculum designed under CBCS pattern."],
    "Applied Mathematics , M.Sc. or MSc Applied Mathematics total Seats":["Regular Seats:35+4(EWS) ,PaymentSeats(06)"],
    "Applied Mathematics , M.Sc. or MSc Applied Mathematics Eligibility":["B.A. / B.Sc. Degree with Mathematics as one of the optional subjects, with 50 percentage in Mathematics. Candidates who have studied Mathematics as an ancillary subject are not eligible."],
    "Applied Microbiology, M.Sc or MSc Applied Microbiology Duration and Pattern":["It is a 2Years(4 Semesters) pattern"],
    "Applied Microbiology, M.Sc or MSc Applied Microbiology Seats":["RegularSeats:15 and Payment Seats 15"],
    "Applied Microbiology, M.Sc or MSc Applied Microbiology Eligibility":["B.Sc. Degree with Chemistry/Biochemistry at least 50 percentage on the aggregate with Microbiology."],
    "M.Sc Biotechnology":["The department was established in the year 2002, it offers M.Sc., Biotechnology (2Y), M.Sc., Integrated Biotechnology (5Y) and M.Phil/Ph.D. programmes."],
    "M.Sc Biotechnology  Total Seats":["Payment Seats: 30.There is no Regular Seats"],
    " M.Sc Biotechnology Eligibility":["Bachelor's Degree with Chemistry/Biochemistry/ Botany/ Zoology/ Biotechnology/ Microbiology/Genetics/Medical Lab Technology/Applied Nutrition/ Bioinformatics and Computer Applications and minimum of 50 percentage in group aggregate marks."],
    "Home Science courses offer":["The Department of Home Science offers:M.Sc Integrated Food Technology (5year), M.Sc. Food and Nutrition sciences (Three specialisations),M.Sc. Human Development and family Studies(HDFS),M.Phil and Ph.D.,Bachelor of Vocational Programmes "],
    "M.Sc Integrated Food Technology Duration":["5 years(10 semesters)"],
    "M.Sc Integrated Food Technology (5year) Total Seats":["RegularSeats;40+4(EWS).There is no payment seats for it"],
    "M.Sc Integrated Food Technology (5year) Eligibility":[" Bi.P.C/ M.P.C group in Intermediate with 55% marks"],
    "M.Sc. Food and Nutrition sciences with Three specialisations Duration":["2 years(4 semesters) with specialisations(Clinical Nutrition and Dietetics(CND),Community Health and Nutrition (CHN),Food Science and Quality Control (FSQC) )"],
    "M.Sc. Food and Nutrition sciences Total Seats":["Regular Seats:30 and Payment Seats:6"],
    "M.Sc. Food and Nutrition sciences Eligibility":[" B.Sc. Home Science, B.Sc. Applied Nutrition, B.Sc. Rural Home Science, B.Sc. Clinical Nutrition and Dietetics, B.Sc. Food Science and Quality Control, General B.Sc. With Nutrition as one paper, BHSC (4 years) with 50% marks in groups."],
    "M.Sc. Human Development and family Studies(HDFS) Duration or Pattern":["2 years (4 semesters)"],
    "M.Sc. Human Development and family Studies(HDFS) Total Seats":["Regular Seats:15 and Payment Seats:6"],
    "M.Sc. Human Development and family Studies(HDFS) Eligibility":["Any Graduate including B.Sc Nursing with 50% marks in groups."],
    "Bachelor of Vocational Programmes or B.Voc.":["University offering two Programmes viz., B.Voc. Nutrition and Health Care Sciences (NHCS) and B.Voc. Fashion Technology and Apparel Designing (FTAD)."],
    "B.Voc. Fashion Technology and Apparel Designing Duration and pattern":["3 years(6 semesters)"],
    "B.Voc. Fashion Technology and Apparel Designing Total Seats":["Regular Seats:50.There is no payment seats"],
    "B.Voc. Fashion Technology and Apparel Designing Eligibility":["Any group in Intermediate with 45% marks"],
    "B. Voc. Nutrition and Health Care Sciences Duration and pattern":["# years(6 semesters)"],
    "B. Voc. Nutrition and Health Care Sciences Total Seats":["Regular Seats:50 and there is no payment seats"],
    "B. Voc. Nutrition and Health Care Sciences Eligibility":["Any group in Intermediate with 45% marks."],
    "M.Sc. Organic Chemistry Duration and pattern":["The Department of Organic Chemistry was established in the year 2006.It is a 2Years(4 semesters) programme."],
    "M.Sc. Organic Chemistry Total Seats":["RegularSeats:120 and PaymentSeats:12"],
    "M.Sc. Organic Chemistry Eligibility":["B.Sc. 3 year degree/ 4 year degree programme with Chemistry as one of the subjects in the combination and the candidates should have secured at least 50% marks in the aggregate, in B.Sc. degree."],
    "M.Sc. Physics (Self Finance)":["The department of physics established in the year of 2004, offers M.Sc Physics with intake of 60.It is a 2Years(4 semesters program)"],
    "M.Sc. Physics (Self Finance) Total Seats":["PaymentSeats:60 and EWS:06"],
    "M.SC. Physics (Self Finance) Eligibility":["B.Sc. Degree with Physics, Mathematics and other subjects with 50 percentage of marks on the aggregate."],
    "Department of Biosciences and Sericulture":["It is etablished in the year 1983 provides master's in Sericulture, Botany, Zoology"],
    "M.Sc. Sericulture Duration and pattern":["2Years(4 semesters)"],
    "M.Sc. Sericulture Total Seats":["Regular Seats:10+1(EWS) only"],
    "M.Sc. Sericulture Eligibility":["B.Sc. With any two of the following subjects Sericulture / Agriculture / Horticulture / Forestry / Zoology / Botany / Chemistry / Home Science / Clinical / Pathology / Microbiology / Biochemistry / Genetics / Molecular / Textiles / Biology / Biotechnology / Entomoloy / Medical Lab Technology. The candidates should have secured at least a II class with 50%  marks in groups "],
    "M.Sc. Botany Duration and Pattern":["2 Years(4 semesters)"],
    "M.Sc. Botany Total Seats":["Payment Seats:30 + 3(EWS) only"],
    "M.Sc. Botany Eligibility":["B.Sc. Degree, Botany with Chemistry / Biochemistry as Compulsory subjects and with 50%  marks on an average in the group"],
    "M.Sc. Zoology Duration and Pattern":["2 Years(4 semesters)"],
    "M.Sc. Zoology Total Seats":["Payment Seats:30+3(EWS) only"],
    "M.Sc. Zoology Eligibility":["B.Sc. Degree with Zoology as one of the subjects in Part-II. The candidates should have secured at least a II class With 50% marks in Zoology and 50% marks in aggregate."],
    "M.Sc Statistics Duration and Pattern":["The Department of Statistics was established in 2014. The Department offers a two years(4 semesters) Master’s Programme in Statistics."],
    "M.Sc Statistics Total Seats":["RegularSeats:50+5(EWS)"],
    "M.Sc Statistics Eligibility":["B.A. / B.Sc. with Statistics and Mathematics as main subjects (in all the three years) on average of 50% marks."],
    "M.Sc. Clinical Psychology (Self-Finance) Duration and Pattern":["The Department of Psychology was established in the academic year 2020-2021 which is a 2Years (4 semesters ) programme"],
    "M.Sc. Clinical Psychology Total Seats":["Regular Seats:30 and Payment Seats:05"],
    "M.Sc. Clinical Psychology Eligibility ":["B.A. Psychology / B.Sc. Psychology /B.Sc. Home science/ Social work (BSW)/ Physiotherapy (BPT)/ B.Sc. Nursing /B.Ed. with Psychology as one subject on average of 50% marks.Through SPMVV CET"],
    "About Business Management Duration and Pattern":["It provides mainly two courses:Masters of Business Management and Master of Commerce.2Years(4 semesters)"],
    "Masters of Business Management and Master of Commerce Duration and Pattern":["2Years(4 semesters)"],
    "Master of Commerce Total Seats":["RegularSeats:60 only"],
    "Masters of Business Management Total Seats":["Regular Seats:120 only"],
    "Master of Commerce Eligibility":[" Bachelor's Degree of any recognized University. Students should qualify through the University level Common Entrance Test (SPMVVPGCET)"],
    "Communication and Journalism Duration and Pattern":["It provides mainly two programmes:Master’s Programme in Communication and Journalism (MCJ),Master’s of Bussiness management (MBA) in media Management.Time period is 2Years(4 semesters)"],
    "Master’s Programme in Communication and Journalism (MCJ) Total Seats":["Regular Seat:20"],
    "Master’s of Bussiness management (MBA) in media Management Total Seats":["RegularSeats:30 and PaymentSeats:30"],
    "Master’s of Bussiness management (MBA) in media Management Eligibility":["Bachelor Degree of any recognized University and should qualify APICET"],
    "Master’s Programme in Communication and Journalism (MCJ) Eligibility":[" Any graduate with 45% the aggregate"],   
    "Education Department":["The Department of Education offers Pre Service Teacher Education Programs for candidates aspiring to take up teaching profession."],
    "English Language and Literature":["The M.A. program in English is offered by the department."],
    "M.A. English Duration and Pattern":["2Years(4 Semesters)"],
    "M.A. English Total Seats":["RegularSeats:30 and Payment Seats:06"],
    "M.A. English Eligibility":[" Any Graduate with 45% marks in Special English / in General English."],
    "Law":["This department provides three programmes: Master's Programme in Law(LL.M),Three Year Degree Course In Law(LL.B. 3YDC),Five Year Degree Programme In Law (LL.B. 5YDC)"],
    "Master's Programme in Law ( LL.M ) Duration and Pattern and Total seats":["2Years(4 semesters), 8 per batch"],
    "Master's Programme in Law ( LL.M ) Eligibility":[" Pass in 3/5 years Degree Course in Law of any recognized University with 40%  the aggregate."],
    "Three Year Degree Course In Law ( LL.B. 3YDC ) Duration Pattern Total Seats":["3Years(6 Semesters) and 40 Regular Seats(minimum 10)"],
    "Three Year Degree Course In Law ( LL.B. 3YDC ) Eligibility":[" Graduate of any recognized University with 45%  the aggregate and qualified in Common Entrance Test, i.e., LAWCET conducted by the Government of Andhra Pradesh. Centralised Admission will be made by the Convener, on the basis of rank obtained in the Entrance Test."],
    "Five Year Degree Programme In Law ( LL.B. 5YDC ) Duration Pattern Total Seats":["5 Years(10 Semesters) and RegularSeats 40(minimum 10)"],
    "Five Year Degree Programme In Law ( LL.B. 5YDC ) Eligibility":["10+2 or Intermediate with 45% the aggregate and is qualified in the 5 Year Common Entrance Test, i.e., LAWCET conducted by the Govt. of Andhra Pradesh. Centralised Admissions will be made by the Convener,on the basis of rank obtained in the Entrance Test."],
    "Music Dance and Fine arts Department courses":["The Department provides M.A.Music, M.A.in Bharathanatyam, M.A.in Performing Arts,Evening Programmes,Ph.D."],
    "M.A. Music Duration and Pattern":["2 Years(4 semesters)"],
    "M.A. Music Total Seats":["Regular Seats 10(Each in Veena & Vocal)"],
    "M.A. Music Eligibility":["Any recognized Degree with Vocal Music / Veena Music as one of the main subjects / any recognized Degree with a Diploma / Certificate in Vocal Music / Veena Music or equivalent / any recognized Degree with a grading in Vocal / Veena in Classical Music Audition Board of All India Radio."],
    "M.A. in Bharathanatyam Duration and Pattern":["2Years(4 Semesters)"],
    "M.A. in Bharathanatyam Total Seats":["Regular Seats:10"],
    "M.A. in Bharathanatyam ":["Any Bachelor degree with Natya Visarada / Govt. Certificate / Diploma Praveena / equivalent oriental Title Degree / B Grade / training under Guru and performance in the interview of SPMVV. Any Degree + One of the above dance courses (or) Bachelors Degree in Dance."],
    "M.A. in Performing Arts Duration and Pattern":["5 Years (Integrated). Music and Dance in first three years, Vocal/ Veena/ Bharatanatyam specialization in next two years."],
    "M.A. in Performing Arts Eligibility":["Students with Intermediate/ +2 / higher secondary. Students with degree and training under a guru are eligible for admission directly into 4th year."],
    "Evening Programmes in Music Dance Fine Arts Department Duration and Pattern":["2Years(4 Stages).50 Hours(Each Stage)"],
    "Evening Programmes in Music Dance Fine Arts Department Eligibility":["The certificates will be issued to the students after the completion of 2 years certificate course by the university"],
    "Physical Education Department":["The Department promotes two programmes:Bachelor's Programme in Physical Education (B.P.ED) (Self Finance) and Master Programme in Physical Education (M.P.ED)(Self Finance"],
    "Bachelor's Programme in Physical Education ( B.P.ED ) (Self Finance) duration Pattern Total Seats":["2 Years(4 Semesters) Intake Seats 100"],
    "Bachelor's Programme in Physical Education ( B.P.ED ) (Self Finance) Eligibility":["Must have passed a Bachelor Degree from any University and Qualified the Physical Education Common entrance Test conducted by Andhra Pradesh State Council of Higher Education, Government of Andhra Pradesh"],
    "Master Programme in Physical Education ( M.P.ED ) (Self Finance) duration Pattern Total Seats":["2 Years(4 Semesters) Intake Seats:40"],
    "Master Programme in Physical Education ( M.P.ED ) (Self Finance) Eligibility":["The admission for the degree of M.P.Ed. Degree shall be open to. The candidates who complete B.P.Ed Degree programme of any University recognized by UGC are eligible for admission provided that they possess a minimum of 50 Percentage of marks in B.P.Ed programme. Concessions in the eligibility for reservation categories as per Government norms and should qualify in SPMVV PGCET"],
    "Master of Social Work ( MSW ) Department duration pattern ":["2 years(4 Semesters)"],
    "Master of Social Work ( MSW ) Department Total Seats":["RegularSeats:30 and Payment Seats:18"],
    "Master of Social Work ( MSW ) Department Eligibility":["Any Graduate – graduates with 45% the aggregate in group for Arts and 50% the aggregate group for Science graduates. In a given class, among the applicants, preference will be given to Social Work graduates"],
    "M.A. Telugu Language, Literature and Translation Duration Pattern Total Seats":["2 Years(4 Semesters) Regular Seats:40 and Payment Seats:06"],
    "M.A. Telugu Language, Literature and Translation Eligibility":["Any graduate with 40 Marks in General Telugu.Preference will be given to special Telugu, BAOL/ sastri"],
    "Women's Studies Department":["This department provides M.A. Women Studies (old) M.A. in Gender Studies(Since 2021-22) and M.A. Economics"],
    "M.A. Women Studies ( old ) M.A. in Gender Studies ( Since 2021-22 ) Duration pattern Total Seats":["2 Years (4 Semesters) .Regular Seats:25"],
    "M.A. Women Studies ( old )M.A. in Gender Studies ( Since 2021-22 ) Eligibility":["Graduate with: 45 pecentage in the subject concerned if it exists at graduate level.45%  the aggregate in groups for Arts and Science Graduates including B.Tech, BBA. There is 5 percent relaxation to SC and ST Students to eligibility criteria"],
    "M.A. Economics Duration Pattern Total Seats":["2 Years(4 Semesters). Regular Seats:25"],
    "M.A. Economics Eligibility":["Any gradate with B.A. with 45percentage and B.Sc. with 50 percentage in groups. They should have studied at least one of the following subjects in their UG course: Economics, Mathematics, Statistics, Accountancy, Computer Science. B. Com/BBA with 45percentage of the aggregate in groups.B. Tech (Any Branch) with 60% marks on the aggregate.There is 5percent relaxation to SC and ST Students to eligibility criteria"],
    "SCHOOL and College  OF NURSING ":["SPMVV provides General Nursing and Midwifery (GNM) under School Of Nursing and B.Sc Nursing under College of Nursing"],
    "B.Sc Nursing 4 Year Degree Course Total Seats":["This is a 4 years degree course with allocated seats 40"],
    "B.Sc Nursing 4 Year Degree Course Eligibility":["Minimum age for admission shall be 17 years as on before 31st December of the year of admission. Minimum education requirement shall be passing of 10+2 years course with biological sciences or an equivalent of 10+2 years course recognized boards with science (Bi.P.C) and English with minimum 45 percentage aggregate marks.10+2 vocational with bridge course under CBSE Board or other equivalent board from the school and recognized by Indian Nursing Council."],
    "General Nursing and Midwifery ( GNM ) 3 Years Diploma Course Total Seats":["This is a 3 Years diploma course with allocated seats:40"],
    "General Nursing and Midwifery ( GNM ) 3 Years Diploma Course Eligibility":[":Minimum and maximum age for the admission will be 17-35 years respectively."],
    "Institute of Pharmaceutical Technology":["This provide two main programmes:M. Pharmacy, Self Finance and B. Pharmacy"],
    "Bachelor's Programme in or B Pharmacy   Duration and Pattern Total Seats ":["This is a 4 years course with Regular seats: 40"],
    "Bachelor's Programme in or B Pharmacy  Eligibility":["A Pass certificate in the Intermediate Examination/Higher Secondary Certificate (Multipurpose). Pre-University science course with Bi.P.C. M.P.C. and qualification in EAMCET Examination. Selection and allotment of seats will be made by the competent authority on the basis of EAMCET ranking in the ratio of 20:20 for M.P.C., Bi.P.C. Students Four students with D.Pharm qualification and based on ECET- 11 rank will be directly admitted to II B.Pharmacy."],
    "Master's Programme in or M Pharmacy Duration and pattern":["2 years(4 semesters)"],
    "Master's Programme in or M Pharmacy Total Seats":["No.of Seats in Pharmaceutical Chemistry : 15 Pharmaceutical Analysis : 15 Pharmacology : 15 Pharmaceutics : 15 Pharmacognosy : 6"],
    "Master's Programme in or M Pharmacy Eligibility":["B.Pharmacy Degree with a minimum of 50% marks on the Aggregate. The Admission is based on a valid GPAT Score/PGECET."],
    "SCHOOL OF ENGINEERING AND TECHNOLOGY":["This offers Programmes: B.Tech(Bachelor of Technology), M.Tech(Masters in Technology), PhD(Doctor of Philosophy)"],
    "B.Tech or Bachelor of Technology":["Departments under B.Tech:CSE(Computer Science and Engineering),ECE(Electronics & Communication Engineering),EEE(Electrical & Electronics Engineering),Mechanical Engineering,Basic Sciences & Humanities"],
    "Placements in SPMVV or Sri Padmavati Mahila Visvavidyalayam or Women's University and salary package for students or student":["Starting from the First year, Placement Cell Organizes Career Guidance Programs and Campus Recruitment Training Programs such as Mock Interviews, Group Discussions, Communication Skills, Technical Skills, Workshops, etc., for all the Students.We also invite HR executives from various Industries to Conduct Training Programs.The maximum salary package has exceeded notably from 3.36 LPA to 10 LPA."],
    "How to contact placement cell":["Phone:0877-2284554 and mail:placement.spmvv@gmail.com or placement@spmvv.ac.in"],
    "Centers or center in SPMVV or Sri Padmavati Mahila Visvavidyalayam or Women's University":["In this university we have Research Center and UGC Center"],
    "What is Research Center ":["DST CURIE , DST CURIE-AI and TRICA comes under Research Centers"],
    "What is UGC Centers":["Central Networking Facility (CNF), Computer Center, EDCELL, Entry into Services, UGC NET Coaching Center, Women's Studies Center comes under UGC Centers."],
    "DST  CURIE Center":["DST CURIE Center was established as a Central Instrumentation facility for the Science Departments of Sri Padmavati Mahila Visvavidyalayam supported by Department of Science and Technology. Govt. of India.This Central Instrumentation facility is located in ground floor of Kalapana Chawla Science block"],
    "DST CURIE AI Center":["DST- CURIE-AI center, Sri Padmavati Mahila Visvavidyalayam (SPMVV) was established to promote Artificial Intelligence (AI), Augmented Reality (AR) and Internet of Thing (IoT) concepts in diverse fields like Agriculture, Science, Medicine, Law, Humanities and Engineering."],
    "TRICA":[" Sri Padmavati Mahila Visvavidyalayam (SPMVV) has come up with the special initiative called, “Trans disciplinary Research Initiative Centre for Adolescent Health” (TRICA). The overall objective of TRICA is to establish a centre and to build capacities of post graduate students, research scholars and young faculty to carry trans disciplinary research in the context of adolescent health."],
    "Central Networking Facility or Command Control Center or CNF":["This  was established in the year 2017, keeping in view of bringing all the technical and Software activities under one umbrella. "],
    "Activities or Activity of CNF ":["Activities of CNF: Data center,Website,Biometric Devices,Video Conference,Digital Class Room, LIVE Studio, IP Based Cameras,Payment Gateway, University Computerization, WhatsApp Group"],
    "Computer Center Timings time in SPMVV or Sri Padmavati Mahila Visvavidyalayam or Wome's University ":["The University Computer Centre was established in 1986 with an aim to facilitate, Students, Research Scholars, Teaching, and Non-Teaching faculty with all the infrastructure facilities. The Computer Centre is functioning from 8 AM to 6 PM on all working days."],
    "What is Entry into Services or Service":["It is a UGC Scheme for Entry Into Services for SC/ST OBC (Non-Creamy layer) Minority Community StudentsThe Coaching Classes are arranged for different competitive exams to the students belong to SC/ST/OBC & Minorities students. "],
    "UGC NET Coaching Center":["The UGC NET Coaching Centre for SC, ST, BCs and Minorities provides coaching for the SC/ST and Minority Community candidates for appearing in the National Educational Testing (NET)"],
    "":[""],   
    # Add more keyword-based rules as needed
}


def get_response(message):
    message = message.lower()
    # Tokenize the user input
    tokens = [token.text.lower() for token in nlp(message)]
    print("User Tokens:", tokens)
    
    max_match = 0
    response = "I'm sorry, I don't understand that."
    
    for keyword, responses in rules.items():
        keyword_tokens = keyword.lower().split()
        match_count = sum(1 for token in keyword_tokens if token in tokens)
        if match_count > max_match:
            max_match = match_count
            response = responses[0]
            print("Matched Keyword:", keyword)
            print("Match Count:", match_count)
            if len(responses) > 1:  # Check if an image path is provided
                image_path = responses[1]
    if max_match == 0:
        print("No Match Found")
    
    return response
