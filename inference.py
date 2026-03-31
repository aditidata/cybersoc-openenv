import os
from openai import OpenAI
from env.environment import CyberSOCEnv

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

env = CyberSOCEnv()

total_score = 0
episodes = 10

for i in range(episodes):

    state = env.reset()

    prompt = f"""
    Security Alert:
    type:{state.alert_type}
    failed_logins:{state.failed_logins}
    malware:{state.malware_detected}
    traffic:{state.network_traffic}
    severity:{state.severity}

    Choose action number:
    0 ignore
    1 investigate_logs
    2 block_ip
    3 isolate_host
    4 escalate_incident
    """

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role":"user","content":prompt}]
    )

    action = int(response.choices[0].message.content.strip())

    state, reward, done, _ = env.step(action)

    total_score += reward.value

print("Baseline score:", total_score/episodes)