from crewai import Task

def create_tasks(blue_agent, red_agent, editor_agent, topic):
    task_blue = Task(
        description=f"""
        Search for the latest news on the topic: '{topic}'.
        Find 3 articles from progressive or left-leaning sources.
        Write a summary that emphasizes the social and environmental implications.
        """,
        expected_output='A 200-word analysis focusing on social equity and regulation.',
        agent=blue_agent
    )

    task_red = Task(
        description=f"""
        Search for the latest news on the topic: '{topic}'.
        Find 3 articles from conservative or right-leaning sources.
        Write a summary that emphasizes the economic and liberty implications.
        """,
        expected_output='A 200-word analysis focusing on economic impact and freedom.',
        agent=red_agent
    )

    task_editor = Task(
        description=f"""
        Review the analysis provided by the Progressive Analyst and the Conservative Analyst on '{topic}'.
        Create a final report with three sections:
        1. The Facts: Data points both sides agree on.
        2. The Left View: A summary of the Progressive arguments.
        3. The Right View: A summary of the Conservative arguments.
        4. The Divergence: Specifically explain WHY they disagree.
        """,
        expected_output='A formatted Markdown report comparing the two perspectives.',
        agent=editor_agent,
        context=[task_blue, task_red]
    )

    return [task_blue, task_red, task_editor]