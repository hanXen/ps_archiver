# ps_archiver

`ps_archiver` (Problem Solving Archiver)는 **Programmers**와 **LeetCode** 같은 플랫폼에서 코딩 문제 설명을 파싱하고 이를 마크다운 파일로 아카이빙하는 Python 도구입니다.

---

## 📌 주요 기능

- **지원 플랫폼**:
  - [Programmers](https://programmers.co.kr)와 [LeetCode](https://leetcode.com) 문제 파싱 지원
  - 플랫폼별 디렉토리에 문제를 자동으로 분류 및 저장

- **마크다운 생성**:
  - URL을 입력받아 문제 description을 파싱하여 마크다운 파일로 저장
  - 깔끔하고 일관된 형식으로 생성되어 체계적인 학습 및 정리 가능

- **아카이빙**:
  - 문제 분류 및 저장 방법:
    - Programmers 문제는 난이도별로 분류
    - LeetCode 문제는 `dynamic-programming` 같은 태그별로 분류

---

## 🤔 누가 사용하면 좋을까요?

- **Problem-Solver 및 학습자**: 문제 풀이를 체계적으로 기록하고 코딩 실력을 향상시키고 싶은 분들
- **코딩 테스트 준비생**: 코딩 면접이나 알고리즘 대회를 준비하며 연습 문제를 난이도나 카테고리별로 정리하고 싶은 분들
- **보안에 민감한 사용자**: GitHub 계정 정보 같은 민감한 정보를 브라우저 확장 프로그램에 저장하고 싶지 않은 분들

---

## 설치 방법

🎯 [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv sync
```

pip

```bash
pip install -r requirements.txt
```

---

## 사용법

명령어:

```bash
uv run main.py -u <problem_url>
```

### 실행 예제

```bash
# leetcode.com
uv run main.py -u "https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=dynamic-programming"

# programmers.co.kr
uv run main.py -u "https://school.programmers.co.kr/learn/courses/30/lessons/176962"
```

‼️ **LeetCode 문제 분류 및 아카이빙**

> LeetCode 문제는 URL의 쿼리 문자열에 포함된 `envId` 값을 기반으로 문제를 분류합니다 (예: `envId=dynamic-programming`). 쿼리 문자열이 없거나 `envId`가 포함되지 않은 경우, 문제는 `leetcode.com` 디렉토리에 바로 저장됩니다.

---

## 아카이브 디렉토리 구조

위 예제 실행 결과, 파싱된 문제는 다음과 같이 저장됩니다:

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

## 📝 마크다운 출력

생성된 마크다운 파일의 기본 구조는 다음과 같습니다:

```markdown
# [Problem Title]

## 문제
[Problem URL]

[Problem description converted to Markdown]

---

## Key Points

(Add your notes here)
```

#### ✅ **마크다운 커스터마이징**

`utils.markdown_utils.py` 모듈의 `generate_markdown()` 함수에서 마크다운 출력 형식을 사용자 정의할 수 있습니다. 구조, 헤딩, 추가 섹션 등을 필요에 따라 수정할 수 있습니다.

---

## 🎯 제안하는 학습 방법

1. **Programmers로 시작하기**:
    
    - [Programmers](https://programmers.co.kr/)에서 난이도별 문제를 풀며 알고리즘 및 자료 구조의 기초를 다지세요.
        
2. **LeetCode로 심화 학습하기**:
    
    - Programmers에서 푼 문제 중 더 연습이 필요한 카테고리를 파악하세요.
        
    - [LeetCode](https://leetcode.com/)의 방대한 문제집을 활용하여 해당 카테고리의 문제를 추가로 연습하세요.
        

이 방법은 체계적인 학습을 가능하게 하며 약점을 보완하는 데 도움을 줍니다.

---

## 라이선스

[MIT License](./LICENSE)
