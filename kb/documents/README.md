# Knowledge base documents

This folder must contain the harness knowledge base (698 JSON documents).

Copy it from the [A2A Hackathon Template](https://github.com/a2anet/a2a-hackathon-template):

```powershell
# From the pharmasafety repo root (requires git or manual download)
git clone --depth 1 https://github.com/a2anet/a2a-hackathon-template.git _template
Copy-Item -Recurse _template\kb\documents .\kb\documents
Remove-Item -Recurse -Force _template
```

Or download [kb/documents](https://github.com/a2anet/a2a-hackathon-template/tree/main/kb/documents) from GitHub and place the JSON files here.

Optional: precompute embeddings for faster startup (requires `GOOGLE_API_KEY`):

```powershell
cd cs_agent
$env:KB_DOCUMENTS_DIR = "..\kb\documents"
$env:KB_EMBEDDINGS_PATH = "..\kb\embeddings.json"
python precompute_embeddings.py
```
