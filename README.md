# Volta ecosystem

Static sites, one Vercel project per folder (root directory = folder name). Rebuild with `python3 build/build.py` (writes to `../sites`).

| Folder | Preview link | Access |
|---|---|---|
| volta-group | https://volta-group.vercel.app | Public preview (front door) |
| volta-group /partners | https://volta-group.vercel.app/partners | Partner password |
| team-volta | https://team-volta.vercel.app | Public preview |
| volta-management | https://volta-management.vercel.app | Public preview |
| volta-consultancy | https://volta-consultancy.vercel.app | Public preview |
| volta-intelligence | https://volta-intelligence.vercel.app | Unlisted preview |
| volta-africa | https://volta-africa.vercel.app | Partner password |

- This repository is public. Player names, coaching hours and footage links are never committed: they live in the private Supabase table `private.partner_content` and load only for signed-in partners via `/api/partner`.
- Enquiry forms post to `public.enquiries` in Supabase project `volta-crm` (insert-only for the public). The partner inbox reads them through `/api/inbox`.
- `PARTNER_PASSWORD` lives only in Vercel environment variables (volta-group, volta-africa). Its SHA-256 fingerprint is in `private.app_secrets` (name `inbox`); change both together.
- While `PREVIEW = True` in `build/shared.py`, every site is noindex. Set it to False when the real domains go live.
