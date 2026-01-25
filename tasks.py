from crewai import Task

def create_tasks(blue_agent, red_agent, editor_agent, topic):
    task_blue = Task(
        description=f"""
        Search for the latest news on the topic: '{topic}'.
        Find 3 articles from progressive/left-leaning sources.
        Write a summary emphasizing social/environmental impact.
        CRITICAL: At the end, list the URLs of the 3 articles you used.
        """,
        expected_output='A 200-word analysis + list of 3 URLs.',
        agent=blue_agent
    )

    task_red = Task(
        description=f"""
        Search for the latest news on the topic: '{topic}'.
        Find 3 articles from conservative/right-leaning sources.
        Write a summary emphasizing economic/liberty impact.
        CRITICAL: At the end, list the URLs of the 3 articles you used.
        """,
        expected_output='A 200-word analysis + list of 3 URLs.',
        agent=red_agent
    )

    task_editor = Task(
        description=f"""
        Review the analyses from both pundits.
        Create a final Markdown report.
        Section 1: The Facts (Neutral)
        Section 2: The Left View (Summarize Blue's points)
        Section 3: The Right View (Summarize Red's points)
        Section 4: The Divergence (Why they disagree)
        Section 5: Sources (Compile the URLs from both analysts)
        """,
        expected_output='A formatted Markdown report with a Sources section.',
        agent=editor_agent,
        context=[task_blue, task_red]
    )

    return [task_blue, task_red, task_editor]