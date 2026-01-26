from crewai import Task

def create_tasks(blue_agent, red_agent, editor_agent, topic):
    task_blue_initial = Task(
        description=f"""
        Search for the latest news on the topic: '{topic}'.
        Find 3 articles from progressive/left-leaning sources.
        Write a summary emphasizing social/environmental impact and equity.
        CRITICAL: At the end, list the URLs of the 3 articles you used.
        """,
        expected_output='A 200-word progressive analysis + list of 3 URLs.',
        agent=blue_agent,
        async_execution=True
    )

    task_red_initial = Task(
        description=f"""
        Search for the latest news on the topic: '{topic}'.
        Find 3 articles from conservative/right-leaning sources.
        Write a summary emphasizing economic freedom, tradition, and security.
        CRITICAL: At the end, list the URLs of the 3 articles you used.
        """,
        expected_output='A 200-word conservative analysis + list of 3 URLs.',
        agent=red_agent,
        async_execution=True
    )

    
    task_blue_rebuttal = Task(
        description=f"""
        Read the analysis provided by the Conservative Analyst (in the context).
        Identify the weak points, logical fallacies, or missing context in their argument.
        Write a sharp 2-sentence rebuttal from a Progressive perspective.
        Start your response with "Rebuttal:".
        """,
        expected_output='A 2-sentence critique of the conservative viewpoint.',
        agent=blue_agent,
        context=[task_red_initial] 
    )

    task_red_rebuttal = Task(
        description=f"""
        Read the analysis provided by the Progressive Analyst (in the context).
        Identify the weak points, economic ignorance, or idealism in their argument.
        Write a sharp 2-sentence rebuttal from a Conservative perspective.
        Start your response with "Rebuttal:".
        """,
        expected_output='A 2-sentence critique of the progressive viewpoint.',
        agent=red_agent,
        context=[task_blue_initial] 
    )

    task_editor = Task(
        description=f"""
        Review the analyses and rebuttals from both pundits.
        Create a final Markdown report.
        
        Structure:
        ## Section 1: The Facts (Neutral)
        ## Section 2: The Left View
        (Summarize Blue's initial analysis)
        > **Blue's Rebuttal to Right:** (Insert Blue's rebuttal here)
        
        ## Section 3: The Right View
        (Summarize Red's initial analysis)
        > **Red's Rebuttal to Left:** (Insert Red's rebuttal here)
        
        ## Section 4: The Divergence
        (Why they disagree)
        
        ## Section 5: Sources
        (Compile the URLs from both analysts)
        """,
        expected_output='A formatted Markdown report including Rebuttals and Sources.',
        agent=editor_agent,
        context=[task_blue_initial, task_red_initial, task_blue_rebuttal, task_red_rebuttal]
    )

    return [task_blue_initial, task_red_initial, task_blue_rebuttal, task_red_rebuttal, task_editor]