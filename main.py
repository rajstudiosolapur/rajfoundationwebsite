import streamlit as st
from html import escape
from urllib.parse import quote
from textwrap import dedent

# =========================================================
# RAJ STUDIOS SOLAPUR — ORCHESTRA WEBSITE
# =========================================================
st.set_page_config(
    page_title="Raj Studios Solapur | Orchestra",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# HTML RENDER HELPER
# =========================================================
def render_html(html: str) -> None:
    """Render HTML safely without showing the source code."""
    st.markdown(dedent(html).strip(), unsafe_allow_html=True)

# =========================================================
# GITHUB ASSETS
# =========================================================
GITHUB_RAW = (
    "https://raw.githubusercontent.com/"
    "rajstudiosolapur/rajfoundationwebsite/main/"
)
LOGO_URL = GITHUB_RAW + "logo.png"

# =========================================================
# CUSTOM CSS
# =========================================================
render_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
    --bg: #080611;
    --panel: #121021;
    --gold: #f7c65b;
    --pink: #ff4fa3;
    --purple: #8f5cff;
    --cyan: #4edcff;
    --text: #f7f4ff;
    --muted: #b9b2c9;
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(143,92,255,.22), transparent 28%),
        radial-gradient(circle at 85% 18%, rgba(255,79,163,.16), transparent 26%),
        radial-gradient(circle at 50% 75%, rgba(78,220,255,.08), transparent 30%),
        var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1200px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

/* HERO */
.hero {
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    padding: 48px 38px;
    min-height: 390px;
    display: flex;
    align-items: center;
    background:
        linear-gradient(115deg, rgba(8,6,17,.96), rgba(18,12,39,.88)),
        radial-gradient(circle at 80% 20%, rgba(255,79,163,.25), transparent 30%);
    border: 1px solid rgba(247,198,91,.20);
    box-shadow: 0 25px 70px rgba(0,0,0,.35);
}

.hero:before {
    content: "";
    position: absolute;
    width: 380px;
    height: 380px;
    right: -100px;
    top: -130px;
    border-radius: 50%;
    background: conic-gradient(
        from 120deg,
        var(--pink),
        var(--purple),
        var(--cyan),
        var(--gold),
        var(--pink)
    );
    filter: blur(70px);
    opacity: .22;
    animation: glow 7s ease-in-out infinite alternate;
}

@keyframes glow {
    from { transform: scale(.9) rotate(0deg); opacity: .16; }
    to   { transform: scale(1.15) rotate(35deg); opacity: .30; }
}

/* HERO CONTENT - CENTERED */
.hero-content {
    position: relative;
    z-index: 2;
    max-width: 760px;
    margin: 0 auto;          /* centers the content */
    text-align: center;      /* centers text + logo */
}

/* LOGO - CIRCULAR */
.logo-wrap {
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
}

