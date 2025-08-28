from langgraph.graph import StateGraph
from langchain_naver import ChatClovaX
from pydantic import BaseModel

from env import env

# 상태 정의
class State(BaseModel):
    question: str
    answer: str = ""
    cut_answer: str = ""

# LLM 모델 정의 및 초기화
model = ChatClovaX(
    model="HCX-005",
    api_key=env.CLOVASTUDIO_API_KEY,
)

# 질문 노드 정의
def ask_node(state: State) -> State:
    response = model.invoke(
        [
            ("human", state.question)
        ]
    )
    state.answer = response.content

    return state

# 답변 자르기 노드
def answer_slice(state: State) -> State:
    if len(state.answer) > 50:
        state.cut_answer = state.answer[:50]
    
    return state

# 그래프 구성
workflow = StateGraph(State)            # 그래프 초기화

# 그래프에 노드 추가
workflow.add_node("ask", ask_node)
workflow.add_node("slice", answer_slice)

# 그래프 연결
workflow.set_entry_point("ask")
workflow.add_edge("ask", "slice")
workflow.set_finish_point("slice")

# 그래프 컴파일
graph = workflow.compile()

if __name__ == "__main__":
    # 생성한 그래프로 질의(질문 -> 자르기 -> 출력) 의 순서를 가짐
    result = graph.invoke(
        {"question": "LangGraph가 무엇인지 설명해주세요."}
    )
    
    # 결과를 State 객체로 변환
    result_model = State.model_validate(result)
    
    # 질문을 출력
    print("[question]\n", result_model.question)
    
    # 자르지 않은 답변을 출력
    print("\n[answer]\n", result_model.answer)
    
    # 자른 답변을 출력
    print("\n[cut_answer]\n", result_model.cut_answer)
