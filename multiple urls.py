import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew


import os

openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'


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


docs_scrape_tool_1 = ScrapeWebsiteTool(url="https://docs.crewai.com/introduction")
docs_scrape_tool_2 = ScrapeWebsiteTool(url="https://docs.crewai.com/installation")
docs_scrape_tool_3 = ScrapeWebsiteTool(url="https://docs.crewai.com/quickstart")
docs_scrape_tool_4 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/agents")
docs_scrape_tool_5 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/tasks")
docs_scrape_tool_6 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/crews")
docs_scrape_tool_7 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/flows")
docs_scrape_tool_8 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/knowledge")
docs_scrape_tool_9 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/llms")
docs_scrape_tool_10 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/processes")
docs_scrape_tool_11 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/collaboration")
docs_scrape_tool_12 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/training")
docs_scrape_tool_13 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/memory")
docs_scrape_tool_14 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/planning")
docs_scrape_tool_15 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/testing")
docs_scrape_tool_16 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/cli")
docs_scrape_tool_17 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/tools")
docs_scrape_tool_18 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/langchain-tools")
docs_scrape_tool_19 = ScrapeWebsiteTool(url="https://docs.crewai.com/concepts/llamaindex-tools")
docs_scrape_tool_20 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/create-custom-tools")
docs_scrape_tool_21 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/sequential-process")
docs_scrape_tool_22 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/hierarchical-process")
docs_scrape_tool_23 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/custom-manager-agent")
docs_scrape_tool_24 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/llm-connections")
docs_scrape_tool_25 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/customizing-agents")
docs_scrape_tool_26 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/coding-agents")
docs_scrape_tool_27 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/force-tool-output-as-result")
docs_scrape_tool_28 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/human-input-on-execution")
docs_scrape_tool_29 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/kickoff-async")
docs_scrape_tool_30 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/kickoff-for-each")
docs_scrape_tool_31 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/replay-tasks-from-latest-crew-kickoff")
docs_scrape_tool_32 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/conditional-tasks")
docs_scrape_tool_33 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/agentops-observability")
docs_scrape_tool_34 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/langtrace-observability")
docs_scrape_tool_35 = ScrapeWebsiteTool(url="https://docs.crewai.com/how-to/openlit-observability")
docs_scrape_tool_36 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/browserbaseloadtool")
docs_scrape_tool_37 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/codedocssearchtool")
docs_scrape_tool_38 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/codeinterpretertool")
docs_scrape_tool_39 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/composiotool")
docs_scrape_tool_40 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/csvsearchtool")
docs_scrape_tool_41 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/dalletool")
docs_scrape_tool_42 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/directorysearchtool")
docs_scrape_tool_43 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/directoryreadtool")
docs_scrape_tool_44 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/docxsearchtool")
docs_scrape_tool_45 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/exasearchtool")
docs_scrape_tool_46 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/filereadtool")
docs_scrape_tool_47 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/filewritetool")
docs_scrape_tool_48 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/firecrawlcrawlwebsitetool")
docs_scrape_tool_49 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/firecrawlscrapewebsitetool")
docs_scrape_tool_50 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/firecrawlsearchtool")
docs_scrape_tool_51 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/githubsearchtool")
docs_scrape_tool_52 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/serperdevtool")
docs_scrape_tool_53 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/jsonsearchtool")
docs_scrape_tool_54 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/mdxsearchtool")
docs_scrape_tool_55 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/mysqltool")
docs_scrape_tool_56 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/nl2sqltool")
docs_scrape_tool_57 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/pdfsearchtool")
docs_scrape_tool_58 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/pgsearchtool")
docs_scrape_tool_59 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/scrapewebsitetool")
docs_scrape_tool_60 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/seleniumscrapingtool")
docs_scrape_tool_61 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/spidertool")
docs_scrape_tool_62 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/txtsearchtool")
docs_scrape_tool_63 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/visiontool")
docs_scrape_tool_64 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/websitesearchtool")
docs_scrape_tool_65 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/xmlsearchtool")
docs_scrape_tool_66 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/youtubechannelsearchtool")
docs_scrape_tool_67 = ScrapeWebsiteTool(url="https://docs.crewai.com/tools/youtubevideosearchtool")
docs_scrape_tool_68 = ScrapeWebsiteTool(url="https://docs.crewai.com/telemetry")


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
	tools = [
    docs_scrape_tool_1, docs_scrape_tool_2, docs_scrape_tool_3, docs_scrape_tool_4, 
    docs_scrape_tool_5, docs_scrape_tool_6, docs_scrape_tool_7, docs_scrape_tool_8, 
    docs_scrape_tool_9, docs_scrape_tool_10, docs_scrape_tool_11, docs_scrape_tool_12, 
    docs_scrape_tool_13, docs_scrape_tool_14, docs_scrape_tool_15, docs_scrape_tool_16, 
    docs_scrape_tool_17, docs_scrape_tool_18, docs_scrape_tool_19, docs_scrape_tool_20, 
    docs_scrape_tool_21, docs_scrape_tool_22, docs_scrape_tool_23, docs_scrape_tool_24, 
    docs_scrape_tool_25, docs_scrape_tool_26, docs_scrape_tool_27, docs_scrape_tool_28, 
    docs_scrape_tool_29, docs_scrape_tool_30, docs_scrape_tool_31, docs_scrape_tool_32, 
    docs_scrape_tool_33, docs_scrape_tool_34, docs_scrape_tool_35, docs_scrape_tool_36, 
    docs_scrape_tool_37, docs_scrape_tool_38, docs_scrape_tool_39, docs_scrape_tool_40, 
    docs_scrape_tool_41, docs_scrape_tool_42, docs_scrape_tool_43, docs_scrape_tool_44, 
    docs_scrape_tool_45, docs_scrape_tool_46, docs_scrape_tool_47, docs_scrape_tool_48, 
    docs_scrape_tool_49, docs_scrape_tool_50, docs_scrape_tool_51, docs_scrape_tool_52, 
    docs_scrape_tool_53, docs_scrape_tool_54, docs_scrape_tool_55, docs_scrape_tool_56, 
    docs_scrape_tool_57, docs_scrape_tool_58, docs_scrape_tool_59, docs_scrape_tool_60, 
    docs_scrape_tool_61, docs_scrape_tool_62, docs_scrape_tool_63, docs_scrape_tool_64, 
    docs_scrape_tool_65, docs_scrape_tool_66, docs_scrape_tool_67, docs_scrape_tool_68
]

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
    "inquiry": "explain to me the key concepts involved in the usage of knowledge in crewai"

                
}
result = crew.kickoff(inputs=inputs)

print(result) 
