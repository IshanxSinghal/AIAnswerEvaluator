# AI Evaluator 🤖📝

An intelligent answer sheet evaluation platform that uses AI and computer vision to automatically grade handwritten answers with detailed scoring and feedback.

![AI Evaluator](https://img.shields.io/badge/AI-Evaluator-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13-green.svg)
![React](https://img.shields.io/badge/React-19.1.0-61dafb.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-009688.svg)

## 🌟 Features

- **Automated OCR**: Extract text from handwritten answer sheets using Google Cloud Vision API and EasyOCR
- **Intelligent Segmentation**: Automatically detects and segments individual questions from answer sheets
- **AI-Powered Scoring**: Uses Groq AI to evaluate answers against model answers with detailed rubrics
- **Interactive Dashboard**: Real-time progress tracking and detailed results visualization
- **Modern UI/UX**: Professional glassmorphism design with smooth animations
- **RESTful API**: FastAPI backend with CORS support for seamless integration

## 🏗️ Architecture

```
┌─────────────────┐
│   React Frontend │
│   (Port 3000)    │
└────────┬─────────┘
         │
         │ HTTP Request
         │
         ▼
┌─────────────────┐
│  FastAPI Backend │
│   (Port 8000)    │
└────────┬─────────┘
         │
         ├─► Orchestrator ──┬─► Preprocessor Agent (Image Processing)
         │                   │
         │                   ├─► OCR Agent (Text Extraction)
         │                   │   └─► Google Cloud Vision API
         │                   │   └─► EasyOCR
         │                   │
         │                   └─► Scoring Agent (AI Evaluation)
         │                       └─► Groq API
         │
         └─► Response (JSON)
```

## 📁 Project Structure

```
Impactathon 25'/
├── ai-evaluator/               # React Frontend
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── team-images/        # Team member photos
│   ├── src/
│   │   ├── App.js              # Main app component with routing
│   │   ├── Homepage.jsx        # Landing page
│   │   ├── EvaluatePage.jsx    # Upload & evaluation interface
│   │   ├── AboutUs.jsx         # Team information page
│   │   └── index.js            # React entry point
│   └── package.json
│
├── scripts/                    # Core AI/ML modules
│   ├── agents/
│   │   ├── preprocessor_agent.py   # Image preprocessing & segmentation
│   │   ├── ocr_agent.py            # Text extraction logic
│   │   └── scoring_agent.py        # AI-based answer evaluation
│   ├── ai_evaluator.py         # Groq AI integration
│   ├── hwr.py                  # Handwriting recognition utilities
│   ├── preprocess.py           # Image preprocessing utilities
│   ├── scorer.py               # Scoring algorithms
│   ├── text_cleaning.py        # OCR text cleaning
│   └── utils.py                # Helper functions
│
├── data/
│   ├── raw/                    # Uploaded answer sheets
│   ├── processed/              # Segmented question images
│   └── annotations.csv         # Training data annotations
│
├── models/                     # ML model storage
│   ├── hwr_model/              # Handwriting recognition model
│   └── scorer_model/           # Scoring model weights
│
├── notebooks/                  # Jupyter notebooks for experimentation
│
├── api.py                      # FastAPI server & endpoints
├── orchestrator.py             # Pipeline coordinator
├── run_pipeline.py             # CLI interface for batch processing
├── .env                        # Environment variables (not in repo)
├── google-cloud-key.json       # Google Cloud credentials (not in repo)
└── README.md                   # This file
```

## 🛠️ Tech Stack

### Frontend
- **React 19.1.0** - UI framework with hooks
- **React Router DOM 7.6.0** - Client-side routing
- **CSS-in-JS** - Inline styling with glassmorphism effects

### Backend
- **FastAPI 0.115.12** - Modern async web framework
- **Python 3.13** - Backend runtime
- **Uvicorn** - ASGI server

### AI/ML Services
- **Google Cloud Vision API** - OCR and text extraction
- **EasyOCR** - Fallback OCR solution
- **Groq API** - AI-powered answer evaluation
- **OpenCV (cv2)** - Image preprocessing
- **PIL/Pillow** - Image manipulation

### Development Tools
- **Node.js & npm** - Frontend package management
- **python-dotenv** - Environment variable management
- **CORS Middleware** - Cross-origin resource sharing

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.13+** - [Download here](https://www.python.org/downloads/)
- **Node.js 16+ and npm** - [Download here](https://nodejs.org/)
- **Google Cloud Account** - For Vision API access
- **Groq API Key** - [Get one here](https://groq.com/)

## 🚀 Installation

### 1. Clone the Repository

```bash
cd "/Users/ishansinghal/Desktop/Impactathon 25'"
```

### 2. Backend Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install Python dependencies
pip install fastapi uvicorn python-multipart opencv-python pillow easyocr groq google-cloud-vision python-dotenv
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd ai-evaluator

# Install Node dependencies
npm install

# Return to root directory
cd ..
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```bash
# .env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=/path/to/google-cloud-key.json
```

### 5. Google Cloud Setup

1. Create a Google Cloud project
2. Enable the Cloud Vision API
3. Create a service account and download the JSON key
4. Save as `google-cloud-key.json` in the project root
5. Update the path in `.env`

## 🎯 Running the Application

### Start Backend Server

```bash
# Make sure you're in the project root and virtual environment is activated
uvicorn api:app --reload
```

The backend will start at `http://localhost:8000`

### Start Frontend Development Server

```bash
# In a new terminal, navigate to frontend directory
cd ai-evaluator

# Start React development server
npm start
```

The frontend will open at `http://localhost:3000`

## 📖 Usage

### Web Interface

1. **Navigate to Homepage** - Visit `http://localhost:3000`
2. **Click "Get Started"** - Navigate to the evaluation page
3. **Upload Answer Sheet** - Drag and drop or click to select an image file (PNG, JPG, JPEG)
4. **View Results** - See detailed scoring, feedback, and visualizations

### API Usage

#### Evaluate Answer Sheet

```bash
POST http://localhost:8000/api/evaluate
Content-Type: multipart/form-data

Body:
  file: <answer_sheet_image>
```

**Example using curl:**

```bash
curl -X POST "http://localhost:8000/api/evaluate" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/answer_sheet.jpg"
```

**Response:**

```json
{
  "submission_id": "b2db6b9c-04b2-4ad8-b2c7-9b686af3d97b",
  "total_questions": 7,
  "total_score": 85,
  "max_score": 100,
  "percentage": 85.0,
  "results": [
    {
      "question_number": 1,
      "student_answer": "Newton's first law states...",
      "model_answer": "Newton's first law states that an object remains at rest...",
      "score": 90,
      "feedback": "Excellent answer with clear understanding of concepts.",
      "strengths": ["Complete explanation", "Correct terminology"],
      "improvements": ["Could add more examples"]
    }
  ]
}
```

#### Health Check

```bash
GET http://localhost:8000/api/health
```

**Response:**

```json
{
  "status": "ok",
  "version": "1.0.0"
}
```

### CLI Interface

For batch processing multiple answer sheets:

```bash
python run_pipeline.py --input data/raw/answer_sheet.jpg --output data/processed/
```

## 🎨 Features Breakdown

### Preprocessing Agent
- Image enhancement and noise reduction
- Contour detection for question segmentation
- Adaptive thresholding for handwriting clarity

### OCR Agent
- Google Cloud Vision API for high-accuracy OCR
- EasyOCR as fallback mechanism
- Text cleaning and normalization

### Scoring Agent
- AI-powered semantic similarity analysis
- Rubric-based evaluation with Groq
- Detailed feedback generation
- Strengths and improvement suggestions

### Frontend Dashboard
- Real-time upload progress tracking
- Glassmorphism design aesthetic
- Animated result cards
- Responsive layout for all devices
- Visual score indicators and progress bars

## 🔧 Configuration

### Model Answers

Edit `api.py` to customize model answers:

```python
MODEL_ANSWERS = {
    1: "Your model answer for question 1",
    2: "Your model answer for question 2",
    # ... add more questions
}
```

### Scoring Rubric

Modify `scripts/agents/scoring_agent.py` to adjust evaluation criteria:

```python
def score_answer(student_answer, model_answer, question_number):
    # Customize scoring logic
    # Adjust weight for different criteria
    pass
```

## 🐛 Troubleshooting

### Backend Issues

**ModuleNotFoundError: No module named 'aiofiles'**
```bash
pip install aiofiles
```

**Google Cloud Vision API Error**
```bash
# Verify credentials path
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/google-cloud-key.json"
```

**Groq API Authentication Failed**
```bash
# Check .env file contains valid API key
echo $GROQ_API_KEY
```

### Frontend Issues

**Port 3000 already in use**
```bash
# Kill existing process
lsof -ti:3000 | xargs kill -9

# Or use different port
PORT=3001 npm start
```

**CORS Error**
- Ensure backend is running on port 8000
- Check CORS middleware in `api.py` allows your origin

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project was created for **Impactathon 25'** hackathon.

## 👥 Team

Meet the incredible team behind AI Evaluator:

- **Ishan Singhal** - AI/ML Engineer, Lead Developer, Frontend Developer

Visit the About Us page at `http://localhost:3000/about` to learn more about the team!

## 🙏 Acknowledgments

- Google Cloud Vision API for powerful OCR capabilities
- Groq for lightning-fast AI inference
- EasyOCR for open-source OCR support
- React and FastAPI communities for excellent documentation

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the development team.

---

**Made with ❤️ for Impactathon 25'**
