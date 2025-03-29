import streamlit as st
import re
import nltk
import pandas as pd
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
# from sentence_transformers import SentenceTransformer
import urllib.parse
import os

# Download NLTK stopwords
nltk.download("stopwords")
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english")).union({"ii","india", "year", "project", "which", "was", "ans", "b", "c", "given", "correct", "answer", "r", "true", "using", "statements", "select"})


def preprocess_question(question):
    # Remove unwanted characters and split into words
    question = re.sub(r"[^a-zA-Z0-9\s]", "", question)  # Remove special characters
    words = question.lower().split()
    
    # Remove stopwords and lemmatize
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return " ".join(words)


# Function to parse multiple MCQ files
def parse_mcq_files(uploaded_files):
    """Extract questions from multiple uploaded files"""
    questions = []
    for file in uploaded_files:
        content = file.getvalue().decode("utf-8")
        
        # Handle different file formats (text, markdown)
        if file.name.endswith('.md') or file.name.endswith('.txt'):
            file_questions = re.split(r"Q\.\d+", content)[1:]  # Split based on question markers
            clean_questions_by_Ans = [q.strip().split("Ans")[0].strip() for q in file_questions]  # Extract questions
            clean_questions_by_1 = [q.strip().split("1.")[0].strip() for q in clean_questions_by_Ans]  # Extract questions
            removed_highfen = [q.replace('*', ' ').replace('-', ' ').replace('*', ' ').strip()   for q in clean_questions_by_1]
            single_line_Qs = [q.replace('\n', ' ').strip()   for q in removed_highfen]  # Replacing newlines with space 
            Qs_with_fileName = [q + " -- "+os.path.splitext(file.name)[0] for q in single_line_Qs]
            questions.extend(Qs_with_fileName)
    return questions

def parse_mcq_files_dynamic(uploaded_files):
    """Extract questions dynamically from multiple uploaded files, keeping answer choices formatted safely."""
    questions = []
    
    for file in uploaded_files:
        content = file.getvalue().decode("utf-8")

        # Normalize content by replacing various bullet markers
        content = re.sub(r"[\*\-]", " ", content)

        # Define a regex pattern to match MCQs dynamically
        pattern = re.compile(r"""
            (?s)                                # Enable multiline matching
            (\d+\.\s*)?                         # Optional numbering (1., 2., etc.)
            ([A-Z][^?\n:]*[\?:]?)\s*            # Question (capitalized, ending with ? or :)
            (?:\[\d+\])?\s*                     # Optional year tag [1995]
            ((?:\(\w\)|\w\.)\s+.*?(?:\n|$)+)    # Answer choices (A., B., C. or (a), (b), etc.)
        """, re.VERBOSE)

        matches = pattern.findall(content)

        for _, question, options in matches:
            # Remove extra spaces and newlines
            question_cleaned = re.sub(r"\s+", " ", question).strip()
            options_cleaned = re.sub(r"\s+", " ", options).strip()

            # Prevent markdown misinterpretation by escaping dots or wrapping in backticks
            options_formatted = re.sub(r"([A-Da-d])\.", r"\1\\.", options_cleaned)  # Escape dots in A., B., etc.
            options_formatted = options_formatted.replace("(", "\\(").replace(")", "\\)")  # Escape (a), (b)

            # Combine question and formatted options
            full_question = f"{question_cleaned} {options_formatted} -- {os.path.splitext(file.name)[0]}"
            questions.append(full_question)

    return questions


