# 📘 Adobe India Hackathon 2025 – Round 1A: Outline Extractor

This project processes PDF files to extract a structured outline (headings like H1, H2, H3) using the `pdfminer.six` library and outputs the result as a JSON file. It is designed to be run in a Docker container with mounted `input/` and `output/` volumes.

---

## 📂 Project Structure

```
.
├── app.py                   # Main entry point for PDF processing
├── Dockerfile               # Docker configuration to containerize the app
├── requirements.txt         # Python dependencies
├── utils/
│   └── pdf_processor.py     # PDF text parser and outline extractor
├── input/                   # Folder to place input PDF files (mount to container)
└── output/                  # Output folder for JSON results (mount to container)
```

---

## 📋 Features

- Extracts document **title** from the first non-empty text on the first page.
- Detects headings based on patterns:
  - **H1**: CHAPTER 1, SECTION 2, ALL CAPS HEADINGS
  - **H2**: Numbered like `1.1 Introduction`, or `Heading:`
  - **H3**: Numbered like `1.1.1 Details`, or lowercase sections ending in colon
- Outputs JSON with:
  ```json
  {
    "title": "Document Title",
    "outline": [
      {
        "level": "H1",
        "text": "CHAPTER 1",
        "page": 1
      },
      ...
    ]
  }
  ```

---

## 🐳 Docker Setup

### Step 1: Build the Docker Image

```bash
docker build --platform linux/amd64 -t outline_extractor:1 .

```

### Step 2: Run the Container

#### ✅ Windows (Command Prompt):
```bash
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output --network none outline_extractor:1
```

#### ✅ macOS/Linux (Bash):
```bash
docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" --network none outline_extractor:1
```

> 📝 Make sure `input/` folder contains at least one `.pdf` file before running.

---

## ⚠️ Common Issues

- `invalid reference format`:  
  Occurs if you run the `docker run` command from **PowerShell** or use incorrect syntax.  
  ✅ Use **Command Prompt** (`cmd.exe`) or fix quotation/escape issues in PowerShell.

- `utils/pdf_processor.py` not found:  
  Ensure `pdf_processor.py` is inside a folder named `utils`, and both are copied in the Docker build context.

---

## ✅ Output

- For every `input/filename.pdf`, a file named `filename.json` will be created in the `output/` folder.
- Each JSON contains the extracted title and a structured outline of the PDF.

---

## 📦 Dependencies

From `requirements.txt`:

```
pdfminer.six==20221105
```

> You may add additional libraries if extending functionality (e.g., sentence transformers for Round 2).

---

## 📌 Next Steps

- [ ] Extend this for **Round 2** with semantic extraction
- [ ] Add error handling/logging
- [ ] Add tests for unit validation
- [ ] Optimize regex for multilingual formats (if required)

---

## 👤 Author

R.V. Abhinav  
Adobe India Hackathon 2025 – Participant
