import streamlit as st
from pathlib import Path
import base64

# =========================================================
# RAJ STUDIOS SOLAPUR — ORCHESTRA WEBSITE
# =========================================================

st.set_page_config(
    page_title="Raj Studios Solapur | Orchestra",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"
MEMBERS_DIR = ASSETS / "members"
LOGO = ASSETS / "logo.png"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
    --bg: #080611;
    --panel: #121021;
    --panel2: #1b1430;
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
        radial-gradient(
            circle at 15% 10%,
            rgba(143,92,255,.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 85% 18%,
            rgba(255,79,163,.16),
            transparent 26%
        ),
        radial-gradient(
            circle at 50% 75%,
            rgba(78,220,255,.08),
            transparent 30%
        ),
        var(--bg);

    color: var(--text);
}

.block-container {
    max-width: 1200px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}


/* =========================================================
   HERO
========================================================= */

.hero {
    position: relative;
    overflow: hidden;

    border-radius: 28px;

    padding: 48px 38px;

    min-height: 390px;

    display: flex;
    align-items: center;

    background:
        linear-gradient(
            115deg,
            rgba(8,6,17,.95),
            rgba(18,12,39,.82)
        ),
        radial-gradient(
            circle at 80% 20%,
            rgba(255,79,163,.25),
            transparent 30%
        );

    border: 1px solid rgba(247,198,91,.20);

    box-shadow:
        0 25px 70px rgba(0,0,0,.35);
}

.hero:before {
    content: "";

    position: absolute;

    width: 380px;
    height: 380px;

    right: -100px;
    top: -130px;

    border-radius: 50%;

    background:
        conic-gradient(
            from 120deg,
            var(--pink),
            var(--purple),
            var(--cyan),
            var(--gold),
            var(--pink)
        );

    filter: blur(70px);

    opacity: .22;

    animation:
        glow 7s ease-in-out infinite alternate;
}

@keyframes glow {

    from {
        transform: scale(.9) rotate(0deg);
        opacity: .16;
    }

    to {
        transform: scale(1.15) rotate(35deg);
        opacity: .30;
    }
}

.hero-content {
    position: relative;
    z-index: 2;

    max-width: 760px;
}

.eyebrow {
    color: var(--gold);

    letter-spacing: 4px;

    text-transform: uppercase;

    font-size: .78rem;

    font-weight: 600;
}

.hero h1 {

    font-family: 'Cinzel', serif;

    font-size:
        clamp(2.5rem, 6vw, 5rem);

    line-height: 1;

    margin:
        10px 0 18px;

    background:
        linear-gradient(
            90deg,
            #fff,
            var(--gold),
            #fff
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color:
        transparent;
}

.hero p {

    color: #d7d1e2;

    font-size: 1.08rem;

    line-height: 1.8;

    max-width: 690px;
}


/* =========================================================
   LOGO
========================================================= */

.logo-wrap {
    margin-bottom: 8px;
}

.logo-wrap img {

    max-height: 90px;

    width: auto;
}


/* =========================================================
   SECTION TITLES
========================================================= */

.section-title {

    font-family: 'Cinzel', serif;

    font-size: 2rem;

    text-align: center;

    margin:
        45px 0 8px;

    color: #fff;
}

.section-subtitle {

    text-align: center;

    color: var(--muted);

    margin-bottom: 28px;
}


/* =========================================================
   FEATURE CARDS
========================================================= */

.feature {

    background:
        rgba(18,16,33,.78);

    border:
        1px solid rgba(255,255,255,.07);

    border-radius: 20px;

    padding: 24px;

    text-align: center;

    height: 100%;

    transition:
        .3s ease;
}

.feature:hover {

    transform:
        translateY(-5px);

    border-color:
        rgba(78,220,255,.35);
}

.feature-icon {

    font-size:
        2.2rem;

    margin-bottom:
        8px;
}

.feature h3 {

    margin:
        6px 0;

    font-size:
        1.05rem;
}

.feature p {

    color:
        var(--muted);

    font-size:
        .88rem;

    line-height:
        1.6;
}


/* =========================================================
   MEMBER CARDS
========================================================= */

.member-card {

    background:
        linear-gradient(
            145deg,
            rgba(27,20,48,.96),
            rgba(13,11,24,.96)
        );

    border:
        1px solid rgba(255,255,255,.08);

    border-radius:
        22px;

    padding:
        15px;

    height:
        100%;

    box-shadow:
        0 15px 40px rgba(0,0,0,.25);

    transition:
        transform .35s ease,
        border-color .35s ease,
        box-shadow .35s ease;
}

.member-card:hover {

    transform:
        translateY(-8px);

    border-color:
        rgba(247,198,91,.55);

    box-shadow:
        0 20px 50px
        rgba(143,92,255,.18);
}

.member-photo {

    width:
        100%;

    height:
        260px;

    object-fit:
        cover;

    border-radius:
        16px;

    display:
        block;
}

.member-name {

    font-family:
        'Cinzel', serif;

    font-size:
        1.2rem;

    margin:
        15px 5px 4px;

    color:
        #fff;
}

.member-role {

    color:
        var(--gold);

    font-size:
        .88rem;

    margin:
        0 5px 10px;

    font-weight:
        600;
}

.member-phone {

    color:
        #c8c1d6;

    font-size:
        .86rem;

    margin:
        0 5px;
}


/* =========================================================
   CONTACT SECTION
========================================================= */

.contact {

    margin-top:
        50px;

    padding:
        35px 25px;

    text-align:
        center;

    border-radius:
        25px;

    background:
        linear-gradient(
            120deg,
            rgba(143,92,255,.18),
            rgba(255,79,163,.15)
        );

    border:
        1px solid rgba(247,198,91,.22);
}

.contact h2 {

    font-family:
        'Cinzel', serif;

    margin-bottom:
        8px;
}

.phone {

    font-size:
        clamp(1.35rem, 4vw, 2rem);

    font-weight:
        700;

    letter-spacing:
        1px;

    color:
        var(--gold);

    margin:
        8px 0;
}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align:
        center;

    color:
        #81798e;

    font-size:
        .78rem;

    padding:
        28px 0 8px;
}


/* =========================================================
   DIVIDER
========================================================= */

.divider {

    height:
        1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(247,198,91,.35),
            transparent
        );

    margin:
        35px 0;
}


