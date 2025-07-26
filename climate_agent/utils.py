# climate_agent/utils.py

import os

def save_documents(documents, folder="data/raw"):
    os.makedirs(folder, exist_ok=True)

    for i, doc in enumerate(documents):
        filename = os.path.join(folder, f"doc_{i+1}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(doc.page_content)

        # Optional: save metadata separately
        meta_file = os.path.join(folder, f"doc_{i+1}_meta.txt")
        with open(meta_file, "w", encoding="utf-8") as mf:
            mf.write(str(doc.metadata))
