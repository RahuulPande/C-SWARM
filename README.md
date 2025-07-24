# Cognizant Talent Edge CRM Toolkit

A comprehensive Streamlit dashboard for talent management and CRM operations, featuring interactive visualizations, AI-powered queries, and PDF export capabilities.

## Features

- **📊 Dashboard**: Overview of talent metrics across locations with interactive charts
- **🔍 Project Query**: Advanced filtering by project type, skills, roles, and locations
- **📈 Visualizations**: Interactive charts and heatmaps for talent insights
- **📅 Availability**: Real-time availability tracking and deployment scheduling
- **🤖 AI-Powered Queries**: Natural language processing for talent searches
- **📄 PDF Export**: Professional reports for client presentations

## Installation

1. Install the required dependencies:
```bash
pip install --break-system-packages -r requirements.txt
```

2. Add the local bin directory to your PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

The application will be available at `http://localhost:8501`

## Application Structure

- **Main Dashboard**: Talent overview with key metrics and skill distribution
- **Project Query**: Filter and search associates by various criteria
- **Visualizations**: Interactive charts showing talent distribution and availability
- **Availability Management**: Track team availability and deployment readiness
- **Help Section**: Comprehensive guide for using the toolkit

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualizations
- **ReportLab**: PDF generation for reports
- **Custom CSS**: Professional styling with Cognizant branding

## Sample Queries

Try these natural language queries in the AI-powered search:
- "Mobile testers in Zurich available now"
- "Python developers across all locations"
- "AI-trained associates available immediately"

## Data Features

The application includes mock data showcasing:
- Multiple project types (Integration/Migration, Pega, Mobile Apps, Cards)
- Skills tracking (AI, Python, Java, Cybersecurity, Cloud)
- Location-based management (Zurich, Pune)
- Role classifications (Developer, Tester)
- Availability metrics (immediate and 1-month)
- Experience tracking

## Export Capabilities

- Generate professional PDF reports
- Include query parameters and timestamps
- Formatted tables with company branding
- Download directly from the interface

---

*This is a prototype application demonstrating advanced CRM capabilities for talent management.* 