/* =========================================================
   STREAMLIT UI CLEANUP
========================================================= */

[data-testid="stHeader"] {
    background:
        transparent;
}

[data-testid="stToolbar"] {
    display:
        none;
}

[data-testid="stDecoration"] {
    display:
        none;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# MEMBER DATA
# =========================================================
# Replace these with your actual artists.

members = [

    {
        "name": "Artist Name 1",
        "role": "Lead Vocalist",
        "phone": "Phone Number",
        "photo": "member1.jpg",
    },

    {
        "name": "Artist Name 2",
        "role": "Singer / Performer",
        "phone": "Phone Number",
        "photo": "member2.jpg",
    },

    {
        "name": "Artist Name 3",
        "role": "Keyboard Artist",
        "phone": "Phone Number",
        "photo": "member3.jpg",
    },

    {
        "name": "Artist Name 4",
        "role": "Musician",
        "phone": "Phone Number",
        "photo": "member4.jpg",
    },

    {
        "name": "Artist Name 5",
        "role": "Singer / Musician",
        "phone": "Phone Number",
        "photo": "member5.jpg",
    },

    {
        "name": "Artist Name 6",
        "role": "Drummer / Percussionist",
        "phone": "Phone Number",
        "photo": "member6.jpg",
    },
]


# =========================================================
# LOAD LOGO
# =========================================================

logo_html = ""

if LOGO.exists():

    encoded = base64.b64encode(
        LOGO.read_bytes()
    ).decode()

    logo_html = f"""
    <div class="logo-wrap">
        <img
            src="data:image/png;base64,{encoded}"
            alt="Raj Studios Solapur Logo"
        >
    </div>
    """


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    f"""
    <section class="hero">

        <div class="hero-content">

            {logo_html}

            <div class="eyebrow">
                Solapur • Maharashtra
            </div>

            <h1>
                Raj Studios
            </h1>

            <p>

                <strong>
                    Orchestra • Live Music • Singing • Entertainment
                </strong>

                <br>

                Bringing soulful voices,
                vibrant music and unforgettable
                live performances to celebrations,
                cultural programs and special occasions
                across Solapur.

            </p>

        </div>

    </section>
    """,
    unsafe_allow_html=True
)


