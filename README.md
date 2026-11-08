# Raj Studios Solapur — Editable Website + Admin CMS

A Streamlit public website with a separate password-protected admin dashboard. Content is stored in Supabase Postgres; uploaded media is stored in Supabase Storage.

## Security

The included SQL enables row-level security and restricts content/media writes to user IDs listed in `admin_users`. Public visitors can read the published content and public media only. Keep the Supabase service-role key private; this app does not need it. Use a strong unique admin password and enable MFA in Supabase when available.

## 1. Create Supabase backend

1. Create a project at https://supabase.com.
2. Open **SQL Editor** and run `supabase/schema.sql`.
3. In **Storage**, create a bucket named `raj-studio-media` and set it to **Public** (public read is required for this version's image URLs).
4. In **Authentication → Users**, create your admin user with an email and a strong password.
5. Copy that user's UUID. In SQL Editor run:

   ```sql
   insert into public.admin_users(user_id)
   values ('PASTE-ADMIN-USER-UUID-HERE');
   ```

6. Copy the project URL and anon/public key from **Project Settings → API**.

## 2. Configure locally

```bash
pip install -r requirements.txt
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edit `.streamlit/secrets.toml` with your Supabase URL and anon key, then run:

```bash
streamlit run app.py
```

Public site: `http://localhost:8501/`  
Admin panel: `http://localhost:8501/Admin` (Streamlit page route may appear as `/Admin`).

Login with the admin email and password created in Supabase Authentication.

## 3. Deploy

### Streamlit Community Cloud
1. Push this project to a GitHub repository.
2. Go to https://share.streamlit.io and deploy the repository, selecting `app.py`.
3. In app **Settings → Secrets**, paste the two values from `secrets.toml.example`.
4. Redeploy/reboot the app.

Your public URL is the main app URL. Admin URL is the same URL plus `/Admin`.

## CMS workflow

- Edit site name, tagline, About text, services, artist profiles, profile images, gallery, contact details, social links, footer and theme colors.
- **Save draft** stores unpublished changes in Supabase.
- **Publish changes** copies the draft to the published website content.
- Uploaded media is stored in Supabase Storage and content references are saved in Postgres.
- The public page reads only the published version.

## Production checklist

- Supabase Auth uses email/password; use your admin email as the login username.
- Enable MFA and configure Auth rate limits/CAPTCHA where appropriate.
- Back up the Supabase database and Storage bucket.
- Use optimized, compressed images for faster loading.
- Add a custom domain through the hosting provider if desired.
