import random

from errbot import BotPlugin, botcmd, botmatch


class Guess(BotPlugin):
    @botcmd
    def tryme(self, msg, _):
        """Start to guess a number !"""
        msg.ctx["tries"] = 10
        msg.ctx["to_guess"] = random.randint(0, 99)
        return "Guess a number between 0 and 99!"

    @botmatch(r"^\d{1,2}$", flow_only=True)
    def guessing(self, msg, match):
        guess = int(match.string)
        to_guess = msg.ctx["to_guess"]
        if guess == to_guess:
            msg.ctx["tries"] = 0
            return "You won !"

        msg.ctx["tries"] -= 1
        if msg.ctx["tries"] == 0:
            return "No more tries, you lost!"

        if guess < to_guess:
            return "More! %d tries left" % msg.ctx["tries"]

        return "Less! %d tries left" % msg.ctx["tries"]