# =========================================================
# ABOUT SECTION
# =========================================================

st.markdown(
    """
    <div class="section-title">
        The Sound of Raj Studios
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-subtitle">

        A passionate orchestra team from Solapur,
        bringing music to every celebration.

    </div>
    """,
    unsafe_allow_html=True
)


features = [

    (
        "🎤",
        "Live Singing",
        "Powerful vocals and engaging performances for every audience."
    ),

    (
        "🎹",
        "Live Orchestra",
        "A talented team of singers and musicians working together."
    ),

    (
        "🎶",
        "Musical Variety",
        "Bollywood, Marathi, devotional, retro and popular melodies."
    ),

    (
        "✨",
        "Stage Entertainment",
        "Colourful, energetic performances designed for memorable events."
    ),

]


cols = st.columns(4)

for col, feature in zip(cols, features):

    icon, title, description = feature

    with col:

        st.markdown(
            f"""
            <div class="feature">

                <div class="feature-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {description}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# ARTISTS SECTION
# =========================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-title">
        Our Artists
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-subtitle">

        Meet the voices and musicians
        behind the Raj Studios Orchestra.

    </div>
    """,
    unsafe_allow_html=True
)


# Display 3 cards per row

for start in range(
    0,
    len(members),
    3
):

    row = members[
        start:start + 3
    ]

    cols = st.columns(
        len(row)
    )

    for col, member in zip(
        cols,
        row
    ):

        with col:

            photo_path = (
                MEMBERS_DIR /
                member["photo"]
            )

            # ---------------------------------
            # Artist photo
            # ---------------------------------

            if photo_path.exists():

                extension = (
                    photo_path
                    .suffix
                    .lower()
                    .replace(".", "")
                )

                if extension in [
                    "jpg",
                    "jpeg"
                ]:
                    mime = "jpeg"
                else:
                    mime = extension

                encoded = base64.b64encode(
                    photo_path.read_bytes()
                ).decode()

                image_html = f"""
                <img
                    class="member-photo"
                    src="data:image/{mime};base64,{encoded}"
                    alt="{member['name']}"
                >
                """

            else:

                image_html = """
                <div
                    class="member-photo"
                    style="
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        background:
                            linear-gradient(
                                135deg,
                                #21163a,
                                #0c0a15
                            );
                        font-size:4rem;
                    "
                >
                    🎤
                </div>
                """


            # ---------------------------------
            # Card
            # ---------------------------------

            st.markdown(
                f"""
                <div class="member-card">

                    {image_html}

                    <div class="member-name">
                        {member["name"]}
                    </div>

                    <div class="member-role">
                        {member["role"]}
                    </div>

                    <div class="member-phone">
                        📞 {member["phone"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# CONTACT / BOOKING SECTION
# =========================================================

st.markdown(
    """
    <div class="contact">

        <h2>
            Book Raj Studios Orchestra
        </h2>

        <p style="color:#c8c1d6;">

            For programs, events,
            celebrations and live musical performances

        </p>

        <div class="phone">
            7507552822
        </div>

        <div class="phone">
            9923181017
        </div>

        <p
            style="
                color:#9e96aa;
                margin-top:18px;
            "
        >
            📍 Solapur, Maharashtra
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        © 2026 Raj Studios Solapur
        • Orchestra & Live Music
        • All Rights Reserved

    </div>
    """,
    unsafe_allow_html=True
)