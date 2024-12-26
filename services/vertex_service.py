import logging

import vertexai
from google.oauth2 import service_account
from vertexai.generative_models import GenerationConfig, GenerativeModel, Tool, grounding


class VertexAIService:
    def __init__(self, config):
        self.config = config.vertex_ai
        self.logger = logging.getLogger(__name__)
        self.model = None
        self.tool = None
        self.initialize_service()

    def initialize_service(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.config.credentials_file
            )
            project_id = credentials.project_id
            vertexai.init(
                project=project_id, location=self.config.project_location, credentials=credentials
            )
            self.model = GenerativeModel(self.config.model_name)
            self.tool = Tool.from_google_search_retrieval(grounding.GoogleSearchRetrieval())
            self.logger.info("Successfully initialized service account and model")
        except Exception as e:
            self.logger.error(f"Failed to initialize service account: {str(e)}")
            raise

    def generate_content(self, prompt):
        return self.model.generate_content(
            prompt,
            tools=[self.tool],
            generation_config=GenerationConfig(temperature=0.0),
        )
