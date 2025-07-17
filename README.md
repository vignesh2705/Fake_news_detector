# AI-Powered Fake News Detection System

A comprehensive web application that uses machine learning and natural language processing to detect fake news articles. Built with Flask, scikit-learn, and Bootstrap for a professional, production-ready experience.

## 🚀 Features

### Core Functionality
- **AI-Powered Analysis**: Uses Logistic Regression and Random Forest classifiers
- **NLP Processing**: Complete text preprocessing pipeline with tokenization, stopword removal, and stemming
- **TF-IDF Vectorization**: Advanced feature extraction for accurate predictions
- **Confidence Scoring**: Provides confidence percentages for each prediction
- **Keyword Highlighting**: Shows influential words in the decision-making process
- **Model Comparison**: Side-by-side results from both ML algorithms

### Web Interface
- **Responsive Design**: Mobile-friendly Bootstrap interface with dark theme
- **Real-time Predictions**: Instant analysis of news articles
- **Prediction History**: Track and review past analyses
- **Sample Articles**: Pre-loaded examples for testing
- **Model Metrics**: View detailed performance statistics

### Technical Features
- **RESTful API**: JSON endpoints for programmatic access
- **Database Storage**: SQLite database for prediction history
- **Model Persistence**: Trained models saved and loaded efficiently
- **Error Handling**: Comprehensive error management and user feedback
- **Auto-save**: Automatically saves draft text while typing

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework for Python
- **scikit-learn**: Machine learning algorithms and evaluation metrics
- **NLTK**: Natural language processing and text preprocessing
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations and array handling
- **SQLAlchemy**: Database ORM for data persistence
- **joblib**: Model serialization and loading

### Frontend
- **Bootstrap 5**: Responsive CSS framework with dark theme
- **Font Awesome**: Professional icon library
- **Vanilla JavaScript**: Interactive features and form handling
- **Chart.js Ready**: Prepared for future analytics visualization

### Machine Learning
- **Logistic Regression**: Linear classification algorithm
- **Random Forest**: Ensemble method for robust predictions
- **TF-IDF Vectorizer**: Text feature extraction
- **Cross-validation**: Model evaluation and metrics

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fake-news-detection
   ```

2. **Install dependencies**
   ```bash
   pip install flask scikit-learn nltk pandas numpy sqlalchemy joblib
   ```

3. **Download NLTK data**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - The system will automatically train models on first run

## 🔧 Configuration

### Environment Variables
- `SESSION_SECRET`: Flask session secret key
- `DATABASE_URL`: Database connection string (defaults to SQLite)

### Model Configuration
The system uses the following default parameters:
- **TF-IDF**: Max features: 5000, N-grams: (1,2)
- **Logistic Regression**: Default parameters with random_state=42
- **Random Forest**: 100 estimators, random_state=42

## 📊 Model Performance

The system provides comprehensive evaluation metrics:
- **Accuracy**: Overall prediction correctness
- **Precision**: Positive prediction accuracy
- **Recall**: True positive detection rate
- **F1-Score**: Harmonic mean of precision and recall
- **Classification Report**: Detailed per-class metrics

## 🎯 Usage Examples

### Web Interface
1. Navigate to the home page
2. Enter a news article in the text area
3. Click "Analyze News" to get predictions
4. View results from both ML models
5. Check important keywords and confidence scores
