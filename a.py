from langchain_core.output_parsers import JsonOutputParser

string = """
```json
{
  "category": explain_potential_reason
}
```
"""

parser = JsonOutputParser()
output = parser.parse(string)
print(output)