.logo-wrap img {
    width: 130px;            /* fixed size for perfect circle */
    height: 130px;
    object-fit: cover;       /* important for circular crop */
    border-radius: 50%;      /* makes it circular */
    border: 3px solid rgba(247, 198, 91, 0.6);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

/* HERO TEXT */
.eyebrow {
    color: var(--gold);
    letter-spacing: 4px;
    text-transform: uppercase;
    font-size: .78rem;
    font-weight: 600;
}
.hero h1 {
    font-family: 'Cinzel', serif;
    font-size: clamp(2.5rem, 6vw, 5rem);
    line-height: 1;
    margin: 10px 0 18px;
    background: linear-gradient(90deg, #ffffff, var(--gold), #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    color: #d7d1e2;
    font-size: 1.08rem;
    line-height: 1.8;
    max-width: 690px;
}

/* SECTION TITLES */
.section-title {
    font-family: 'Cinzel', serif;
    font-size: 2rem;
    text-align: center;
    margin: 45px 0 8px;
    color: #ffffff;
}
.section-subtitle {
    text-align: center;
    color: var(--muted);
    margin-bottom: 28px;
}

/* FEATURE CARDS */
.feature {
    background: rgba(18,16,33,.78);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    height: 100%;
    transition: .3s ease;
}
.feature:hover {
    transform: translateY(-6px);
    border-color: rgba(78,220,255,.40);
    box-shadow: 0 15px 40px rgba(78,220,255,.08);
}
.feature-icon {
    font-size: 2.2rem;
    margin-bottom: 8px;
}
.feature h3 {
    margin: 6px 0;
    font-size: 1.05rem;
}
.feature p {
    color: var(--muted);
    font-size: .88rem;
    line-height: 1.6;
}

/* MEMBER CARDS */
.member-card {
    background: linear-gradient(145deg, rgba(27,20,48,.96), rgba(13,11,24,.96));
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 22px;
    padding: 15px;
    height: 100%;
    box-shadow: 0 15px 40px rgba(0,0,0,.25);
    transition: transform .35s ease, border-color .35s ease, box-shadow .35s ease;
}
.member-card:hover {
    transform: translateY(-8px);
    border-color: rgba(247,198,91,.55);
    box-shadow: 0 20px 50px rgba(143,92,255,.18);
}

.member-photo-wrap {
    position: relative;
    width: 100%;
    height: 260px;
    overflow: hidden;
    border-radius: 16px;
    background: rgba(255,255,255,.04);
}

.member-photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    border-radius: 16px;
    display: block;
}

.photo-fallback {
    position: absolute;
    inset: 0;
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    color: var(--muted);
    font-size: 2.4rem;
    background: linear-gradient(145deg, rgba(27,20,48,.96), rgba(13,11,24,.96));
}
.photo-fallback span {
    margin-top: 8px;
    font-size: .8rem;
    letter-spacing: .5px;
}

.member-name {
    font-family: 'Cinzel', serif;
    font-size: 1.2rem;
    margin: 15px 5px 4px;
    color: #ffffff;
}
.member-role {
    color: var(--gold);
    font-size: .88rem;
    margin: 0 5px 10px;
    font-weight: 600;
}
.member-phone {
    color: #c8c1d6;
    font-size: .86rem;
    margin: 0 5px;
}

/* CONTACT SECTION */
.contact {
    margin-top: 50px;
    padding: 40px 25px;
    text-align: center;
    border-radius: 25px;
    background: linear-gradient(120deg, rgba(143,92,255,.18), rgba(255,79,163,.15));
    border: 1px solid rgba(247,198,91,.22);
    box-shadow: 0 20px 60px rgba(0,0,0,.20);
}
.contact h2 {
    font-family: 'Cinzel', serif;
    margin-bottom: 8px;
    font-size: 2rem;
}
.phone {
    font-size: clamp(1.35rem, 4vw, 2rem);
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--gold);
    margin: 8px 0;
}

/* DIVIDER */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(247,198,91,.35), transparent);
    margin: 35px 0;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #81798e;
    font-size: .78rem;
    padding: 28px 0 8px;
}

/* STREAMLIT CLEANUP */
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }

