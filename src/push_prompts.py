"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header, validate_prompt_structure
from langsmith import Client
from langsmith import utils as ls_utils

load_dotenv()

#Nome do prompt a ser carregado no LangSmith
prompt_name = "bug_to_user_story_v2"

def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", prompt_data[prompt_name]["system_prompt"]),
        ("human", prompt_data[prompt_name]["user_prompt"])
    ])

    client = Client()
    url = client.push_prompt(
        "stefanritter/"+prompt_name,
        object=prompt_template
    )
    return True


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """

    errors: list[str] = []

    if not isinstance(prompt_data, dict):
        return False, ["O YAML deve ser um dicionário."]

    if len(prompt_data) != 1:
        errors.append("O YAML deve conter exatamente um prompt na raiz.")
        return False, errors

    prompt_name, prompt = next(iter(prompt_data.items()))

    if not isinstance(prompt_name, str) or not prompt_name.strip():
        errors.append("A chave raiz do prompt deve ser uma string não vazia.")

    if not isinstance(prompt, dict):
        errors.append(f"O conteúdo de '{prompt_name}' deve ser um dicionário.")
        return False, errors

    required_fields = ["description", "system_prompt", "user_prompt"]

    for field in required_fields:
        if field not in prompt:
            errors.append(f"Campo obrigatório ausente: '{field}'.")
            continue

        if not isinstance(prompt[field], str):
            errors.append(f"O campo '{field}' deve ser uma string.")
            continue

        if field in ["system_prompt", "user_prompt"] and not prompt[field].strip():
            errors.append(f"O campo '{field}' não pode estar vazio.")

    if "tags" in prompt and not isinstance(prompt["tags"], list):
        errors.append("O campo 'tags' deve ser uma lista.")

    if "version" in prompt and prompt["version"] is not None:
        if not isinstance(prompt["version"], (int, str)):
            errors.append("O campo 'version' deve ser inteiro, string ou null.")

    if "created_at" in prompt and prompt["created_at"] is not None:
        if not isinstance(prompt["created_at"], str):
            errors.append("O campo 'created_at' deve ser string ou null.")

    return len(errors) == 0, errors

def main():
    print_section_header("push prompt session starts")
    env_vars = ["LANGSMITH_TRACING","LANGSMITH_ENDPOINT","LANGSMITH_API_KEY","LANGSMITH_PROJECT","USERNAME_LANGSMITH_HUB","OPENAI_API_KEY","GOOGLE_API_KEY","LLM_PROVIDER","LLM_MODEL","EVAL_MODEL"]
    check_env_vars(env_vars)
    yaml_content = load_yaml("prompts/"+prompt_name+".yml")

    is_valid, errors = validate_prompt(yaml_content)
    if (is_valid):
        try:
            if (push_prompt_to_langsmith(prompt_name, yaml_content)):
                print("Prompt publicado com sucesso.")

        except ls_utils.LangSmithConflictError as e:
            # Caso específico: o prompt não sofreu alterações
            if "Nothing to commit" in str(e):
                print("Nenhuma alteração detectada no prompt. Commit não realizado.")
            else:
                # Repropaga outros conflitos inesperados
                raise

        except Exception as e:
            print(f"Erro inesperado ao publicar o prompt: {e}")
            raise
    else:
        print(errors)


if __name__ == "__main__":
    sys.exit(main())
