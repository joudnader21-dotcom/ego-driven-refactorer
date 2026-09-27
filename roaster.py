import time

class EgoRoaster:
    """
    An interactive AI companion featuring a chat bubble and avatar simulation
    to guide the user with sarcastic, engaging English feedback.
    """
    
    def __init__(self, analysis_result: dict):
        self.score = analysis_result.get("ego_score", 0)
        self.issues = analysis_result.get("issues", [])
        
    def interactive_dialogue(self):
        print("\n" + "="*55)
        print(" 💬 [Ego-Driven Assistant Chat Room]")
        print("="*55)
        
        print(" 👤 [User Code Submitted]")
        time.sleep(0.5)
        
        # Avatar representation in a simulated circular layout
        print("\n       ╭──────────────────────────╮")
        print("       │      ( 🟢 [ Bob ] )      │  <-- Active Companion")
        print("       ╰──────────────────────────╯")
        time.sleep(0.8)
        
        print("\n 🤖 [Bob is chatting with you...]:")
        
        if self.score > 70:
            print(" ┌────────────────────────────────────────────────────────┐")
            print(" │ 'Hey artist! You wrote code like you're building a      │")
            print(" │  spacecraft for NASA! Let's simplify it before it      │")
            print(" │  crashes.'                                             │")
            print(" └────────────────────────────────────────────────────────┘")
        elif self.score > 40:
            print(" ┌────────────────────────────────────────────────────────┐")
            print(" │ 'Hey there! I am here if you need to tone down the     │")
            print(" │  over-engineering a bit.'                              │")
            print(" └────────────────────────────────────────────────────────┘")
        else:
            print(" ┌────────────────────────────────────────────────────────┐")
            print(" │ 'Clean and humble code! I am here anytime you need.'   │")
            print(" └────────────────────────────────────────────────────────┘")
        print("="*55 + "\n")