# Problem Statement
# Many applications require the ability to restore an object to a previous state, 
# such as providing an "undo" or "rollback" functionality. Embedding this capability 
# directly into an object can violate encapsulation, as it may expose internal details 
# that should remain hidden. The Memento Design Pattern solves this problem by capturing
#  and externalizing an object’s internal state into a memento, which can be stored and 
# later used to restore the object without exposing its internal structure. This allows 
# clients (or caretakers) to request state snapshots at various points in time and 
# later revert to those snapshots when needed.

# Example: Text Editor Undo Functionality
# Consider a simple text editor that allows users to edit text. To implement an undo 
# feature, the text editor (originator) can save its state (the current text content) 
# into a memento object. The caretaker manages these mementos (for example, by using a 
# stack) so that the editor can revert to an earlier state if the user decides to undo 
# an operation.

# Memento class: stores the state of the TextEditor.
class TextEditorMemento:
    def __init__(self, content: str):
        self._content = content

    def get_saved_content(self) -> str:
        return self._content

# Originator: The TextEditor that can create and restore its state using mementos.
class TextEditor:
    def __init__(self):
        self._content = ""

    def type(self, words: str):
        self._content += words
        print(f"TextEditor current content: '{self._content}'")

    def get_content(self) -> str:
        return self._content

    def save(self) -> TextEditorMemento:
        print("Saving current state.")
        return TextEditorMemento(self._content)

    def restore(self, memento: TextEditorMemento):
        self._content = memento.get_saved_content()
        print(f"Restored content: '{self._content}'")

# Caretaker: Maintains history of mementos to support undo functionality.
class Caretaker:
    def __init__(self):
        self._history = []

    def save_state(self, memento: TextEditorMemento):
        self._history.append(memento)

    def undo(self) -> TextEditorMemento:
        if self._history:
            memento = self._history.pop()
            print("Undoing state change.")
            return memento
        else:
            print("No state to restore.")
            return None

# Client code demonstrating the Memento Design Pattern.
if __name__ == "__main__":
    editor = TextEditor()
    caretaker = Caretaker()

    # User types some text.
    editor.type("Hello, ")
    caretaker.save_state(editor.save())

    editor.type("World!")
    caretaker.save_state(editor.save())

    editor.type(" This is a Memento Pattern demo.")
    
    # Undo last change.
    memento = caretaker.undo()
    if memento:
        editor.restore(memento)

    # Undo one more change.
    memento = caretaker.undo()
    if memento:
        editor.restore(memento)
