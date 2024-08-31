from Introduction.hello import LLM_profile_summary
from ReachOut.agents.profile_search_agent import profile_url_search



if __name__=='__main__':
    
    name = 'Jayant Nehra'
    persons_detail = f"LinkedIn profile URL for: {name} who works at Fifty Five technologies pvt ltd."
    
    profile_url = profile_url_search(persons_detail)
    print(profile_url)

    # LLM_profile_summary()