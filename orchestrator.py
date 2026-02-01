from crewai import Crew, Process
from agents.jd_analyst import get_jd_analyst_agent, create_jd_analysis_task
from usajobs_api import fetch_usajobs

def run_pipeline():
    job_posts = fetch_usajobs("business analyst", location = "New York")
    if not job_posts:
        print("No job posts found.")
        return
    
    job_data = job_posts[0]['MatchedObjectDescriptor']
    job_summary = job_data['UserArea']['Details']['JobSummary']

    jd_agent = get_jd_analyst_agent()
    jd_task = create_jd_analysis_task(jd_agent, job_summary)

    crew = Crew(
        agents = [jd_agent],
        tasks = [jd_task],
        process = Process.sequential
    )

    result = crew.kickoff()

    print("\n== FINAL OUTPUT ===\n")
    print(result)

if __name__ == "__main__":
    run_pipeline()