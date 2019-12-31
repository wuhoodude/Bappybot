from invoker import ReplyObject, Command

def bap(params):
    return ReplyObject("BAP", True)
commands = [
    Command(['bap'], bap),
    Command(['bear'], lambda: ReplyObject("\\\\{\\\\^\\\\°(T)°\\\\^\\\\}\\\\", True)),

]