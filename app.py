from fastapi import FastAPI
from env.environment import CyberSOCEnv

app = FastAPI()
env = CyberSOCEnv()
@app.get("/")
def home():
    return {"message": "CyberSOC OpenEnv running"}

@app.get("/reset")
def reset():
    state = env.reset()
    return state.dict()

@app.post("/step/{action}")
def step(action:int):
    state,reward,done,_ = env.step(action)
    return {
        "state": state.dict(),
        "reward": reward.value,
        "done": done
    }