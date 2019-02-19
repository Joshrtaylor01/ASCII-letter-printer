
class OUTPUT:

    def __init__(self, line_one, line_two, line_three, line_four, line_five, line_six):
        self.line_one = line_one
        self.line_two = line_two
        self.line_three = line_three
        self.line_four = line_four
        self.line_five = line_five
        self.line_six = line_six

    def print_letters(self):
        return self.line_one + '\n' + self.line_two + '\n' + self.line_three + '\n' + self.line_four + '\n' + self.line_five + '\n' + self.line_six + '\n'

    ASCII = 0

    def add_letter(self, ASCII):

        if ASCII == 32:
            self.line_one +=   '    '
            self.line_two +=   '    '
            self.line_three += '    '
            self.line_four +=  '    '
            self.line_five +=  '    '
            self.line_six +=   '    '

        if ASCII == 65:
            self.line_one +=   '           '
            self.line_two +=   '     /\    '
            self.line_three += '    /  \   '
            self.line_four +=  '   / /\ \  '
            self.line_five +=  '  / ____ \ '
            self.line_six +=   ' |_/    \_|'

        if ASCII == 66:
            self.line_one +=   '  ____  '
            self.line_two +=   ' |  _ \ '
            self.line_three += ' | |_) |'
            self.line_four +=  ' |  _ < '
            self.line_five +=  ' | |_) |'
            self.line_six +=   ' |____/ '

        if ASCII == 67:
            self.line_one +=   '   _____ '
            self.line_two +=   '  / ____|'
            self.line_three += ' | |     '
            self.line_four +=  ' | |     '
            self.line_five +=  ' | |____ '
            self.line_six +=   '  \_____|'

        if ASCII == 68:
            self.line_one +=   '  _____  '
            self.line_two +=   ' |  __ \ '
            self.line_three += ' | |  | |'
            self.line_four +=  ' | |  | |'
            self.line_five +=  ' | |__| |'
            self.line_six +=   ' |_____/ '

        if ASCII == 69:
            self.line_one +=   '  ______ '
            self.line_two +=   ' |  ____|'
            self.line_three += ' | |__   '
            self.line_four +=  ' |  __|  '
            self.line_five +=  ' | |____ '
            self.line_six +=   ' |______|'

        if ASCII == 70:
            self.line_one +=   '  ______ '
            self.line_two +=   ' |  ____|'
            self.line_three += ' | |__   '
            self.line_four +=  ' |  __|  '
            self.line_five +=  ' | |     '
            self.line_six +=   ' |_|     '

        if ASCII == 71:
            self.line_one +=   '   _____ '
            self.line_two +=   '  / ____|'
            self.line_three += ' | |  __ '
            self.line_four +=  ' | | |_ |'
            self.line_five +=  ' | |__| |'
            self.line_six +=   '  \_____|'

        if ASCII == 72:
            self.line_one +=   '  _    _ '
            self.line_two +=   ' | |  | |'
            self.line_three += ' | |__| |'
            self.line_four +=  ' |  __  |'
            self.line_five +=  ' | |  | |'
            self.line_six +=   ' |_|  |_|'

        if ASCII == 73:
            self.line_one +=   '  _____ '
            self.line_two +=   ' |_   _|'
            self.line_three += '   | |  '
            self.line_four +=  '   | |  '
            self.line_five +=  '  _| |_ '
            self.line_six +=   ' |_____|'

        if ASCII == 74:
            self.line_one +=   '       _ '
            self.line_two +=   '      | |'
            self.line_three += '      | |'
            self.line_four +=  '  _   | |'
            self.line_five +=  ' | |__| |'
            self.line_six +=   '  \____/ '

        if ASCII == 75:
            self.line_one +=   '  __    __'
            self.line_two +=   ' |  | /  /'
            self.line_three += ' |  |/  / '
            self.line_four +=  ' |     <  '
            self.line_five +=  ' |  |\  \ '
            self.line_six +=   ' |__| \__|'

        if ASCII == 76:
            self.line_one +=   '  _      '
            self.line_two +=   ' | |     '
            self.line_three += ' | |     '
            self.line_four +=  ' | |     '
            self.line_five +=  ' | |____ '
            self.line_six +=   ' |______|'

        if ASCII == 77:
            self.line_one +=   '  __  __ '
            self.line_two +=   ' |  \/  |'
            self.line_three += ' | \  / |'
            self.line_four +=  ' | |\/| |'
            self.line_five +=  ' | |  | |'
            self.line_six +=   ' |_|  |_|'

        if ASCII == 78:
            self.line_one +=   '  _   _ '
            self.line_two +=   ' | \ | |'
            self.line_three += ' |  \| |'
            self.line_four +=  ' | . ` |'
            self.line_five +=  ' | |\  |'
            self.line_six +=   ' |_| \_|'

        if ASCII == 79:
            self.line_one +=   '   ____  '
            self.line_two +=   '  / __ \ '
            self.line_three += ' | |  | |'
            self.line_four +=  ' | |  | |'
            self.line_five +=  ' | |__| |'
            self.line_six +=   '  \____/ '

        if ASCII == 80:
            self.line_one +=   '  _____  '
            self.line_two +=   ' |  __ \ '
            self.line_three += ' | |__) |'
            self.line_four +=  ' |  ___/ '
            self.line_five +=  ' | |     '
            self.line_six +=   ' |_|     '

        if ASCII == 81:
            self.line_one +=   '   ____   '
            self.line_two +=   '  / __ \  '
            self.line_three += ' | |  | | '
            self.line_four +=  ' | |  |_| '
            self.line_five +=  ' | |__\ \ '
            self.line_six +=   '  \___|\_|'

        if ASCII == 82:
            self.line_one +=   '  _____  '
            self.line_two +=   ' |  __ \ '
            self.line_three += ' | |__) |'
            self.line_four +=  ' |  _  / '
            self.line_five +=  ' | | \ \ '
            self.line_six +=   ' |_|  \_|'

        if ASCII == 83:
            self.line_one +=   '   _____ '
            self.line_two +=   '  / ____|'
            self.line_three += ' | (___  '
            self.line_four +=  '  \___ \ '
            self.line_five +=  '  ____) |'
            self.line_six +=   ' |_____/ '

        if ASCII == 84:
            self.line_one += '  _______ '
            self.line_two += ' |__   __|'
            self.line_three += '    | |   '
            self.line_four += '    | |   '
            self.line_five += '    | |   '
            self.line_six +=  '    |_|   '

        if ASCII == 85:
            self.line_one += '  _    _ '
            self.line_two += ' | |  | |'
            self.line_three += ' | |  | |'
            self.line_four += ' | |  | |'
            self.line_five += ' | |__| |'
            self.line_six += '  \____/ '

        if ASCII == 86:
            self.line_one += ' __      __'
            self.line_two += ' \ \    / /'
            self.line_three += '  \ \  / / '
            self.line_four += '   \ \/ /  '
            self.line_five += '    \  /   '
            self.line_six += '     \/    '

        if ASCII == 87:
            self.line_one += ' __          __'
            self.line_two += ' \ \        / /'
            self.line_three += '  \ \  /\  / / '
            self.line_four += '   \ \/  \/ /  '
            self.line_five += '    \  /\  /   '
            self.line_six += '     \/  \/    '

        if ASCII == 88:
            self.line_one +=   ' __   __'
            self.line_two +=   ' \ \ / /'
            self.line_three += '  \ V / '
            self.line_four +=  '   > <  '
            self.line_five +=  '  / . \ '
            self.line_six +=   ' /_/ \_|'

        if ASCII == 89:
            self.line_one +=   ' __     __'
            self.line_two +=   ' \ \   / /'
            self.line_three += '  \ \_/ / '
            self.line_four +=  '   \   /  '
            self.line_five +=  '    | |   '
            self.line_six +=   '    |_|   '

        if ASCII == 90:
            self.line_one +=   '  ______'
            self.line_two +=   ' |___  /'
            self.line_three += '    / / '
            self.line_four +=  '   / /  '
            self.line_five +=  '  / /__ '
            self.line_six +=   ' /_____|'



