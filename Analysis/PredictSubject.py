import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV

# Sample labeled data (You can replace this with your actual dataset)
data = [
    ("Which of the following is the largest inhabited riverine island in the world?", "Geography"),
    ("In the Right-Hand Thumb Rule, the thumb is directed towards the direction of:", "Physics"),
    ("Which of the following illustrations is related to chloroplasts?", "Biology"),
    ("Which is the most important protein component in milk, both quantitatively and nutritionally, that accounts for about 80% of the total protein in bovine milk?", "Biology"),
    ("Which web portal was launched by the Department of Telecommunications for sharing information on mobile towers and EMF emission compliance?", "Government Schemes"),
    ("Which of the following is Fisher's equation of exchange?", "Economy"),
    ("In 1539, the Battle of Chausa was fought between Humayun and:", "Indian History"),
    ("Sardhana Christian Fair is held in which of the following states?", "Indian Geography"),
    ("Ali Akbar Khan was associated with which of the following gharanas?", "Music"),
    ("Which Article of the Indian Constitution mentions that 'The State shall endeavour to promote cottage industries on an individual or co-operative basis in rural areas'?", "Indian Constitution"),
    ("Which of the following is the most controversial Article in the Indian Constitution, which provides for President's rule in any state?", "Indian Constitution"),
    ("A dense mass of water drops on smoke or dust particles in the lower atmosphere layers is referred to as:", "Environmental Science"),
    ("Bhakti Pradeep Kulkarni is associated with:", "Sports"),
    ("Who among the following was the youngest recipient of the Sangeetha Kalanidhi awarded by the Music Academy in 1947?", "Music"),
    ("In which year was the battle of Buxar fought?", "Indian History"),
    ("Which of the following State governments has launched a scheme 'Ankur' in May 2021 to promote planting of trees in public, wherein people will be awarded for planting and taking care of the saplings?", "Government Schemes"),
    ("Which of the following Acts passed under Warren Hastings was also called 'half-loaf system'?", "Indian History"),
    ("In Newlands' Octaves, the properties of lithium and:", "Chemistry"),
    ("India hosted the Asian Games in which of the following years?", "Sports"),
    ("Which of the following movements created regional disparities between large and small farmers in India?", "Agriculture"),
    ("What was the main objective of the Second Green Revolution in India?", "Agriculture"),
    ("Which of the following Articles of the Indian Constitution CANNOT be suspended even during an emergency declared on the grounds of war or external aggression?", "Indian Constitution"),
    ("Elelakkaradi dance of Kerala is performed by which of the following tribes?", "Culture & Tribal Affairs"),
    ("Who among the following Indian classical dancers is associated with Kuchipudi?", "Indian Classical Dance"),
    ("How many ICC World Cups has India won in ODI?", "Sports"),
    ("With reference to Ajivikas, consider the following statements.", "Indian History"),
    ("Who first stated the principle of refraction that postulates that every substance has a specific bending ratio - 'refractive index'?", "Physics & Chemistry"),
    ("Who among the following was appointed as the Chief Economic Advisor (CEA) to the Indian government in 2022?", "Economy & Government Schemes"),
    ("Which Article in the fundamental duty is invoked when you see in a private party that the Indian flag has been used as a covering for the speaker's desk?", "Indian Constitution & Law"),
    ("Kati Bihu is celebrated in which of the following months in Assam?", "Geography & Climate"),
    ("Coir conductor Coomi Nariman Wadia was awarded with which of the following awards by the Government of India in 2023?", "General Knowledge"),
    ("What is the gas evolved when zinc reacts with sulphuric acid?", "Physics & Chemistry"),
    ("Name the pension scheme that seeks to ensure old age protection for unorganised workers.", "Economy & Government Schemes"),
    ("Who published Systema Naturae in 1735 classifying the three kingdoms of nature and outlining the sexual system for the classification of plants?", "General Knowledge"),
    ("In 2022, who has been appointed as new Attorney General of India?", "Indian Constitution & Law"),
    ("The most common rainfall measurement is the total rainfall depth during a given period, which is expressed in", "Geography & Climate"),
    ("Which of the following is NOT a kharif crop?", "Geography & Agriculture"),
    ("Which of the following statements about the second five-year plan is INCORRECT?", "Indian History & Politics"),
    ("Being the President of the Indian National Congress, who among the following had called for complete independence from the British Raj in 1929?", "Indian History & Politics"),
    ("In 1936, The Independent Labour Party was founded by", "Indian History & Politics"),
    ("Which of the following Sultans of Delhi primarily adopted a policy of consolidation rather than expansion?", "Indian History & Politics"),
    ("Who is often touted as Tansen of the 20th century, this musical genius blended the best of classical music and created a unique style of his own?", "Indian Classical Dance & Music"),
    ("Which of the following is the largest inhabited riverine island in the world?", "Geography"),
    ("In the Right-Hand Thumb Rule, the thumb is directed towards the direction of:", "Physics"),
    ("Which of the following illustrations is related to chloroplasts?", "Biology"),
    ("Which is the most important protein component in milk, both quantitatively and nutritionally, that accounts for about 80% of the total protein in bovine milk?", "Biology"),
    ("Which web portal was launched by the Department of Telecommunications for sharing information on mobile towers and EMF emission compliance?", "Technology & Government Schemes"),
    ("Which of the following is Fisher's equation of exchange?", "Economy"),
    ("In 1539, the Battle of Chausa was fought between Humayun and:", "Indian History"),
    ("Sardhana Christian Fair is held in which of the following states?", "Indian Geography"),
    ("Ali Akbar Khan was associated with which of the following gharanas?", "Music"),
    ("Which Article of the Indian Constitution mentions that 'The State shall endeavour to promote cottage industries on an individual or co-operative basis in rural areas'?", "Indian Constitution"),
    ("Which of the following is the most controversial Article in the Indian Constitution, which provides for President's rule in any state?", "Indian Constitution"),
    ("A dense mass of water drops on smoke or dust particles in the lower atmosphere layers is referred to as:", "Environmental Science"),
    ("Bhakti Pradeep Kulkarni is associated with:", "Sports"),
    ("Who among the following was the youngest recipient of the Sangeetha Kalanidhi awarded by the Music Academy in 1947?", "Music"),
    ("In which year was the battle of Buxar fought?", "Indian History"),
    ("Which of the following State governments has launched a scheme 'Ankur' in May 2021 to promote planting of trees in public, wherein people will be awarded for planting and taking care of the saplings?", "Government Schemes"),
    ("Which of the following Acts passed under Warren Hastings was also called 'half-loaf system'?", "Indian History"),
    ("In Newlands' Octaves, the properties of lithium and:", "Chemistry"),
    ("India hosted the Asian Games in which of the following years?", "Sports"),
    ("Which of the following movements created regional disparities between large and small farmers in India?", "Agriculture"),
    ("What was the main objective of the Second Green Revolution in India?", "Agriculture"),
    ("Which of the following Articles of the Indian Constitution CANNOT be suspended even during an emergency declared on the grounds of war or external aggression?", "Indian Constitution"),
    ("Elelakkaradi dance of Kerala is performed by which of the following tribes?", "Culture & Tribal Affairs"),
    ("In which year was Project Tiger launched in India?", "Indian History"),
    ("Details about Sudarshana lake is given in a rock inscription at Girnar (Junagarh), which was composed to record the achievements of the Shaka ruler.", "Indian History"),
    ("Who among the following formed the Bihar Provincial Kisan Sabha in 1929?", "Indian History"),
    ("Mahendravarman I was the ruler of which of the following dynasties?", "Indian History"),
    ("Who founded the Prarthana Samaj in Mumbai in 1867?", "Indian History"),
    ("Which plateaus are very fertile because they are rich in black soil that is very good for farming?", "Indian Geography"),
    ("When the analysis of population density is done by calculating it through net cultivated area, then the measure is termed as:", "Indian Geography"),
    ("Which of the following statements best defines the monoecious?", "Science and Technology"),
    ("Which of the following decomposition reactions is NOT a redox reaction?", "Science and Technology"),
    ("Which of the following is a correct order of basicity?", "Science and Technology"),
    ("Which of the following pairs is INCORRECT regarding the grade of organisation and its example?", "Science and Technology"),
    ("What challenge does foreign investment often face in India?", "Indian Economics"),
    ("Which of the following states is the biggest producer of Pulses?", "Indian Economics"),
    ("Which article has a similar provision to that of Article 32 and deals with writ jurisdiction?", "Indian Politics"),
    ("Which of the following is NOT a condition for the President's office in India?", "Indian Politics"),
    ("Mohan Veena player, Pandit Vishwa Mohan Bhatt won the Award in the year 1994.", "Sports"),
    ("The head office of Board of Control for Cricket in India (BCCI) is located in:", "Sports"),
    ("In which city was the first golf club of India situated?", "Sports"),
    ("Who is Union Minister of State (Independent Charge) for Science and Technology as of July 2023?", "Current Affairs"),
    ("Who is the Chief Minister of Tamil Nadu as of July 2023?", "Current Affairs"),
    ("Which Indian among the following has his name in Time Magazine's list of '100 most influential people of 2021'?", "Current Affairs"),
    ("The first southern campaign of Alauddin Khilji in 1307-08 AD was led to which of the following regions?", "Indian History and Politics"),
    ("Which of the following inscriptions of Rudradaman happened to be the first royal inscription of early India composed in chaste Sanskrit?", "Indian History and Politics"),
    ("When was a Madrasa opened in Kolkata to promote the study of Arabic, Persian and Islamic law?", "Indian History and Politics"),
    ("Under the leadership of which of the following revolutionaries was Chittagong Armoury Raid conducted?", "Indian History and Politics"),
    ("In 2021, in which of the following states did the Prime Minister lay the foundation stone for the Raja Mahendra Pratap Singh State University?", "Indian History and Politics"),
    ("In which part of India does the hot wind 'Loo' blow?", "Indian Geography"),
    ("At what latitude does the easterly jet stream blow over peninsular India during the summer months?", "Indian Geography"),
    ("In which state of India is Kund or Tanka used for water harvesting?", "Indian Geography"),
    ("Which of the following celebrations is dedicated to Sun God and his wife Usha to thank them for sustaining life on earth and for granting wishes?", "Indian Geography"),
    ("Which condition, also known as icterus, causes a yellowing of your skin and the whites of your eyes?", "Science and Technology"),
    ("When electricity is passed through water, what kind of chemical reaction occurs?", "Science and Technology"),
    ("What is the IUPAC name of tertiarybutyl alcohol?", "Science and Technology"),
    ("What is the relationship between interest rate and demand for money?", "Economics"),
    ("When was the High Court and Supreme Court Judges (Salaries and Conditions of Service) Amendment Bill, 2021 introduced in Lok Sabha?", "Indian Politics"),
    ("Which Article of the Constitution explains that the executive power of every state shall be so exercised as not to impede or prejudice the exercise of the executive power of the Union, and the executive power of the union shall extend to the giving of such directions to a state as may appear to the Government of India to be necessary for that purpose?", "Indian Politics"),
    ("The government of which of the following states created a draft policy in 2022 for senior citizens on the basis of article 41, which aims to form a directorate for the welfare of senior citizens?", "Indian Politics"),
    ("Which of the following is NOT correct about Directive Principles of State Policy?", "Indian Politics"),
    ("The inaugural match of the Women Premier League 2023 cricket was played in which of the following venues?", "Sports"),
    ("At which Olympics did Gagan Narang win a bronze medal?", "Sports"),
    ("In the year 1952, who among the following lent his voice for the film 'Amar Bhupali', which was being produced in two languages simultaneously and he sang in both Bengali and Marathi?", "Sports"),
    ("Which of the following can be represented as a functional unit of nature?", "Economics"),
    ("Which of the following statements correctly defines the green revolution?", "Economics"),
    ("What is the length of Indian Railways network, according to Railway Yearbook 2019-20?", "Indian Geography"),
    ("Which of the following is the largest crustal plate on Earth with an area of over 103,000,000 km²?", "Indian Geography"),
    ("'Nuakhai' is the state festival of:", "Indian Geography"),
    ("Hot local wind that flows over north India in summer is known as:", "Indian Geography"),
    ("Which of the following is a straight-chain alkyl carboxylic acid with the chemical formula CH₃CH₂CH₂CO₂H?", "Science and Technology"),
    ("Which of the following Illustrations shows the mitochondrion's structural details?", "Science and Technology"),
    ("Which of the following goods needs further transformation in the economic process?", "Economics"),
    ("Which of the following is an inactivated (killed) polio vaccine developed in 1952?", "Science and Technology"),
    ("Who was the revenue minister during the reign of Akbar?", "Indian History and Politics"),
    ("Which government honoured a distinguished percussionist named Pandit Anindo Chatterjee with the Banga Vibhushan Award in 2022?", "Indian History and Politics"),
    ("After the death of Humayun, the 13 year-old Akbar was coronated in 1556 at Kalanaur in ________.", "Indian History and Politics"),
    ("Which Governor-General of British India helped Raja Ram Mohan Roy legally abolish the sati practice?", "Indian History and Politics"),
    ("Mahabalipuram emerged as an important centre of temple architecture under which of the following kingdoms of south India?", "Indian History and Politics"),
    ("By which of the following state governments is the Tansen Music Festival organised?", "Indian History and Politics"),
    ("Which of the following places is related to Gandhi's Satyagraha of the year 1917?", "Indian History and Politics"),
    ("Which of the following festivals is celebrated as the birth anniversary of Guru Nanak Dev?", "Indian History and Politics"),
    ("According to the Indian Railways (2019-2020), which state has the largest railway track in India?", "Indian Geography"),
    ("Which of the following is in geographical proximity to Sri Lanka?", "Indian Geography"),
    ("The climate of a place is NOT affected by which of the following?", "Indian Geography"),
    ("The decomposition of gaseous Ammonia on a hot platinum surface is a ________ order reaction at high pressure.", "Science and Technology"),
    ("In which musical note did Newland put the metals Co and Ni with halogens?", "Science and Technology"),
    ("Which organisms are classified as Aves?", "Science and Technology"),
    ("Which of the following was the mascot of the FIH men's Hockey World Cup - 2023?", "Sports"),
    ("How many awards were presented at the National Sports and Adventure Awards-2022 ceremony held at Rashtrapati Bhavan on 30 November 2022?", "Sports"),
    ("Which Five-Year Plan primarily focused on the 'Garibi Hatao' initiative?", "Indian Economics"),
    ("The Parliament passed the Marine Aids to Navigation Bill, 2021 to repeal and replace which of the following Acts?", "Indian Economics"),
    ("Who was appointed as India's 28th Controller General of Accounts (CGA) in March 2023?", "Current Affairs"),
    ("Which of the following statements is INCORRECT about the Directive Principles of State Policy?", "Current Affairs"),
    ("Which of the following has the highest salinity?", "Indian Geography"),
    ("Harela is a festival of greenery, peace, prosperity, and environmental conservation, primarily celebrated in which of the following states?", "Indian Geography"),
    ("Which physical feature of India prevents the cold winds from central Asia from entering the Indian subcontinents?", "Indian Geography"),
    ("Which of the following is the transboundary river between India and Pakistan?", "Indian Geography"),
    ("According to the Agricultural and Processed food products Export Development Authority (APEDA) 2020-2021, which state of India has the first rank in grapes production?", "Indian Geography"),
    ("Which of the following social reformers of 19th century India was the author of 'Stree Purush Tulana'?", "Indian History and Politics"),
    ("Which state initiated the implementation of the Mid-day Meal scheme in elementary schools?", "Indian History and Politics"),
    ("Who among the following freedom fighters of India is the author of the book, 'The Indian Struggle'?", "Indian History and Politics"),
    ("Gautamiputra Satakarni titled Rajaraja and Maharaja is related to which of the following dynasties?", "Indian History and Politics"),
    ("In the 7th Century AD, a new religion called Islam was born in ________.", "Indian History and Politics"),
    ("Which Article of the Constitution of India grants power to the President to appoint Judges of the Supreme Court?", "Indian Constitution and Governance"),
    ("Which of the following Articles of the Indian Constitution mentions about the organisation of 'Village Panchayats'?", "Indian Constitution and Governance"),
    ("Which of the following Articles of the Indian Constitution contains Fundamental Duties?", "Indian Constitution and Governance"),
    ("'Au' is the symbol for which of the following elements?", "Science and Technology"),
    ("To which group do the alkaline earth metals such as radium, barium and strontium belong?", "Science and Technology"),
    ("Which species is known as black lipped pearl oyster found in the Indo-Pacific, within tropical coral reefs?", "Science and Technology"),
    ("In which of the following games is one player known as the Wicketkeeper?", "Sports"),
    ("How many medals did India win in International Shooting Sport Federation (ISSF) World Cup 2022, which was held in Cairo, Egypt?", "Sports"),
    ("Mohiniyattam is associated with which of the following traditional dance styles?", "Arts and Culture"),
    ("Ustad Vilayat Ali Khan is a maestro in ________.", "Arts and Culture"),
    ("Sitar maestro, Pandit Ravi Shankar was awarded which of the following awards by the Government of India in 1999?", "Arts and Culture")
]




