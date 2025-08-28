# LangGraph Demo

이 프로젝트는 Naver Clova Studio의 언어 모델과 `langgraph` 라이브러리를 사용하여 간단한 질문-답변 그래프를 시연하는 데모입니다. `langgraph`는 사용자가 LLM 모델의 워크플로우를 보다 쉽게 관리할 수 있게 해주는 라이브러리입니다.

## 프로젝트 설명

사용자의 질문을 입력받아 `ChatClovaX` 모델을 통해 답변을 생성합니다. 그 후, 생성된 답변의 일부(50자)를 잘라내어 원본 답변과 함께 출력합니다. 이는 `langgraph`를 통해 정의된 워크플로우(질문 노드 -> 답변 자르기 노드)에 따라 실행됩니다.

## 시작하기

### 사전 요구 사항

- Python 3.12
- `pipenv`

### 설치

### 1. **저장소 클론:**

```bash
git clone https://github.com/leeing1414/LangGraph-Demo
cd LangGraph-Demo
```

### 2. **의존성 설치:**

`Pipfile`에 명시된 패키지들을 설치합니다.

```bash
pipenv install
```

### 3. **환경 변수 설정:**

`.env.example` 파일을 복사하여 `.env` 파일을 생성하고, Naver Clova Studio에서 발급받은 API 키를 입력합니다.

```bash
cp .env.example .env
```

`.env` 파일 내용:

```bash
CLOVASTUDIO_API_KEY=여기에_발급받은_API_키를_입력하세요
```

## 사용법

아래 명령어를 실행하여 프로젝트를 시작합니다.

```bash
pipenv run python main.py
```

## 실행 예제 및 결과

### 명령어

```bash
pipenv run python main.py
```

### 결과

```bash
[question]
LangGraph가 무엇인지 설명해주세요.

[answer]
LangGraph는 인공지능 언어모델인 하이퍼클로바(HyperCLOVA)의 핵심 기술 중 하나입니다.

이는 **언어의 구조와 의미를 파악하여, 이를 그래프 형태로 표현한 것**을 의미합니다. LangGraph를 활용하면 다음과 같은 장점이 있습니다.

1. 언어 이해 능력 향상: 문장의 구조를 분석하고, 단어들 간의 관계를 파악할 수 있어 언어 모델의 언어 이해 능력을 향상시킵니다.
2. 자동 번역 성능 개선: 문장을 그래프로 변환하여 번역하기 때문에 기존의 단어 기반 번역 방식보다 정확도가 높습니다.
3. 문서 요약 및 생성: 문서 내의 핵심 내용을 추출하거나 새로운 문서를 자동으로 작성하는 등의 작업에 활용할 수 있습니다.

결론적으로, LangGraph는 인공지능 언어모델의 성능을 높이는 데 중요한 역할을 하는 기술이며, 다양한 분야에서 응용될 가능성이 높습니다.

[cut_answer]
LangGraph는 인공지능 언어모델인 하이퍼클로바(HyperCLOVA)의 핵심 기술 중
```
