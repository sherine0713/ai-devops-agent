from ai_analyzer import analyze_logs

sample_logs = """
ModuleNotFoundError: No module named 'flask'
"""

result = analyze_logs(sample_logs)

print(result)