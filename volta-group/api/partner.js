// Partner-only content (player review, showcase footage links), held privately in the database.
// Protected by middleware.js; the database also checks the partner password fingerprint.
export async function GET() {
  try {
    const r = await fetch(`${process.env.SUPABASE_URL}/rest/v1/rpc/partner_content_v1`, {
      method: 'POST',
      headers: { apikey: process.env.SUPABASE_PUBLISHABLE_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({ p_key: process.env.PARTNER_PASSWORD }),
    });
    if (!r.ok) throw new Error(String(r.status));
    return new Response(await r.text(), { headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
  } catch (e) {
    return new Response(JSON.stringify({ error: 'Unavailable' }), { status: 502, headers: { 'Content-Type': 'application/json' } });
  }
}
