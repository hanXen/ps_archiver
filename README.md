# ps_archiver

`ps_archiver` (short for "Problem Solving Archiver") is a Python tool that helps parse and archive coding problem descriptions from platforms like **Programmers** and **LeetCode** into Markdown files for easy reference.


## 📌 Features

- **Platform Support**:
  - Parse problems from [Programmers](https://programmers.co.kr) and [LeetCode](https://leetcode.com).
  - Automatically categorize and save problems in platform-specific directories.

- **Markdown Generation**:
  - Takes problem URLs as input and generates well-structured Markdown files.
  - Provides a clean and consistent format for easy reference and sharing.

- **Archiving**:
  - Saves problems in an organized directory structure:
    - Programmers problems are categorized by difficulty levels.
    - LeetCode problems are categorized by tags like `dynamic-programming`.


## 🤔 Who Needs This Tool?

This tool is ideal for:

- **Problem-Solvers and Learners**: Those who want to document and organize solved problems to improve their coding skills.  
- **Coding Test Takers**: Individuals preparing for coding interviews or competitive programming, who want to organize practice problems by category or difficulty.  
- **Security-Conscious Users**: Users who prefer not to store sensitive information like GitHub credentials in browser extensions. (as this might pose a potential security risk 🫢).


---

## Installation

🎯 [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv sync
```

pip

```bash
pip install -r requirements.txt
```

---

### Usage

Run the tool using the following command:
```bash
uv run main.py -u <problem_url>
```

### Example
```bash
# leetcode.com
uv run main.py -u "https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=dynamic-programming"

# programmers.co.kr
uv run main.py -u "https://school.programmers.co.kr/learn/courses/30/lessons/176962"
```

‼️ LeetCode Parsing and Archiving

> For LeetCode problems, the tool categorizes problems based on the `envId` value in the URL's query string (e.g., `envId=dynamic-programming`). If the query string is absent or does not include `envId`, the problem will be saved directly under the `leetcode.com` directory without further categorization.


### Output Directory Structure
For the above example, the parsed problem will be saved as:

```
archive/
└── leetcode.com/
│   └── dynamic-programming/
│       └── 338. Counting Bits/
│           └── README.md
│
└── programmers.co.kr/
    └── LV.2/
        └── 과제 진행하기/
            └── README.md            
````

---

### 📝 Markdown Output

The generated Markdown file follows this structure:

```markdown
# [Problem Title]

## 문제
[Problem URL]

[Problem description converted to Markdown]

---

## Key Points

(Add your notes here)
```

#### ✅ Customization

The `generate_markdown()` function in the `utils.markdown_utils.py` module allows customization of the Markdown output format. You can modify the structure, headings, or additional sections according to your preferences.


--- 

### 🎯 Suggested Study Workflow

1. **Start with Programmers**:
   - Focus on solving problems categorized by difficulty on [Programmers](https://programmers.co.kr).
   - Build a strong foundational understanding of algorithms and data structures.

2. **Deepen Your Expertise with LeetCode**:
   - Identify categories or topics you'd like to master further, based on problems you've solved on Programmers.
   - Practice those specific categories on [LeetCode](https://leetcode.com), utilizing their broader problem sets and varying difficulty levels.

This methodical approach helps reinforce learning while addressing targeted weaknesses.


---

### License

This project is licensed under the [MIT License](./LICENSE).
