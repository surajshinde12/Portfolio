import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

# ----------------------------------------------------------------------------
# CONFIG - edit these values
# ----------------------------------------------------------------------------
NAME = "Suraj Baban Shinde"
TAGLINE = "AI & ML engineer building LLM, RAG and agent applications"
LOCATION = "Wai, Satara, Maharashtra, India"
EMAIL = "surajshinde1208@gmail.com"
PHONE = "+91-8177859768"
LINKEDIN = "https://www.linkedin.com/in/suraj-shinde-91a833302"
GITHUB = "https://github.com/surajshinde12"
BASE_DIR = Path(__file__).parent
CV_PATH = BASE_DIR / "assets" / "CV.pdf"
CERT_DIR = BASE_DIR / "assets" / "certificates"  # put certificate images here

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# STYLE
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap');

    :root {
        --ink: #2a1650;
        --muted: #6b5f85;
        --paper: #f7f3fd;
        --card: #ffffff;
        --line: #e3d9f5;
        --accent: #7c3aed;
        --accent-soft: #ece3fd;
    }
    html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; color: var(--ink); }
    .stApp { background: var(--paper); }
    h1, h2, h3, .display { font-family: 'Fraunces', serif !important; color: var(--ink); letter-spacing: -0.01em; }
    .block-container { padding-top: 2.5rem; max-width: 1050px; }

    section[data-testid="stSidebar"] { background: linear-gradient(180deg, #3b1d78 0%, #2a1650 100%); }
    section[data-testid="stSidebar"] * { color: #f1eaff !important; }
    section[data-testid="stSidebar"] .sb-name { font-family: 'Fraunces', serif; font-size: 1.35rem; font-weight: 700; }
    section[data-testid="stSidebar"] .sb-sub { font-size: .85rem; opacity: .75; margin-bottom: 1rem; }
    section[data-testid="stSidebar"] label { font-size: 1rem; padding: .2rem 0; }

    .hero-title { font-family: 'Fraunces', serif; font-size: clamp(2.4rem, 6vw, 4rem); font-weight: 700; line-height: 1.05; margin: .2rem 0 .8rem 0; }
    .hero-sub { font-size: 1.2rem; color: var(--muted); max-width: 42rem; line-height: 1.55; }
    .pill { display: inline-block; background: var(--accent-soft); color: var(--accent); border-radius: 999px;
            padding: .22rem .75rem; margin: .15rem .25rem .15rem 0; font-size: .85rem; font-weight: 500; }
    .card { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 1.25rem 1.4rem; margin-bottom: 1rem; }
    .card h3 { margin: 0 0 .15rem 0; font-size: 1.3rem; }
    .meta { color: var(--muted); font-size: .9rem; margin-bottom: .6rem; }
    .stat { border-left: 3px solid var(--accent); padding-left: .8rem; }
    .stat b { font-size: 1.15rem; display: block; }
    .stat span { color: var(--muted); font-size: .9rem; }
    .badge-wip { background: #fff1d6; color: #8a5a00; border-radius: 6px; padding: .1rem .5rem; font-size: .75rem; font-weight: 600; }
    .section-intro { color: var(--muted); max-width: 40rem; margin-bottom: 1.5rem; }
    a { color: var(--accent) !important; }
    .stButton > button, .stDownloadButton > button, .stLinkButton > a, .stFormSubmitButton > button {
        border-radius: 8px; border: 1px solid var(--accent); color: var(--accent); background: #fff; font-weight: 500;
    }
    .stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover, .stLinkButton > a:hover {
        background: var(--accent); color: #fff !important; border-color: var(--accent);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# DATA (taken from the resume)
# ----------------------------------------------------------------------------
SKILLS = {
    "Programming": ["Python"],
    "Data & Visualization": ["NumPy", "Pandas", "Matplotlib", "Seaborn"],
    "Machine Learning": ["Machine Learning", "Scikit-learn"],
    "NLP & LLM Applications": ["NLP", "LLMs", "RAG", "Text Embeddings"],
    "Frameworks & Tools": ["LangChain", "ChromaDB", "Streamlit", "Groq"],
    "Databases": ["MySQL", "ChromaDB"],
    "Core Concepts": ["OOP", "DBMS"],
    "Tools & Platforms": ["Git", "GitHub", "VS Code", "Jupyter Notebook", "Google Colab"],
}

PROJECTS = [
    {
        "title": "Intelligent Document Q&A Chatbot using RAG",
        "stack": ["Python", "LangChain", "RAG", "LLM", "ChromaDB", "Streamlit", "Groq"],
        "points": [
            "Built a RAG-based app where users upload PDF documents and ask context-aware questions.",
            "Implemented document processing, text chunking, embeddings and vector similarity search to retrieve relevant information.",
            "Integrated a Groq-hosted LLM with retrieved context to generate grounded answers and reduce hallucinations.",
            "Added source and page references to make answers transparent and reliable.",
        ],
        "link": "https://github.com/surajshinde12/Intelligent-Document-QA-Chatbot",
        "wip": False,
    },
    {
        "title": "Autonomous AI Agent for Task Automation",
        "stack": ["Python", "LangChain", "LLM", "Tool Calling", "AI Agents", "Streamlit", "Groq"],
        "points": [
            "Developed an LLM-based agent that understands user requests and decides when tools are required.",
            "Implemented tool calling and multi-step agent workflows to execute tasks and process tool outputs.",
            "Designed the workflow to check whether a tool is needed before generating the final response.",
            "Built an interactive interface to submit tasks and monitor agent responses.",
        ],
        "link": "",
        "wip": False,
    },
    {
        "title": "LLM & RAG Evaluation System with Machine Learning",
        "stack": ["Python", "Scikit-learn", "NLP", "LLMs", "RAG"],
        "points": [
            "Developing a system to analyze the quality of LLM- and RAG-generated responses.",
            "Working on criteria such as correctness, relevance, faithfulness, completeness and retrieval quality.",
            "Building an ML pipeline to classify AI-generated responses from extracted evaluation features.",
            "Creating a Streamlit interface to analyze results and find weaknesses in LLM/RAG responses.",
        ],
        "link": "",
        "wip": True,
    },
]

# For each certificate:
#   "image": file name inside assets/certificates/ (png, jpg or webp)
#   "link":  optional verification / credential URL (leave "" if none)
CERTIFICATES = [
    {
        "title": "Machine Learning",
        "issuer": "LearnTube & CampusX",
        "detail": "Course certification covering machine learning concepts and algorithms.",
        "image": "machine_learning.png",
        "link": "",
    },
    {
        "title": "Deep Learning",
        "issuer": "LearnTube & CampusX",
        "detail": "Course certification covering deep learning and neural networks.",
        "image": "deep_learning.png",
        "link": "",
    },
    {
        "title": "Generative AI",
        "issuer": "LearnTube & CampusX",
        "detail": "Course certification covering generative AI and LLM-based applications.",
        "image": "genai.png",
        "link": "",
    },
]

EXPERIENCE = [
    {
        "title": "Event Coordinator, SAAI, RIT",
        "period": "May 2024 – May 2025",
        "detail": "Coordinated a gaming event and helped lead a state-level technical fest at RIT Sangli "
                  "with 300+ participants across gaming events.",
    },
]


def pills(items):
    return "".join(f'<span class="pill">{i}</span>' for i in items)


# ----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------------------------
PAGES = [
    "🏠 Home",
    "👨‍💻 About Me",
    "🛠️ Skills",
    "🚀 Projects",
    "📜 Certificates",
    "📄 Resume",
    "📬 Contact",
]

with st.sidebar:
    st.markdown(f'<div class="sb-name">{NAME}</div><div class="sb-sub">{LOCATION}</div>', unsafe_allow_html=True)
    page = st.radio("Navigate", PAGES, label_visibility="collapsed")
    st.markdown("---")
    st.markdown(f"[GitHub]({GITHUB})  \n[LinkedIn]({LINKEDIN})  \n[{EMAIL}](mailto:{EMAIL})")


# ----------------------------------------------------------------------------
# PAGES
# ----------------------------------------------------------------------------
def home():
    st.markdown(f"<div class='meta'>Hi, I'm</div><div class='hero-title'>{NAME}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-sub'>{TAGLINE}. I turn documents and tools into assistants that give grounded, "
                "checkable answers.</div>", unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns([1, 1, 3])
    with c1:
        if CV_PATH.exists():
            st.download_button("Download resume", CV_PATH.read_bytes(), "Suraj_Shinde_CV.pdf", "application/pdf")
    with c2:
        st.link_button("View GitHub", GITHUB)

    st.write("")
    s1, s2, s3 = st.columns(3)
    s1.markdown("<div class='stat'><b>3 projects</b><span>RAG, agents and LLM evaluation</span></div>", unsafe_allow_html=True)
    s2.markdown("<div class='stat'><b>CSE (AI & ML)</b><span>RIT Sangli, graduating June 2026</span></div>", unsafe_allow_html=True)
    s3.markdown("<div class='stat'><b>300+ participants</b><span>at a state-level tech fest I helped lead</span></div>", unsafe_allow_html=True)

    st.write("")
    st.subheader("What I work with")
    st.markdown(pills(["Python", "LangChain", "RAG", "ChromaDB", "Groq", "Scikit-learn", "Streamlit"]), unsafe_allow_html=True)


def about():
    st.title("About Me")
    st.markdown(
        "<div class='section-intro'>I'm a final-year Computer Science (AI & ML) student from Satara, Maharashtra, "
        "focused on practical LLM applications.</div>",
        unsafe_allow_html=True,
    )
    left, right = st.columns([3, 2], gap="large")
    with left:
        st.markdown(
            "I enjoy building things that make language models more reliable: retrieval pipelines that cite their "
            "sources, agents that decide when to call a tool, and evaluation systems that show where an answer "
            "falls short.\n\n"
            "My work so far uses Python, LangChain, ChromaDB and Groq-hosted models, with Streamlit for fast, usable "
            "interfaces. Beyond code, I've coordinated events at my college, including a state-level technical fest, "
            "which taught me to plan, delegate and work under deadlines."
        )
        st.subheader("Experience")
        for e in EXPERIENCE:
            st.markdown(
                f"<div class='card'><h3>{e['title']}</h3><div class='meta'>{e['period']}</div>{e['detail']}</div>",
                unsafe_allow_html=True,
            )
    with right:
        st.subheader("Education")
        st.markdown(
            """
            <div class='card'><h3>B.Tech, CSE (AI & ML)</h3>
            <div class='meta'>Rajarambapu Institute of Technology, Sangli<br>Nov 2022 – June 2026</div>
            CGPA: 7.32</div>
            <div class='card'><h3>HSC (PCM)</h3>
            <div class='meta'>Karmaveer Bhaurao Patil Jr. College, Bhuinj<br>Aug 2020 – March 2022</div>
            Percentage: 62.83%</div>
            """,
            unsafe_allow_html=True,
        )


def skills():
    st.title("Skills")
    st.markdown("<div class='section-intro'>Tools and concepts I use to build and evaluate AI applications.</div>", unsafe_allow_html=True)
    cols = st.columns(2, gap="large")
    for i, (group, items) in enumerate(SKILLS.items()):
        with cols[i % 2]:
            st.markdown(f"<div class='card'><h3>{group}</h3><div style='margin-top:.6rem'>{pills(items)}</div></div>", unsafe_allow_html=True)


def projects():
    st.title("Projects")
    st.markdown("<div class='section-intro'>Hands-on work with retrieval, agents and evaluation of LLM output.</div>", unsafe_allow_html=True)
    for p in PROJECTS:
        badge = " <span class='badge-wip'>In progress</span>" if p["wip"] else ""
        points = "".join(f"<li>{x}</li>" for x in p["points"])
        st.markdown(
            f"<div class='card'><h3>{p['title']}{badge}</h3>"
            f"<div style='margin:.5rem 0 .7rem 0'>{pills(p['stack'])}</div><ul>{points}</ul></div>",
            unsafe_allow_html=True,
        )
        if p["link"]:
            st.link_button("View code", p["link"], key=p["title"])


def find_cert_image(name):
    """Find the image even if the capital letters or the extension differ."""
    exact = CERT_DIR / name
    if exact.exists():
        return exact
    if CERT_DIR.exists():
        stem = Path(name).stem.lower()
        for f in CERT_DIR.iterdir():
            if f.stem.lower() == stem and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                return f
    return None


@st.dialog("Certificate", width="large")
def show_certificate(cert):
    """Pop-up that shows the certificate image."""
    st.markdown(f"**{cert['title']}**  \n{cert['issuer']}")
    img = find_cert_image(cert["image"])
    if img:
        st.image(str(img))
    else:
        found = sorted(f.name for f in CERT_DIR.iterdir()) if CERT_DIR.exists() else []
        st.warning(
            f"Could not find '{cert['image']}' in assets/certificates/. "
            f"Files found there: {found if found else 'none (folder missing or empty)'}"
        )
    if cert.get("link"):
        st.link_button("Verify online", cert["link"])


def certificates():
    st.title("Certificates")
    st.markdown("<div class='section-intro'>Courses and certifications I've completed.</div>", unsafe_allow_html=True)
    for i, c in enumerate(CERTIFICATES):
        st.markdown(
            f"<div class='card' style='margin-bottom:.5rem'><h3>{c['title']}</h3>"
            f"<div class='meta'>{c['issuer']}</div>{c['detail']}</div>",
            unsafe_allow_html=True,
        )
        if st.button("View certificate", key=f"cert_{i}"):
            show_certificate(c)
        st.write("")


def resume():
    st.title("Resume")
    if not CV_PATH.exists():
        st.warning("Resume file not found. View it here: "
                   "https://drive.google.com/file/d/1VZ60Qp2KFSG9ryGrlVXgA5Me5jmwotzx/view?usp=drivesdk")
        return
    data = CV_PATH.read_bytes()
    st.download_button("Download resume (PDF)", data, "Suraj_Shinde_CV.pdf", "application/pdf")
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="900" '
        'style="border:1px solid #e3d9f5;border-radius:10px;margin-top:1rem"></iframe>',
        unsafe_allow_html=True,
    )


def contact():
    st.title("Contact")
    st.markdown("<div class='section-intro'>Open to internships and entry-level roles in AI/ML. Send a message and your email app will open with it ready to send.</div>", unsafe_allow_html=True)
    left, right = st.columns([3, 2], gap="large")
    with left:
        with st.form("contact"):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            msg = st.text_area("Message", height=160)
            sent = st.form_submit_button("Write email")
        if sent:
            if not (name and msg):
                st.error("Enter your name and a message first.")
            else:
                body = f"{msg}\n\nFrom: {name} ({email})"
                href = f"mailto:{EMAIL}?subject={quote('Portfolio message from ' + name)}&body={quote(body)}"
                st.success("Ready to send.")
                st.link_button("Open in email app", href)
    with right:
        st.markdown(
            f"""
            <div class='card'><h3>Details</h3>
            <p>📧 <a href="mailto:{EMAIL}">{EMAIL}</a></p>
            <p>📞 {PHONE}</p>
            <p>📍 {LOCATION}</p>
            <p>🔗 <a href="{LINKEDIN}">LinkedIn</a></p>
            <p>💻 <a href="{GITHUB}">GitHub</a></p></div>
            """,
            unsafe_allow_html=True,
        )


ROUTES = {
    PAGES[0]: home,
    PAGES[1]: about,
    PAGES[2]: skills,
    PAGES[3]: projects,
    PAGES[4]: certificates,
    PAGES[5]: resume,
    PAGES[6]: contact,
}
ROUTES[page]()