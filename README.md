# Metro Parcel ChatGPT API

## Deploy to Vercel

##1. Install Vercel CLI:
##```bash
##npm i -g vercel
##vercel login
# Metro Parcel ChatGPT API

This is a FastAPI service deployed on Vercel that integrates Metro Nashville's Parcel Viewer into ChatGPT.

---

## 🚀 Deploy

1. Fork or clone this repo.
2. Push to your GitHub account.
3. Deploy to [Vercel](https://vercel.com).

---

## 🔌 Connect to ChatGPT

1. Open ChatGPT → Settings → **Custom GPTs** → Create a GPT.
2. When adding an **API schema**, upload [`openapi.json`](./openapi.json).
3. ChatGPT will automatically detect the function `get_parcel_summaries`.

---

## 🛠 Usage Examples

**Single parcel:**
