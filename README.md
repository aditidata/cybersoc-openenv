CyberSOC OpenEnv

A real-world cybersecurity incident response environment.

Agents act as SOC analysts and respond to alerts like:

- brute force login attempts
- malware infection
- data exfiltration

API

reset()
step(action)
state()

Actions

0 ignore
1 investigate logs
2 block IP
3 isolate host
4 escalate incident

Tasks

Easy – brute force attack
Medium – malware response
Hard – data exfiltration attack

Setup

pip install -r requirements.txt
python inference.py