# ai-models-catalog-api 🧠
A simple and free API that lists AI models usable via API from top providers. Instantly access to real time updated model names, descriptions and metadata.

No API key needed, it currently suppors OpenAI, Google (Gemini), DeepSeek and Anthropic.

# 🔍🚀 Overview & Usage
Ideal for anyone needing a simple, unified way to track available AI models across multiple providers.

Perfect for building dashboards, automating logic, or comparing options, without the hassle of managing API keys or dealing with multiple requests and inconsistent response formats.


## ✅ **Get only Google models (example):**

### Via Browser:

    https://3eurotools.it/models-info?company=google

### Via Python:
    import requests

    url = "https://3eurotools.it/models-info"
    params = {
        "company": "google",
    }
    
    response = requests.get(url, params=params)
    print(response.text)

***
**Sample Response:**

```json
{
  "model_names": ["gemini-2.5-pro-preview-06-05", ..., "gemini-2.0-flash-thinking-exp-01-21"],
  "detailed_version": [
    // model details here
  ],
  "last_updated_timestamp": 1750290515.4080338,
  "last_updated_human": "2025-06-18T23:48:35.408034",
  "error": null
}
```
---
## 🌐 Get models from all supported providers:


### Via Browser:

    https://3eurotools.it/models-info

### Via Python:
    import requests

    url = "https://3eurotools.it/models-info"
    
    response = requests.get(url)
    print(response.text)

---

**Sample Response:**
```json

{
  "google": {
    // model IDs and metadata
  },

  "anthropic": {
    // model IDs and metadata
  },

  "openai": {
    // model IDs and metadata
  },

  "deepseek": {
    // model IDs and metadata
  }
}
```

---

## Limits and quotas

The service is free to use, including for commercial purposes. Requests are unlimited, but avoid making too many in a short time: you have a credit of 100 requests, which replenishes at a rate of 1 request per second.
To increase the limits and remove the attribution requirement (which is mandatory in public projects), contact me at: d.sagona.20@gmail.com
