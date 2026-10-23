// Private inbox API for the Volta partner hub. Protected by middleware.js (partner password).
// The database key never reaches the browser: it is the PARTNER_PASSWORD environment variable, checked by fingerprint in the database.
const URL_ = process.env.SUPABASE_URL;
const PUB = process.env.SUPABASE_PUBLISHABLE_KEY;
const KEY = process.env.PARTNER_PASSWORD; // same secret as the partner password gate

async function rpc(fn, body) {
  const r = await fetch(`${URL_}/rest/v1/rpc/${fn}`, {
    method: 'POST',
    headers: { apikey: PUB, 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const text = await r.text();
  if (!r.ok) throw new Error(`database ${r.status}`);
  return text ? JSON.parse(text) : null;
}

const json = (data, status = 200) => new Response(JSON.stringify(data), {
  status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
});

export async function GET() {
  try { return json(await rpc('partner_inbox_v2', { p_key: KEY })); }
  catch (e) { return json({ error: 'Inbox unavailable' }, 502); }
}

export async function POST(request) {
  let b;
  try { b = await request.json(); } catch (e) { return json({ error: 'Bad request' }, 400); }
  const statuses = ['new', 'contacted', 'qualified', 'won', 'closed'];
  if (!b || typeof b.id !== 'string' || !statuses.includes(b.status)) return json({ error: 'Bad request' }, 400);
  try {
    await rpc('partner_update', {
      p_key: KEY, p_id: b.id, p_status: b.status,
      p_owner: (b.owner || '').slice(0, 60) || null, p_notes: (b.notes || '').slice(0, 1000) || null,
    });
    return json({ ok: true });
  } catch (e) { return json({ error: 'Update failed' }, 502); }
}
