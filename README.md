# Cognitive Data Storyteller 
Cognitive Data Storyteller (CDS) is a standalone software system that transforms raw data into human-like narratives using natural language processing
and database insights. It is designed to help users—technical and non-technical alike—understand complex datasets through clear, contextual stories. 
## ✨ Features 
Human-like narrative synthesis from structured data
Interactive story customization
Cross-domain insight linking
Query-driven story augmentation
Modular and extensible architecture 
# 📁 Project Structure 
Cognitive-Data-Storyteller/
├── data_loader.py # Handles data import from databases or CSVs
├── analysis.py # Performs data analysis and generates insights
├── narrative_generator.py # Converts insights into natural language
├── insight_linker.py # Links related insights into a cohesive story
├── query_engine.py # Supports user-driven custom queries
├── visualization.py # (Optional) Generates visual summaries
├── main.py # Entry point for running the software
├── requirements.txt # List of required Python packages
├── README.md # Project overview and instructions

## 🚀 How to Run 
### 1. Clone the Repository 
```
git clone https://github.com/Aaryan-Poria/Cognitive-Data-Storyteller.git
cd Cognitive-Data-Storyteller
```

## 2. Create and Activate a Virtual Environment (Recommended) 
```
python -m venv venv
```
### On Windows
```
venv\Scripts\activate
```
### On macOS/Linux
```
source venv/bin/activate
```

## 3. Install Dependencies 
```
pip install -r requirements.txt
```
## 4. Prepare the Data 
Ensure your SQLite database file (e.g., data.db) or CSV files are available. The path should be correctly referenced in data_loader.py. 
## 5. Run the Application 
```
streamlit run main.py
```
The program will: - Load the data - Analyze the content - Generate meaningful, natural-language insights - (Optionally) Display visualizations 
## 🛠 Customization 
Data Source: Modify data_loader.py to change data inputs.
Narrative Style: Update narrative_generator.py for tone or format.
Insight Rules: Adapt analysis.py or insight_linker.py to refine insight logic. 
## 🧹 Recommended .gitignore 
__pycache__/
*.pyc
.DS_Store
venv/
## 📜 License 
This project is licensed under the MIT License
