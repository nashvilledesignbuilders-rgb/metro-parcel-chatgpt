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
# Metro Parcel ChatGPT

This project integrates Metro Nashville's Parcel Viewer data with ChatGPT using a FastAPI app deployed on Vercel.

---

## 🚀 Deployment on Vercel
The FastAPI app is located in the `api/` folder.  
Vercel automatically deploys endpoints under `/api/`.

---

## 🔎 Example API Usage

Get a parcel summary by PIN:

```bash
curl "https://metro-parcel-chatgpt.vercel.app/api/parcel_summary?pins=09408003000"
