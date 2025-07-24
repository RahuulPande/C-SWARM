import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Page configuration
st.set_page_config(
    page_title="Cognizant Talent Edge CRM Toolkit",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for branding
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #F5F5F5;
    }
    
    /* Headers styling */
    .main-header {
        color: #0072C6;
        font-family: 'Roboto', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        padding: 20px 0;
    }
    
    .sub-header {
        color: #333;
        font-family: 'Roboto', sans-serif;
        font-size: 1.2rem;
        text-align: center;
        padding-bottom: 20px;
    }
    
    /* Cognizant blue buttons */
    .stButton > button {
        background-color: #0072C6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        font-family: 'Roboto', sans-serif;
        font-weight: 500;
        border-radius: 4px;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #005a9e;
        transform: translateY(-1px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    /* UBS red accent buttons */
    .accent-button > button {
        background-color: #D40511;
        color: white;
    }
    
    .accent-button > button:hover {
        background-color: #b00410;
    }
    
    /* Success messages */
    .success-text {
        color: #4CAF50;
        font-weight: bold;
        font-family: 'Roboto', sans-serif;
    }
    
    /* Metric cards */
    div[data-testid="metric-container"] {
        background-color: white;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: white;
        border: 1px solid #0072C6;
    }
    
    /* DataFrame styling */
    .dataframe {
        font-family: 'Roboto', sans-serif;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #0072C6;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'query_results' not in st.session_state:
    st.session_state.query_results = None

# Mock data creation
@st.cache_data
def create_mock_data():
    data = {
        'Project_Type': ['Integration/Migration', 'Integration/Migration', 'Pega', 'Pega', 
                        'Mobile Apps', 'Mobile Apps', 'Cards', 'Cards',
                        'Integration/Migration', 'Mobile Apps', 'Pega', 'Cards'],
        'Location': ['Zurich', 'Pune', 'Zurich', 'Pune', 
                    'Zurich', 'Pune', 'Zurich', 'Pune',
                    'Zurich', 'Zurich', 'Pune', 'Zurich'],
        'Skill': ['AI', 'Python', 'Java', 'AI', 
                  'Python', 'AI', 'Cybersecurity', 'Cloud',
                  'Cloud', 'AI', 'Python', 'Java'],
        'Role': ['Developer', 'Developer', 'Developer', 'Tester', 
                'Developer', 'Tester', 'Developer', 'Tester',
                'Tester', 'Developer', 'Developer', 'Tester'],
        'Count': [150, 120, 80, 60, 200, 100, 90, 70, 110, 180, 140, 85],
        'Available_Now': [90, 60, 50, 40, 120, 60, 60, 40, 70, 110, 80, 50],
        'Available_1_Month': [40, 40, 20, 15, 50, 30, 20, 20, 30, 50, 40, 25],
        'Experience_Years': [5, 4, 6, 3, 5, 4, 7, 5, 4, 6, 5, 6]
    }
    return pd.DataFrame(data)

# NLP Query Mock Function
def mock_nlp_response(query):
    query_lower = query.lower()
    df = create_mock_data()
    
    # Simple keyword matching
    if 'mobile' in query_lower and 'zurich' in query_lower:
        mobile_zurich = df[(df['Project_Type'] == 'Mobile Apps') & (df['Location'] == 'Zurich')]
        total = mobile_zurich['Count'].sum()
        available = mobile_zurich['Available_Now'].sum()
        if 'tester' in query_lower:
            testers = mobile_zurich[mobile_zurich['Role'] == 'Tester']
            return f"📊 We have {testers['Count'].sum()} Mobile App Testers in Zurich, {testers['Available_Now'].sum()} available immediately."
        return f"📊 We have {total} Mobile App specialists in Zurich, {available} available immediately."
    
    elif 'ai' in query_lower:
        ai_data = df[df['Skill'] == 'AI']
        total = ai_data['Count'].sum()
        available = ai_data['Available_Now'].sum()
        return f"🤖 Total AI-trained associates: {total}, with {available} available now across all locations."
    
    elif 'python' in query_lower:
        python_data = df[df['Skill'] == 'Python']
        total = python_data['Count'].sum()
        return f"🐍 We have {total} Python developers across our teams."
    
    else:
        return "💡 Try asking about specific skills, locations, or project types. For example: 'Mobile testers in Zurich available now'"

# PDF Export Function
def generate_pdf_report(data, query_params):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0072C6'),
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    # Title
    elements.append(Paragraph("Cognizant Talent Report", title_style))
    elements.append(Spacer(1, 20))
    
    # Query Parameters
    elements.append(Paragraph(f"<b>Query Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    elements.append(Paragraph(f"<b>Project Type:</b> {query_params.get('project_type', 'All')}", styles['Normal']))
    elements.append(Paragraph(f"<b>Skill:</b> {query_params.get('skill', 'All')}", styles['Normal']))
    elements.append(Paragraph(f"<b>Location:</b> {query_params.get('location', 'All')}", styles['Normal']))
    elements.append(Spacer(1, 20))
    
    # Data Table
    if not data.empty:
        table_data = [data.columns.tolist()] + data.values.tolist()
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0072C6')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
    
    doc.build(elements)
    buffer.seek(0)
    return buffer

# Header
st.markdown('<h1 class="main-header">Cognizant Talent Edge CRM Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Empower CRMs to showcase associate skills and availability for UBS projects</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("# Talent Edge CRM Toolkit")
    st.markdown("### Cognizant Talent Insights for UBS Deals")
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigate",
        ["Dashboard", "Project Query", "Visualizations", "Availability", "Help"],
        label_visibility="collapsed"
    )

# Load data
df = create_mock_data()

# Main content based on selected page
if page == "Dashboard":
    st.subheader("🏠 Talent Overview")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        zurich_total = df[df['Location'] == 'Zurich']['Count'].sum()
        zurich_available = df[df['Location'] == 'Zurich']['Available_Now'].sum()
        st.metric(
            "Zurich Total Associates",
            f"{zurich_total}",
            f"{round(zurich_available/zurich_total*100)}% Available"
        )
    
    with col2:
        pune_total = df[df['Location'] == 'Pune']['Count'].sum()
        pune_available = df[df['Location'] == 'Pune']['Available_Now'].sum()
        st.metric(
            "Pune Total Associates",
            f"{pune_total}",
            f"{round(pune_available/pune_total*100)}% Available"
        )
    
    with col3:
        ai_total = df[df['Skill'] == 'AI']['Count'].sum()
        ai_available = df[df['Skill'] == 'AI']['Available_Now'].sum()
        st.metric(
            "AI-Trained Globally",
            f"{ai_total}",
            f"{round(ai_available/ai_total*100)}% Available"
        )
    
    # Skill Distribution Pie Chart
    st.markdown("### 📊 Skill Distribution")
    skill_dist = df.groupby('Skill')['Count'].sum().reset_index()
    fig_pie = px.pie(
        skill_dist, 
        values='Count', 
        names='Skill',
        color_discrete_map={
            'AI': '#0072C6',
            'Python': '#D40511',
            'Java': '#4CAF50',
            'Cybersecurity': '#FF9800',
            'Cloud': '#9C27B0'
        }
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # NLP Query Section
    st.markdown("### 🤖 AI-Powered Talent Query")
    nlp_query = st.text_input(
        "Ask about talent (e.g., 'Mobile testers in Zurich available now')",
        placeholder="Type your question here..."
    )
    
    if nlp_query:
        response = mock_nlp_response(nlp_query)
        st.markdown(f'<p class="success-text">{response}</p>', unsafe_allow_html=True)

elif page == "Project Query":
    st.subheader("🔍 Query Talent by Project")
    
    col1, col2 = st.columns(2)
    
    with col1:
        project_type = st.selectbox(
            "Project Type",
            ["All"] + df['Project_Type'].unique().tolist()
        )
        skill = st.selectbox(
            "Skill",
            ["All"] + df['Skill'].unique().tolist()
        )
    
    with col2:
        role = st.selectbox(
            "Role",
            ["All"] + df['Role'].unique().tolist()
        )
        location = st.selectbox(
            "Location",
            ["All"] + df['Location'].unique().tolist()
        )
    
    # Search button with custom styling
    search_col1, search_col2, search_col3 = st.columns([1, 1, 3])
    with search_col1:
        st.markdown('<div class="accent-button">', unsafe_allow_html=True)
        search_clicked = st.button("🔍 Search Talent", help="Query associates")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if search_clicked:
        # Filter data
        filtered_df = df.copy()
        
        if project_type != "All":
            filtered_df = filtered_df[filtered_df['Project_Type'] == project_type]
        if skill != "All":
            filtered_df = filtered_df[filtered_df['Skill'] == skill]
        if role != "All":
            filtered_df = filtered_df[filtered_df['Role'] == role]
        if location != "All":
            filtered_df = filtered_df[filtered_df['Location'] == location]
        
        if not filtered_df.empty:
            # Store results in session state
            st.session_state.query_results = filtered_df
            
            # Display results
            st.success(f"✅ {filtered_df['Count'].sum()} associates found. Average Experience: {filtered_df['Experience_Years'].mean():.1f} years.")
            
            # Show relevant columns
            display_df = filtered_df[['Project_Type', 'Location', 'Skill', 'Role', 'Count', 'Available_Now', 'Available_1_Month', 'Experience_Years']]
            st.dataframe(display_df, use_container_width=True)
            
            # Export to PDF button
            query_params = {
                'project_type': project_type,
                'skill': skill,
                'role': role,
                'location': location
            }
            
            pdf_buffer = generate_pdf_report(display_df, query_params)
            st.download_button(
                label="📄 Export to PDF",
                data=pdf_buffer,
                file_name=f"talent_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf"
            )
        else:
            st.warning("⚠️ No results found. Try different filters.")

elif page == "Visualizations":
    st.subheader("📈 Talent Insights Visualizations")
    
    # Skills by Location Bar Chart
    st.markdown("### Skills Distribution by Location")
    skills_location = df.groupby(['Location', 'Skill'])['Count'].sum().reset_index()
    fig_bar = px.bar(
        skills_location,
        x='Location',
        y='Count',
        color='Skill',
        title='Associate Count by Location and Skill',
        color_discrete_map={
            'AI': '#0072C6',
            'Python': '#D40511',
            'Java': '#4CAF50',
            'Cybersecurity': '#FF9800',
            'Cloud': '#9C27B0'
        }
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Availability Heatmap
    st.markdown("### Availability Heatmap by Project Type")
    pivot_data = df.pivot_table(
        values='Available_Now',
        index='Project_Type',
        columns='Location',
        aggfunc='sum'
    )
    
    fig_heatmap = px.imshow(
        pivot_data,
        labels=dict(x="Location", y="Project Type", color="Available Now"),
        color_continuous_scale='Blues',
        title='Associates Available Now by Project Type and Location'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

elif page == "Availability":
    st.subheader("📅 Talent Availability & Deployment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        project_filter = st.selectbox(
            "Filter by Project Type",
            ["All"] + df['Project_Type'].unique().tolist()
        )
    
    with col2:
        location_filter = st.selectbox(
            "Filter by Location",
            ["All"] + df['Location'].unique().tolist()
        )
    
    # Filter data
    availability_df = df.copy()
    
    if project_filter != "All":
        availability_df = availability_df[availability_df['Project_Type'] == project_filter]
    if location_filter != "All":
        availability_df = availability_df[availability_df['Location'] == location_filter]
    
    # Display availability table
    st.info("📌 Filter to see associates ready for immediate deployment or in 1 month.")
    display_cols = ['Project_Type', 'Location', 'Skill', 'Role', 'Available_Now', 'Available_1_Month']
    st.dataframe(availability_df[display_cols], use_container_width=True)
    
    # Mock calendar check
    if st.button("📅 Check Team Calendar for Deployment", type="primary"):
        st.markdown(
            '<p class="success-text">✅ Mock Calendar: Teams available starting August 1, 2025. 70% readiness for UBS projects.</p>',
            unsafe_allow_html=True
        )

elif page == "Help":
    st.subheader("❓ Help & Tips")
    
    st.markdown("""
    ### How to Use the Talent Edge CRM Toolkit
    
    **📊 Dashboard**
    - Get a quick overview of talent metrics across locations
    - View skill distribution with interactive charts
    - Use natural language queries to find specific talent information
    
    **🔍 Project Query**
    - Search associates by project type (e.g., Pega for UBS workflows)
    - Filter by skills, roles, and locations
    - Export results to PDF for client meetings
    - View availability counts for immediate and 1-month deployment
    
    **📈 Visualizations**
    - Explore interactive charts for deeper talent insights
    - Analyze skill distribution across locations
    - View availability heatmaps by project type
    
    **📅 Availability**
    - Check deployment readiness by project and location
    - Access mock calendar for team scheduling
    - Filter associates by immediate or short-term availability
    
    **💡 Pro Tips:**
    - Use NLP queries on the Dashboard for quick answers (powered by mock Claude AI)
    - Export query results to PDF for professional client presentations
    - Leverage visualizations to demonstrate Cognizant's talent depth to UBS
    
    **📧 Contact:** support@cognizant.com for real system integrations
    
    ---
    *This is a prototype for the Vibe Coding Event. In production, this would integrate with live HR systems and Claude AI.*
    """)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #666; font-size: 0.9rem;">© 2025 Cognizant Technology Solutions. Prototype for Vibe Coding Event.</p>',
    unsafe_allow_html=True
)