# Function to extract and sort keywords by frequency
def extract_keywords(questions):
    """Extracts keywords and maps them to questions"""
    keyword_map = defaultdict(list)
    for question in questions:
        q = question.split(" -- ")[0]
        words = q.lower().split()
        filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
        for word in filtered_words:
            keyword_map[word].append(question)

    # Sort keywords by the number of associated questions (most frequent first)
    sorted_keywords = sorted(keyword_map.items(), key=lambda x: len(x[1]), reverse=True)
    
    return dict(sorted_keywords)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def cluster_questions(questions, n_clusters=5):
    """Clusters similar questions using KMeans and returns cluster names based on feature terms"""
    original_questions = questions.copy()
    
    # Preprocess the questions to remove unnecessary characters (e.g., -- file names)
    for i in range(len(questions)):
        questions[i] = preprocess_question(questions[i].split(" -- ")[0])

    # Vectorize the questions using TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(questions)

    # Fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X)

    # Get the feature names (terms) from the vectorizer
    feature_names = np.array(vectorizer.get_feature_names_out())

    # Get the top terms for each cluster based on centroids
    cluster_terms = {}
    for i in range(n_clusters):
        cluster_center = kmeans.cluster_centers_[i]
        top_terms_idx = cluster_center.argsort()[-5:][::-1]  # Get top 5 terms for each cluster
        top_terms = feature_names[top_terms_idx]
        cluster_terms[i] = " ".join(top_terms)  # Combine top terms to represent the cluster

    # Create a DataFrame to store questions and their assigned clusters
    clustered_data = pd.DataFrame({"question": original_questions, "cluster": clusters})

    # Sort clusters by number of questions (most populated first)
    cluster_sizes = clustered_data["cluster"].value_counts().to_dict()
    sorted_clusters = sorted(cluster_sizes.keys(), key=lambda c: cluster_sizes[c], reverse=False)

    # Replace cluster numbers with the feature-based cluster names
    clustered_data["cluster_name"] = clustered_data["cluster"].apply(lambda x: cluster_terms[x])

    return clustered_data, sorted_clusters, cluster_sizes, cluster_terms


# Function to create a search URL for a question
def create_search_url(question):
    """Generates a Google search URL for a given question"""
    query = urllib.parse.quote_plus(question.split(" -- ")[0])  # URL encode the question
    return f"https://www.google.com/search?q={query}+%2Btestbook+%2Bexamrobot"


from collections import Counter

def display_keyword_related_questions(selected_keyword, keywords_map):
    """Displays questions related to a selected keyword with a visual bar distribution in the sidebar."""
    
    keyword = selected_keyword.split(" (")[0]  # Extract keyword without count
    questions = keywords_map.get(keyword, [])

    if not questions:
        st.warning(f'No questions found for **"{keyword}"**.')
        return

    # Count questions per file
    file_counts = Counter(q.split(" -- ")[1] for q in questions)
    max_count = max(file_counts.values())  # Find max count for normalization

    # Sidebar: Display file-wise question distribution using visual bars
    st.sidebar.subheader(f"Questions Per File for '{keyword}'")

    for file, count in file_counts.items():
        bar_width = int((count / max_count) * 100)  # Normalize bar width (max = sidebar width)
        file = file[0:31].strip()
        st.sidebar.markdown(
            f'<div style="background-color: #1f77b4; height: 12px; width: {bar_width}%; border-radius: 5px;"></div>',
            unsafe_allow_html=True,
        )
        st.sidebar.markdown(f"**{file}** ({count})")

    # Sidebar: Select file to filter questions
    selected_file = st.sidebar.selectbox("Filter by File:", ["All Files"] + list(file_counts.keys()))

    # Display filtered questions
    st.markdown(f"## Questions related to: **{keyword}**")
    for q in questions:
        file_name = q.split(" -- ")[1]
        if selected_file == "All Files" or file_name == selected_file:
            search_url = create_search_url(q)  # Generate search URL for the question
            st.markdown(f"- [{q}]({search_url})")  # Clickable search link




# Function to display questions for a selected cluster
def display_clustered_questions(clustered_df, cluster_sizes, selected_cluster, terms):
    """Displays questions for a selected cluster"""
    cluster_num = selected_cluster  # Extract cluster number
    st.text(f"📌 Questions in Cluster {terms[cluster_num]}")
    for q in clustered_df[clustered_df["cluster"] == cluster_num]["question"]:
        search_url = create_search_url(q)  # Generate search URL for the question
        st.markdown(f"- [{q}]({search_url})")  # Make question clickable (searchable on Google)
        

