"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""

        yaml_content = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = yaml_content["bug_to_user_story_v2"]["system_prompt"]

        assert system_prompt is not None, (
            "O campo 'system_prompt' não foi encontrado no arquivo YAML."
        )

        assert isinstance(system_prompt, str), (
            "O campo 'system_prompt' deve ser uma string."
        )

        assert system_prompt.strip(), (
            "O campo 'system_prompt' está vazio."
        )

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""

        yaml_content = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = yaml_content["bug_to_user_story_v2"]["system_prompt"]

        # Padrões comuns para definição de papel/persona
        role_indicators = [
            "você é",
            "voce é",
            "you are",
            "atue como",
            "aja como",
            "assuma o papel de",
            "você atua como",
            "voce atua como",
        ]

        system_prompt_lower = system_prompt.lower()

        assert any(
            indicator in system_prompt_lower
            for indicator in role_indicators
        ), (
            "O system_prompt deve definir explicitamente uma persona ou papel "
            "(ex.: 'Você é um Product Manager')."
        )

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""

        yaml_content = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = yaml_content["bug_to_user_story_v2"]["system_prompt"]

        format_indicators = [
            # Referências explícitas a formato
            "formato de saída",
            "formato de saida",
            "output format",
            "retorne no formato",
            "retorne exatamente no formato",
            "siga o formato",
            "estrutura obrigatória",
            "formato obrigatório",
            "formato markdown",
            "markdown",

            # User Story
            "user story",
            "como um",
            "eu quero",
            "para que",

            # Critérios de aceitação
            "critérios de aceitação",
            "criterios de aceitacao",
            "dado que",
            "quando",
            "então",
            "entao",
        ]

        assert any(
            indicator in system_prompt
            for indicator in format_indicators
        ), (
            "O system_prompt deve especificar claramente o formato esperado "
            "da resposta (ex.: Markdown, User Story ou estrutura de saída)."
        )

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""

        yaml_content = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = yaml_content["bug_to_user_story_v2"]["system_prompt"]

        # Indicadores típicos de exemplos few-shot
        few_shot_indicators = [
            "exemplo",
            "exemplos",
            "example",
            "examples",
            "entrada:",
            "saída:",
            "saida:",
            "input:",
            "output:",
            "resposta esperada:",
            "prompt original:",
            "resultado esperado:",
            "few-shot",
        ]

        # Também aceita a técnica declarada no metadata
        metadata = yaml_content.get("metadata", {})
        techniques = [t.lower() for t in metadata.get("techniques", [])]

        has_example_in_prompt = any(
            indicator in system_prompt
            for indicator in few_shot_indicators
        )

        has_few_shot_in_metadata = (
            "few_shot" in techniques
            or "few-shot" in techniques
        )

        assert (
            has_example_in_prompt or has_few_shot_in_metadata
        ), (
            "O prompt deve conter pelo menos um exemplo de entrada/saída "
            "(Few-shot) ou declarar 'few_shot' em metadata.techniques."
        )

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""

        yaml_content = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = yaml_content["bug_to_user_story_v2"]["system_prompt"]
        user_prompt = yaml_content["bug_to_user_story_v2"]["user_prompt"]

        full_text = f"{system_prompt}\n{user_prompt}"

        assert "[TODO]" not in full_text, "O prompt contém marcador [TODO]."
        assert "TODO" not in full_text, "O prompt contém marcador TODO."

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""

        yaml_content = load_prompts("prompts/bug_to_user_story_v2.yml")
        metadata = yaml_content["bug_to_user_story_v2"]["metadata"]

        # Recupera a lista de técnicas
        techniques = metadata.get("techniques", [])

        # Garante que o campo seja uma lista
        assert isinstance(
            techniques, list
        ), "O campo metadata.techniques deve ser uma lista."

        # Verifica quantidade mínima
        assert len(techniques) >= 2, (
            f"O prompt deve informar pelo menos 2 técnicas de engenharia de prompt. "
            f"Encontradas: {len(techniques)} ({techniques})"
        )

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])