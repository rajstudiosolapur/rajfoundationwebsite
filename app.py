import streamlit as st
from html import escape
from cms import get_supabase, load_site_content, DEFAULT_CONTENT, public_image_url

st.set_page_config(page_title="Raj Studios Solapur", page_icon="🎵", layout="wide")

try:
    sb = get_supabase()
    content = load_site_content(sb, published=True) or DEFAULT_CONTENT
except Exception as e:
    st.error("Website setup is incomplete. Please configure Supabase secrets. See README.md.")
    st.stop()

def section_title(text):
    st.markdown(f"## {text}")

cfg = content
st.markdown(f"""
<style>
:root {{ --accent: {cfg.get('accent_color','#b51f36')}; --background: {cfg.get('background_color','#101018')}; }}
.stApp {{ background: var(--background); color: {cfg.get('text_color','#ffffff')}; }}
.hero {{ padding: 3rem 1.5rem; border-radius: 18px; text-align:center;
         background: linear-gradient(135deg, #161625, #35202c); }}
.hero h1 {{ font-size: clamp(2.2rem, 5vw, 4rem); margin-bottom:.25rem; }}
.hero p {{ font-size:1.15rem; opacity:.9; }}
a {{ color: var(--accent); }}
</style>
""", unsafe_allow_html=True)

logo = public_image_url(sb, cfg.get("logo_path", ""))
if logo:
    st.image(logo, width=130)
st.markdown(f"""<div class="hero"><h1>{escape(str(cfg.get('site_name','Raj Studios Solapur')))}</h1>
<p>{escape(str(cfg.get('tagline','Music • Events • Memories')))}</p></div>""", unsafe_allow_html=True)

st.write("")
section_title(cfg.get("about_heading", "About Us"))
st.write(cfg.get("about_text", ""))
services = cfg.get("services", [])
if services:
    section_title("Our Services")
    cols = st.columns(min(3, len(services)))
    for i, service in enumerate(services):
        with cols[i % len(cols)]:
            st.markdown(f"### {service.get('name','Service')}")
            st.write(service.get("description", ""))

profiles = cfg.get("profiles", [])
if profiles:
    section_title("Our Artists")
    cols = st.columns(min(3, len(profiles)))
    for i, person in enumerate(profiles):
        with cols[i % len(cols)]:
            url = public_image_url(sb, person.get("photo_path", ""))
            if url: st.image(url, use_container_width=True)
            st.markdown(f"### {person.get('name','Artist')}")
            st.caption(person.get("designation", ""))
            if person.get("phone"): st.write(person["phone"])

gallery = cfg.get("gallery", [])
if gallery:
    section_title("Gallery")
    cols = st.columns(3)
    for i, item in enumerate(gallery):
        with cols[i % 3]:
            url = public_image_url(sb, item.get("path", ""))
            if url: st.image(url, use_container_width=True)

section_title(cfg.get("contact_heading", "Contact Us"))
contact = cfg.get("contact", {})
contact_cols = st.columns(3)
with contact_cols[0]: st.write("**Phone**"); st.write(contact.get("phone", ""))
with contact_cols[1]: st.write("**WhatsApp**"); st.write(contact.get("whatsapp", ""))
with contact_cols[2]: st.write("**Email**"); st.write(contact.get("email", ""))

social = cfg.get("social", {})
links = [("Instagram", social.get("instagram")), ("Facebook", social.get("facebook")), ("YouTube", social.get("youtube"))]
st.markdown("  ·  ".join(f"[{name}]({url})" for name, url in links if url))
st.divider()
st.caption(cfg.get("footer_text", "© Raj Studios Solapur. All rights reserved."))