# Function to create a slider for selecting number of clusters
def select_number_of_clusters():
    """Creates a slider to select the number of clusters"""
    # st.sidebar.header("🔢 Select Number of Clusters")
    return st.sidebar.slider("🔢 Select Number of Clusters", min_value=2, max_value=100, value=5, step=1)

# Function to create a selectbox for keyword selection
def select_keyword(keywords_map):
    """Creates a selectbox for keyword selection"""
    # st.sidebar.header()
    sorted_keyword_options = ["Select"] + [f"{kw} ({len(qs)})" for kw, qs in keywords_map.items()]
    return st.sidebar.selectbox("🔍 Select a Keyword", sorted_keyword_options)

def select_cluster(sorted_clusters, cluster_sizes, features):
    """Creates a selectbox for selecting a cluster and returns the cluster number"""
    # Create options that include both the cluster feature name and its size
    sorted_cluster_options = ["Select"] + [f"{features[c]} ({cluster_sizes[c]})" for c in sorted_clusters]
    
    # Show the selectbox with the cluster names and sizes
    selected_cluster_option = st.sidebar.selectbox("📂 Select a Cluster", sorted_cluster_options)
    
    # If a cluster is selected, return the corresponding cluster number (index)
    if selected_cluster_option != "Select":
        # Find the cluster number corresponding to the selected option
        selected_cluster_index = sorted_clusters[sorted_cluster_options.index(selected_cluster_option) - 1]
        return selected_cluster_index
    
    # Return None if no valid cluster is selected
    return None


# Streamlit UI
st.text("📚 Multi-File MCQ Question Explorer & Clustering")
# Store state for selected keyword and cluster
if "selected_keyword" not in st.session_state:
    st.session_state.selected_keyword = None
if "selected_cluster" not in st.session_state:
    st.session_state.selected_cluster = None

# File upload
uploaded_files = st.file_uploader("Upload MCQ files (text or markdown format)", accept_multiple_files=True, type=["txt", "md"])

if uploaded_files:
    # Parse the uploaded files
    questions = parse_mcq_files_dynamic(uploaded_files)
    st.sidebar.text(f'Total Questions: {len(questions)}')

    # Initialize the session state for enable_clustering if not already done
    if "enable_clustering" not in st.session_state:
        st.session_state.enable_clustering = False  # Default: Clustering OFF

    # Toggle switch to enable/disable clustering
    st.session_state.enable_clustering = st.sidebar.checkbox("Enable Clustering", value=st.session_state.enable_clustering)

    # Handle clustering logic when enabled
    if st.session_state.enable_clustering:
        # Number of clusters selection and clustering
        n_clusters = select_number_of_clusters()

        # Check if clustering has already been done or if number of clusters has changed
        clustered_df, sorted_clusters, cluster_sizes, cluster_terms = cluster_questions(questions, n_clusters=n_clusters)

        # Cluster selection and reset keyword if needed
        selected_cluster = select_cluster(sorted_clusters, cluster_sizes, cluster_terms)
        if selected_cluster != "Select" and selected_cluster != None:
            st.session_state.selected_cluster = selected_cluster
            st.session_state.selected_keyword = None  # Reset keyword selection
            display_clustered_questions(clustered_df, cluster_sizes, selected_cluster, cluster_terms)
    else:
        # Extract keywords and create keyword map if clustering is disabled
        keywords_map = extract_keywords(questions)

        # Keyword selection and reset cluster if needed
        selected_keyword = select_keyword(keywords_map)
        if selected_keyword != "Select":
            st.session_state.selected_keyword = selected_keyword
            st.session_state.selected_cluster = None  # Reset cluster selection
            display_keyword_related_questions(selected_keyword, keywords_map)

