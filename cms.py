import streamlit as st
from supabase import create_client

BUCKET = "raj-studio-media"

DEFAULT_CONTENT = {
    "site_name": "Raj Studios Solapur",
    "tagline": "Orchestra • Live Music • Unforgettable Celebrations",
    "logo_path": "",
    "about_heading": "About Raj Studios Solapur",
    "about_text": "Raj Studios Solapur brings music, artists and audiences together through memorable live performances and celebrations.",
    "services": [
        {"name": "Orchestra Shows", "description": "Live Hindi and Marathi music performances."},
        {"name": "Event Entertainment", "description": "Professional entertainment for your special occasions."}
    ],
    "profiles": [],
    "gallery": [],
    "contact_heading": "Contact Us",
    "contact": {"phone": "7507552822", "whatsapp": "9923181017", "email": ""},
    "social": {"instagram": "", "facebook": "", "youtube": ""},
    "footer_text": "© Raj Studios Solapur. All rights reserved.",
    "accent_color": "#c52b48",
    "background_color": "#101018",
    "text_color": "#ffffff"
}

def get_supabase():
    # Keep one client per Streamlit session so the Supabase Auth session survives reruns.
    if "_supabase_client" not in st.session_state:
        url = st.secrets.get("SUPABASE_URL", "")
        key = st.secrets.get("SUPABASE_ANON_KEY", "")
        if not url or not key:
            raise RuntimeError("Missing Supabase URL or anon key")
        st.session_state["_supabase_client"] = create_client(url, key)
    return st.session_state["_supabase_client"]

def load_site_content(sb, published=False):
    row = sb.table("site_content").select("content").eq("id", 1).maybe_single().execute()
    if not row.data:
        return DEFAULT_CONTENT.copy()
    data = row.data["content"]
    selected = data.get("published" if published else "draft") or DEFAULT_CONTENT
    # Preserve defaults for newly introduced fields while keeping saved edits.
    merged = DEFAULT_CONTENT.copy()
    merged.update(selected)
    merged["contact"] = {**DEFAULT_CONTENT["contact"], **selected.get("contact", {})}
    merged["social"] = {**DEFAULT_CONTENT["social"], **selected.get("social", {})}
    return merged

def save_draft(sb, content):
    current = sb.table("site_content").select("content").eq("id", 1).maybe_single().execute()
    wrapper = current.data["content"] if current.data else {}
    wrapper["draft"] = content
    sb.table("site_content").upsert({"id": 1, "content": wrapper}).execute()

def publish(sb):
    current = sb.table("site_content").select("content").eq("id", 1).single().execute()
    wrapper = current.data["content"]
    wrapper["published"] = wrapper.get("draft", DEFAULT_CONTENT)
    sb.table("site_content").update({"content": wrapper}).eq("id", 1).execute()

def public_image_url(sb, path):
    if not path: return None
    return sb.storage.from_(BUCKET).get_public_url(path)

def upload_image(sb, uploaded, folder):
    if uploaded is None: return ""
    safe_name = uploaded.name.replace(" ", "_")
    path = f"{folder}/{__import__('uuid').uuid4().hex}_{safe_name}"
    sb.storage.from_(BUCKET).upload(path, uploaded.getvalue(), {"content-type": uploaded.type, "upsert": "false"})
    return path

def delete_image(sb, path):
    if path:
        sb.storage.from_(BUCKET).remove([path])

def is_admin(sb, user_id):
    result = sb.table("admin_users").select("user_id").eq("user_id", user_id).maybe_single().execute()
    return bool(result.data)
