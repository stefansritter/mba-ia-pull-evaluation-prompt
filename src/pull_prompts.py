"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import sys
from dotenv import load_dotenv
from langsmith import Client
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():

    prompt_name = "bug_to_user_story_v1"
    client = Client()
    prompt = client.pull_prompt("leonanluppi/"+prompt_name)
    system_prompt = ""
    user_prompt = ""

    if hasattr(prompt, "messages"):
        for msg in prompt.messages:
            role = msg.__class__.__name__

            if hasattr(msg, "prompt"):
                template = msg.prompt.template
            else:
                template = msg.content

            if "System" in role:
                system_prompt = template
            elif "Human" in role:
                user_prompt = template

    metadata = getattr(prompt, "metadata", {}) or {}

    version = metadata.get("version")
    created_at = metadata.get("created_at")
    tags = metadata.get("tags", [])
    description = metadata.get("description", "")

    # fallback (caso metadata não venha)
    if not description:
        description = getattr(prompt, "description", "")

    yaml_content = {
        prompt_name: {
            "description": description,
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "version": version,
            "created_at": str(created_at) if created_at else None,
            "tags": tags
        }
    }

    if (save_yaml(yaml_content, "prompts/"+prompt_name+".yml")):
        print("Arquivo YAML salvo com sucesso!")


def main():
    print_section_header("push prompt session starts")
    env_vars = ["LANGSMITH_TRACING","LANGSMITH_ENDPOINT","LANGSMITH_API_KEY","LANGSMITH_PROJECT","USERNAME_LANGSMITH_HUB","OPENAI_API_KEY","GOOGLE_API_KEY","LLM_PROVIDER","LLM_MODEL","EVAL_MODEL"]
    check_env_vars(env_vars)
    pull_prompts_from_langsmith()


if __name__ == "__main__":
    sys.exit(main())