/* MOBILE */
@media (max-width: 768px) {
    .hero {
        padding: 35px 24px;
        min-height: 420px;
    }
    .hero h1 { font-size: 3rem; }
    .hero p { font-size: .95rem; }
    .section-title { font-size: 1.6rem; }
    .member-photo-wrap { height: 300px; }
}
</style>
""")

# =========================================================
# MEMBER DATA
# =========================================================
members = [
    {
        "name": "Atul Swami",
        "role": "Founder & Managing Director of Raj Studio Solapur",
        "phone": "7507552822",
        "photo": "artist1.jpg",
    },
    {
        "name": "Dhanashri Sargule",
        "role": "President of Orchestra Dhanashri.",
        "phone": "9923181017",
        "photo": "artist2.jpg",
    },
    {
        "name": "Vinayak Sargule",
        "role": "Co-Founder of Raj Studio Solapur",
        "phone": "9923181017",
        "photo": "artist3.jpg",
    },
    {
        "name": "Bhakti Mahamuni",
        "role": "Singer",
        "phone": "7507552822",
        "photo": "artist4.jpg",
    },
    {
        "name": "Rahul Koulgud",
        "role": "Secretary of Raj Studio",
        "phone": "Phone Number",
        "photo": "artist5.png",
    },
    {
        "name": "Artist Name 6",
        "role": "Musician",
        "phone": "Phone Number",
        "photo": "artist6.jpg",
    },
]

# =========================================================
# HERO SECTION
# =========================================================
render_html(f"""
<section class="hero">
    <div class="hero-content">
        <div class="logo-wrap">
            <img src="{escape(LOGO_URL)}" alt="Raj Studios Solapur Logo">
        </div>
        <div class="eyebrow">Solapur • Maharashtra</div>
        <h1>Raj Studios</h1>
        <p>
            <strong>Orchestra • Live Music • Singing • Entertainment</strong><br>
            Bringing soulful voices, vibrant music and unforgettable
            live performances to celebrations, cultural programs and
            special occasions across Solapur.
        </p>
    </div>
</section>
""")

# =========================================================
# ABOUT SECTION
# =========================================================
render_html("""
<div class="section-title">The Sound of Raj Studios</div>
<div class="section-subtitle">
    A passionate orchestra team from Solapur,
    bringing music to every celebration.
</div>
""")

# =========================================================
# FEATURES
# =========================================================
features = [
    ("🎤", "Live Singing", "Powerful vocals and engaging performances for every audience."),
    ("🎹", "Live Orchestra", "A talented team of singers and musicians working together."),
    ("🎶", "Musical Variety", "Bollywood, Marathi, devotional, retro and popular melodies."),
    ("✨", "Stage Entertainment", "Colourful and energetic performances for memorable events."),
]

cols = st.columns(4)
for col, (icon, title, description) in zip(cols, features):
    with col:
        render_html(f"""
        <div class="feature">
            <div class="feature-icon">{escape(icon)}</div>
            <h3>{escape(title)}</h3>
            <p>{escape(description)}</p>
        </div>
        """)

# =========================================================
# ARTISTS SECTION
# =========================================================
render_html('<div class="divider"></div>')
render_html("""
<div class="section-title">Our Artists</div>
<div class="section-subtitle">
    Meet the voices and musicians behind the Raj Studios Orchestra.
</div>
""")

# =========================================================
# ARTIST CARDS
# =========================================================
for start in range(0, len(members), 3):
    row = members[start:start + 3]
    cols = st.columns(3)

    for col, member in zip(cols, row):
        with col:
            photo_url = (
                GITHUB_RAW
                + "members/"
                + quote(str(member["photo"]).lstrip("/"), safe="")
            )

            render_html(f"""
            <div class="member-card">
                <div class="member-photo-wrap">
                    <img
                        class="member-photo"
                        src="{escape(photo_url)}"
                        alt="{escape(member['name'])}"
                        loading="lazy"
                        onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                    >
                    <div class="photo-fallback">
                        🎵
                        <span>Photo coming soon</span>
                    </div>
                </div>
                <div class="member-name">{escape(member['name'])}</div>
                <div class="member-role">{escape(member['role'])}</div>
                <div class="member-phone">📞 {escape(member['phone'])}</div>
            </div>
            """)

# =========================================================
# CONTACT / BOOKING
# =========================================================
render_html("""
<div class="contact">
    <h2>Book Raj Studios Orchestra</h2>
    <p style="color:#c8c1d6;">
        For programs, events, celebrations and live musical performances
    </p>
    <div class="phone">📞 7507552822</div>
    <div class="phone">📞 9923181017</div>
    <p style="color:#9e96aa; margin-top:18px;">
        📍 Solapur, Maharashtra
    </p>
</div>
""")

# =========================================================
# FOOTER
# =========================================================
render_html("""
<div class="footer">
    © 2026 Raj Studios Solapur • Orchestra & Live Music • All Rights Reserved
</div>
""")