# Separate the data into questions and labels (subjects)
questions, labels = zip(*data)

# Create a train-test split for validation
X_train, X_test, y_train, y_test = train_test_split(questions, labels, test_size=0.2, random_state=42)

# Create a pipeline with TF-IDF Vectorizer and Naive Bayes
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),  # TF-IDF and bi-grams
    ('clf', MultinomialNB())  # Naive Bayes classifier
])

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'tfidf__max_features': [500, 1000, 2000],
    'tfidf__ngram_range': [(1, 1), (1, 2)],  # Unigrams vs. Bigrams
    'clf__alpha': [0.5, 1.0, 2.0]  # Regularization strength for Naive Bayes
}

# Grid search with cross-validation
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)

# Train the model using grid search
grid_search.fit(X_train, y_train)

# Save the best model
joblib.dump(grid_search.best_estimator_, 'best_subject_classifier_model.pkl')
print("Best model saved successfully!")

# Load the best model back (for future use)
best_model = joblib.load('best_subject_classifier_model.pkl')

# Function to predict the subject of a new question
def predict_subject(question):
    return best_model.predict([question])[0]

# Example new questions to classify
new_questions = [
    "What is the role of RBI in controlling inflation?",
    "Who was the first emperor of the Gupta dynasty?",
    "Where is Mount Everest located?"
]

# Classify new questions using the best model
for question in new_questions:
    predicted_subject = predict_subject(question)
    print(f"Question: {question}\nPredicted Subject: {predicted_subject}\n")
