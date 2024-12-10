import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew


import os

openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'


url = str(input("enter url : "))
inquiry = str(input("enter inquiry : "))

support_agent = Agent(
    role="Senior Support Representative",
	goal="Be the most friendly and helpful "
        "support representative in your team",
	backstory=(
		"You work at crewAI (https://crewai.com) and "
        " are now working on providing "
		"support to {customer}, a super important customer "
        " for your company."
		"You need to make sure that you provide the best support!"
		"Make sure to provide full complete answers, "
        " and make no assumptions."
	),
	allow_delegation=False,
	verbose=False
)


support_quality_assurance_agent = Agent(
	role="Support Quality Assurance Specialist",
	goal="Get recognition for providing the "
    "best support quality assurance in your team",
	backstory=(
		"You work at crewAI (https://crewai.com) and "
        "are now working with your team "
		"on a request from {customer} ensuring that "
        "the support representative is "
		"providing the best support possible.\n"
		"You need to make sure that the support representative "
        "is providing full"
		"complete answers, and make no assumptions."
	),
	verbose=False
)

final_review_agent = Agent(
    role="Final Review Specialist",
    goal="Ensure the final response is clear, concise, and free from repetition or confusion.",
    backstory=(
        "You are an expert in content editing and quality control. "
        "Your role is to review the final customer support response and ensure "
        "it is polished, concise, and completely free of redundancies or mixed-up information."
    ),
    allow_delegation=False,
    verbose=False
)




from crewai_tools import ScrapeWebsiteTool


docs_scrape_tool = ScrapeWebsiteTool(
    website_url= url
)

inquiry_resolution = Task(
    description=(
        "{customer} just reached out with a super important ask:\n"
	    "{inquiry}\n\n"
        "{person} from {customer} is the one that reached out. "
		"Make sure to use everything you know "
        "to provide the best support possible."
		"You must strive to provide a complete "
        "and accurate response to the customer's inquiry."
    ),
    expected_output=(
	    "A detailed, informative response to the "
        "customer's inquiry that addresses "
        "all aspects of their question.\n"
        "The response should include references "
        "to everything you used to find the answer, "
        "including external data or solutions. "
        "Ensure the answer is complete, "
		"leaving no questions unanswered, and maintain a helpful and friendly "
		"tone throughout."
    ),
	tools=[docs_scrape_tool],

    agent=support_agent,
)

quality_assurance_review = Task(
    description=(
        "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
        "Ensure that the answer is comprehensive, accurate, and adheres to the "
		"high-quality standards expected for customer support.\n"
        "Verify that all parts of the customer's inquiry "
        "have been addressed "
		"thoroughly, with a helpful and friendly tone.\n"
        "Check for references and sources used to "
        " find the information, "
		"ensuring the response is well-supported and "
        "leaves no questions unanswered."
    ),
    expected_output=(
        "A final, detailed, and informative response "
        "ready to be sent to the customer.\n"
        "This response should fully address the "
        "customer's inquiry, incorporating all "
		"relevant feedback and improvements.\n"
		"Don't be too formal, we are a chill and cool company "
	    "but maintain a professional and friendly tone throughout."
    ),
    agent=support_quality_assurance_agent,
)

final_review_task = Task(
    description=(
        "Review the response produced by the Support and QA agents. "
        "Your goal is to eliminate any repetition, confusion, or verbosity, "
        "ensuring the response is concise, clear, and professional. "
        "Maintain a friendly and helpful tone throughout."
    ),
    expected_output=(
        "A refined and polished response that is free from repetition, confusion, "
        "and unnecessary verbosity, ready to be sent to the customer."
    ),
    agent=final_review_agent
)

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent , final_review_agent],
  tasks=[inquiry_resolution, quality_assurance_review , final_review_task],
  verbose=False,
  memory=False
)


inputs = {
    "customer": "DeepLearningAI",
    "person": "Adi",
    "inquiry": inquiry               
}


result = crew.kickoff(inputs=inputs)

print(result) 
