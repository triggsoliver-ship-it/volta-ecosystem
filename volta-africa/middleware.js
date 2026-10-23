import { next } from '@vercel/functions';

export const config = { matcher: ["/:path*"] };

function unauthorised() {
  return new Response('Volta partner area. Please sign in with the partner password.', {
    status: 401,
    headers: { 'WWW-Authenticate': 'Basic realm="Volta partners", charset="UTF-8"', 'Cache-Control': 'no-store' },
  });
}

export default function middleware(request) {
  const expected = process.env.PARTNER_PASSWORD;
  if (!expected) return unauthorised();
  const header = request.headers.get('authorization') || '';
  if (!header.startsWith('Basic ')) return unauthorised();
  let decoded = '';
  try { decoded = atob(header.slice(6)); } catch (e) { return unauthorised(); }
  const password = decoded.slice(decoded.indexOf(':') + 1);
  if (password.length !== expected.length) return unauthorised();
  let diff = 0;
  for (let i = 0; i < password.length; i++) diff |= password.charCodeAt(i) ^ expected.charCodeAt(i);
  if (diff !== 0) return unauthorised();
  return next({ headers: { 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow' } });
}
