from analyzer import EgoAnalyzer
from roaster import EgoRoaster

def main():
    print("🚀 Starting Ego-Driven Code Refactorer...")
    
    # Sample complex/over-engineered code for testing
    sample_code = """
    class OverEngineeredGreeter:
        def __init__(self, name):
            self.name = name
        async def generate_greeting(self):
            return lambda: f"Hello, {self.name}!"
    """
    
    # 1. Analyze the code
    analyzer = EgoAnalyzer(sample_code)
    analysis_result = analyzer.analyze()
    
    print(f"📊 Analysis Complete. Ego Score calculated: {analysis_result['ego_score']}%")
    
    # 2. Trigger the interactive AI companion dialogue
    roaster = EgoRoaster(analysis_result)
    roaster.interactive_dialogue()

if __name__ == "__main__":
    main()