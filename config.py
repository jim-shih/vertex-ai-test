from dataclasses import dataclass

import yaml


@dataclass
class VertexAIConfig:
    project_location: str
    model_name: str
    credentials_file: str


@dataclass
class ProcessingConfig:
    max_workers: int
    output_file: str
    dataset_path: str


@dataclass
class LoggingConfig:
    log_dir: str
    level: str


@dataclass
class PromptsConfig:
    transaction_template: str


@dataclass
class Config:
    vertex_ai: VertexAIConfig
    processing: ProcessingConfig
    logging: LoggingConfig
    prompts: PromptsConfig

    @classmethod
    def from_yaml(cls, yaml_path: str = "config.yaml") -> "Config":
        with open(yaml_path, "r") as f:
            config_dict = yaml.safe_load(f)

        return cls(
            vertex_ai=VertexAIConfig(**config_dict["vertex_ai"]),
            processing=ProcessingConfig(**config_dict["processing"]),
            logging=LoggingConfig(**config_dict["logging"]),
            prompts=PromptsConfig(**config_dict["prompts"]),
        )
