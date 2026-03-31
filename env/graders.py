def grade_action(agent_action, correct_action):

    if agent_action == correct_action:
        return 1.0

    if agent_action in [1,4]:
        return 0.5

    return 0.0